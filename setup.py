from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name='cnl',
    version='1.0',
    description=' A library of tools for use with complex numbers ',
    license="Apache-3.0",
    long_description=long_description,
    author='William Meathrel',
    author_email='wcmeathrel@gmail.com',
    url="https://github.com/wm-c/CNL",
    packages=['cnl'],
    install_requires=[],
    platforms=["Platform Independent"]
)
