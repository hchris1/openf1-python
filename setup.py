from setuptools import setup, find_packages

setup(
    name="openf1",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests>=2.25.1", "pydantic>=2.6.3"],
)
