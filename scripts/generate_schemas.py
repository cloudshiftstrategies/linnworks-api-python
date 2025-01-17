import os
from pathlib import Path
import subprocess
import logging
import shutil
import re

logging.basicConfig(level=os.getenv("LOG_LEVEL", logging.INFO))
formatter = logging.Formatter("%(levelname)s: %(message)s")
logging.getLogger().handlers.clear()
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logging.getLogger().addHandler(handler)


def sanitize_module_name(name: str) -> str:
    """
    Convert a string to a valid Python module name.
    - Replace dashes with underscores
    - Replace spaces with underscores
    - Remove any other invalid characters
    - Ensure it doesn't start with a number
    """
    # Replace dashes and spaces with underscores
    name = name.replace("-", "_").replace(" ", "_")

    # Remove any characters that aren't alphanumeric or underscore
    name = "".join(c for c in name if c.isalnum() or c == "_")

    # Ensure it doesn't start with a number
    if name[0].isdigit():
        name = f"_{name}"

    return name


def find_swagger_files(directory: str) -> list[str]:
    swagger_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith((".json", ".yaml", ".yml")):  # Support both JSON and YAML
                swagger_files.append(os.path.join(root, file))
    return swagger_files


def fix_pydantic_conflicts(file_path: Path) -> None:
    """Fix field names that conflict with Pydantic BaseModel attributes."""
    if not file_path.exists():
        return

    content = file_path.read_text()

    # Replace "register" field with "register_field"
    content = re.sub(r"(\s+)register: typing\.Optional\[(.+?)\]", r"\1register_field: typing.Optional[\2]", content)
    content = re.sub(r'(\s+)"register":', r'\1"register_field":', content)

    file_path.write_text(content)


def generate_clients():
    logging.info("Generating Linnworks API clients")
    base_dir = Path(__file__).parent.parent
    specs_dir = base_dir / "PublicApiSpecs"
    output_dir = base_dir / "src" / "linnworks_api" / "generated"
    logging.debug(f"Base dir: {base_dir}")
    logging.debug(f"Specs dir: {specs_dir}")
    logging.debug(f"Output dir: {output_dir}")

    # Create output directory if it doesn't exist
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create empty __init__.py with package name prefix
    init_file = output_dir / "__init__.py"
    init_file.write_text('"""Generated Linnworks API client models."""\n\n')
    logging.debug(f"Created Init file: {init_file}")

    swagger_files = find_swagger_files(str(specs_dir))
    package_name = "linnworks_api"

    for input_file in swagger_files:
        model_name = sanitize_module_name(Path(input_file).stem)
        if model_name == "orders_v2":
            # from linnworks_api.generated.orders_v2.models \
            # .one_of_order_item_anonymous_order_item_with_children_order_item_with_children
            # import OneOfOrderItemAnonymousOrderItemWithChildrenOrderItemWithChildren
            logging.info(f"Skipping {model_name} as we have trouble with it")
            continue
        logging.info(f"Generating model: {model_name}")
        model_dir = output_dir / model_name
        temp_dir = model_dir.with_name(f"{model_name}_temp")
        logging.debug(f"Model dir: {model_dir}")
        logging.debug(f"Temp dir: {temp_dir}")
        model_dir.mkdir(exist_ok=True)
        base_client = base_dir / "src" / "linnworks_api" / "base_client.py"
        logging.debug(f"Base client: {base_client}")

        try:
            # Generate into a temporary directory first
            cmd = [
                "openapi-generator-cli",
                "generate",
                "-i",
                input_file,
                "-g",
                "python",
                "-o",
                str(temp_dir),
                "--package-name",
                f"{package_name}.generated.{model_name}",
                "--skip-validate-spec",
                "--global-property",
                "apiTests=false,modelTests=false",
                "--additional-properties",
                "packageUrl=,generateSourceCodeOnly=true,projectName=linnworks-api-python,"
                "packageVersion=1.0.0,generateSetupPy=false,"
                "generateTox=false,generateGitIgnore=false,"
                "hideGenerationTimestamp=true",
            ]
            logging.debug(f"Running command: {cmd}")
            subprocess.run(cmd, check=True, capture_output=True, text=True)

            # Move the generated files from nested directory to the correct location
            generated_dir = temp_dir / "linnworks_api" / "generated" / model_name
            logging.debug(f"Generated dir: {generated_dir}")
            if not generated_dir.exists():
                logging.error(f"Generated dir does not exist: {generated_dir}")
                raise SystemExit(1)
            # Remove existing files in target directory
            if model_dir.exists():
                logging.debug(f"Removing existing files in {model_dir}")
                shutil.rmtree(model_dir)
            # Move files to correct location
            logging.debug(f"Moving files from {generated_dir} to {model_dir}")
            shutil.move(str(generated_dir), str(model_dir))

            # Add base_client.py to the model directory
            base_client_file = model_dir / "base_client.py"
            logging.debug(f"Adding base_client.py to {model_dir}")
            base_client_file.write_text(base_client.read_text())

            # Clean up temp directory
            logging.debug(f"Cleaning up temp directory {temp_dir}")
            shutil.rmtree(temp_dir)

            # After moving files to correct location
            model_files = list(model_dir.rglob("*.py"))
            for file in model_files:
                fix_pydantic_conflicts(file)

        except subprocess.CalledProcessError as e:
            logging.error(f"Error generating client for {input_file}:")
            logging.error(f"Exit code: {e.returncode}")
            logging.error(f"stdout: {e.stdout}")
            logging.error(f"stderr: {e.stderr}")
            raise SystemExit(1)
        except OSError as e:
            logging.error(f"Error handling files for {model_name}: {e}")
            raise SystemExit(1)
        except Exception as e:
            logging.error(f"Error processing generated files: {e}")
            raise SystemExit(1)

        # Use absolute imports in __init__.py
        try:
            logging.debug(f"Updating {init_file}")
            with init_file.open("a") as f:
                f.write(f"from {package_name}.generated.{model_name} import *\n")
        except IOError as e:
            logging.error(f"Error writing to __init__.py: {e}")
            raise SystemExit(1)


if __name__ == "__main__":
    try:
        generate_clients()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        raise SystemExit(1)
