# setup.py
from setuptools import setup, find_packages

setup(
    name="optidocs",
    version="0.1",
    packages=find_packages(include=["core*"]),
    install_requires=[
        "django>=4.0",
    ],
)
