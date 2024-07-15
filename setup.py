from setuptools import setup, find_packages
import dbsys

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="dbsys",
    version=dbsys.__version__,
    author="Mark Powers",
    author_email="mpoweru@lifsys.com",
    description="A library for managing database operations using SQLAlchemy and pandas",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lifsys/dbsys",
    packages=find_packages(exclude=["tests*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Database",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.7",
    install_requires=[
        "pandas>=1.0.0",
        "sqlalchemy>=1.3.0",
    ],
    keywords="database sqlalchemy pandas orm",
    project_urls={
        "Bug Tracker": "https://github.com/lifsys/dbsys/issues",
        "Documentation": "https://github.com/lifsys/dbsys/blob/main/README.md",
        "Source Code": "https://github.com/lifsys/dbsys",
    },
    include_package_data=True,
    package_data={"dbsys": ["py.typed"]},
)
