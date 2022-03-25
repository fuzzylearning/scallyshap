from setuptools import setup, find_packages

with open("README.md", "r") as readme_file:
    readme = readme_file.read()

requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]

setup(
    name="scallyshap",
    version="0.0.2",
    author="Hossein Javedani Sadaei",
    author_email="h.javedani@gmail.com",
    description="SHAP feature selection for large scale projects",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/fuzzylearning/scallyshap",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: BSD License",
    ],
)