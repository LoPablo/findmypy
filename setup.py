from setuptools import setup, find_packages

REPO_URL = "https://github.com/picklepete/pyicloud"
VERSION = "0.1.0"

setup(
    name="findmypy",
    author="LoPablo",
    author_email="lopablo@protonmail.com",
    description="Library to use Apple's FindMy Api.",
    version=VERSION,
    url=REPO_URL,
    packages=find_packages(include=["findmypy"]),
    install_requires=required,
    python_requires=">=3.7",
    license="MIT",
    classifiers=[
        "Development Status :: 1",
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