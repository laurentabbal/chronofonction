from setuptools import setup, find_packages
from pathlib import Path

parent_dir = Path(__file__).resolve().parent

setup(
    name="chronocode",
    version="0.0.1",
    description="Module Chronocode",
    long_description=parent_dir.joinpath("README.md").read_text(),
    long_description_content_type="text/markdown",
    url="https://github.com/laurentabbal/module-chrono",
    author="xxx",
    author_email="xxx@gmail.com",
    license="MIT License",
    packages=find_packages(exclude=("assets", "notebooks", "prints", "script")),
    install_requires=parent_dir.joinpath("requirements.txt").read_text().splitlines(),
    classifiers=[
        "Intended Audience :: Science/Research",
    ],
)
