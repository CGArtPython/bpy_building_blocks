from setuptools import setup
import pathlib

README_TEXT = pathlib.Path(__file__).parent.joinpath("README.md").read_text()

# imports __version__ without importing the bpybb package
exec(pathlib.Path(__file__).parent.joinpath("src", "bpybb", "version.py").read_text())

setup(
    name="bpy_building_blocks",
    version=__version__,
    description="A collection of helper functions and code used for speeding up Blender 3D Python script development.",
    long_description=README_TEXT,
    long_description_content_type="text/markdown",
    url="https://github.com/CGArtPython/bpy_building_blocks",
    author="Viktor Stepanov",
    author_email="cgartpython@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
    ],
    packages=["bpybb"],
    package_dir={"": "src"},
)
