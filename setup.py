from setuptools import setup, find_packages
from pathlib import Path

REPO_URL = "https://github.com/LoPablo/findmypy"
VERSION = "0.1.8"


this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="findmypy",
    author="LoPablo",
    author_email="lopablo@protonmail.com",
    description="Library to use Apple's FindMy Api.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    version=VERSION,
    url=REPO_URL,
    packages=find_packages(include=["findmypy"]),
    package_data={
        "": ["AppleCA.pem"],
    },
    python_requires=">=3.7",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries",
    ],
    keywords=["icloud", "find-my-iphone"],
)