import os
from setuptools import setup, find_packages

VERSION = "0.6.0"

# Ensure the package directory exists
version_file_path = os.path.join(os.path.dirname(__file__), "dikicli", "__version__.py")
with open(version_file_path, "w") as f:
    f.write(f'__version__ = "{VERSION}"\n')

setup(
    name="dikicli",
    version=VERSION,
    description="Commandline interface for diki.pl polish-english dictionary",
    author="Dawid Zych",
    author_email="dwd@mailo.com",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/silenc3r/dikicli",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: 3 :: Only",
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Education",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Polish",
        "Operating System :: POSIX",
        "Topic :: Education",
    ],
    keywords=["diki", "dictionary"],
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "beautifulsoup4>=4.8",
    ],
    extras_require={"dev": ["pytest>=7.4.0"]},
    entry_points={
        "console_scripts": [
            "diki=dikicli.__main__:main",
        ]
    },
)
