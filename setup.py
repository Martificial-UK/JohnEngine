from setuptools import setup, find_packages

setup(
    name="JohnEngine",
    version="0.1.0",
    description="Reusable engine core for automation products.",
    author="Your Name",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
)
