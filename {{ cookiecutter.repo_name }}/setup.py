from pathlib import Path
from setuptools import find_namespace_packages, setup

BASE_DIR = Path(__file__).parent
long_description = (BASE_DIR / "README.md").read_text()

# Load packages from requirements.txt
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines() if not ln.startswith("#")]


test_packages = [
    "pytest"
]

dev_packages = [
    "flake8",
    "isort",
    "autopep8",
    "pre-commit"
]

docs_packages = [
    "sphinx==4.5.0",
    "sphinx-autobuild"
]


setup(
    name='{{ cookiecutter.package_name }}',
    packages=find_namespace_packages(),
    version='0.0.1',
    description='{{ cookiecutter.description }}',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="{{ cookiecutter.author_name }}",
    python_requires=">=3.8",
    install_requires=[required_packages],
    extras_require={
        "test": test_packages,
        "dev": test_packages + dev_packages + docs_packages,
        "docs": docs_packages,
    }
)
