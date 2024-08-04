from setuptools import setup, find_packages
import os

# Get the long description from the README file
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Read the version from __init__.py
with open(os.path.join("dbsys", "__init__.py"), "r") as f:
    for line in f:
        if line.startswith("__version__"):
            version = line.split("=")[1].strip().strip('"')
            break

setup(
    name="dbsys",
    version="0.1.13",
    author="Mark Powers",
    author_email="mpoweru@lifsys.com",
    description="A library for managing database operations using SQLAlchemy and pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lifsys/dbsys",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=1.0.0",
        "sqlalchemy>=1.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "flake8>=4.0",
            "black>=22.0",
            "mypy>=0.900",
            "isort>=5.0",
        ],
    },
    keywords="database sqlalchemy pandas orm data management",
    project_urls={
        "Bug Tracker": "https://github.com/lifsys/dbsys/issues",
        "Documentation": "https://github.com/lifsys/dbsys/blob/main/README.md",
        "Source Code": "https://github.com/lifsys/dbsys",
    },
    include_package_data=True,
    package_data={"dbsys": ["py.typed"]},
)
from setuptools import setup, find_packages
from dbsys import __version__

setup(
    name="dbsys",
    version=__version__,
    packages=find_packages(),
    install_requires=[
        "pandas",
        "sqlalchemy",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package for managing database operations",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/dbsys",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
