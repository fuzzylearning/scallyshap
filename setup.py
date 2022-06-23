import sys
sys.path.append("./scallyshap/src")
from setuptools import find_packages, setup
from version import __version__

__version__ = "0.0.4"

with open("README.md", "r") as readme_file:
    readme = readme_file.read()


with open('requirements.txt') as f:
    required = f.read().splitlines()

requirements = ["ipython>=6"]

setup(
    name="scallyshap",
    version=__version__,
    author="Hossein Javedani Sadaei",
    author_email="h.javedani@gmail.com",
    description="SHAP feature selection for large scale projects",
    long_description=readme,
    install_requires=required,
    packages=['scallyshap'],
    long_description_content_type="text/markdown",
    url="https://github.com/fuzzylearning/scallyshap",
    classifiers=[
        "Programming Language :: Python :: 3.10.0",
        "License :: OSI Approved :: BSD License",
    ],

    entry_points='''
        [console_scripts]
        scallyshap=scallyshap.src.cli:cligroup
    ''',

)
