import setuptools
from setuptools import setup

setup(
    name="geo",
    version="1.0",
    description="A little collection of python scripts to help with high school geometry.",
    author="Qtechinnovation",
    author_email="qtechinnovation@gmail.com",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": [
            "geo=geo.geo:main"
        ]
    }
)