import setuptools
from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="thermotron",
    version="0.0.1",
    author="Steven Lowery",
    author_email="steven.lowery011@gmail.com",
    description="A package for controlling Thermotron thermal chambers with Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stevenlowery011/thermotron",
    packages=setuptools.find_packages(),
	install_requires=['pyvisa'],
	classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
