from setuptools import setup, Command
import sys
from codecs import open

CURRENT_PYTHON = sys.version_info[:2]
REQUIRED_PYTHON = (3, 5)

if CURRENT_PYTHON < REQUIRED_PYTHON:
    sys.stderr.write(
        """
==========================
Unsupported Python version
==========================
This version of flatway requires at least Python {}.{}, but
you're trying to install it on Python {}.{}. To resolve this,
consider upgrading to a supported Python version.
""".format(
            *(REQUIRED_PYTHON + CURRENT_PYTHON)
        )
    )
    sys.exit(1)

with open("README.md", "r", "utf-8") as f:
    readme = f.read()


class RunTestsCommand(Command):
    description = 'Run unit tests'
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import pytest
        errno = pytest.main(['tests'])  # Replace 'tests' with the directory containing your tests
        sys.exit(errno)


setup(
    name="flatway",
    version="1.0.2",
    description="Python package for flatting of list or tuple.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Paiman Rasoli",
    url="https://github.com/Paiman-Rasoli/flatway",
    author_email="paimanrasoli789@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.5",
    license='MIT',
    keywords=['flat', 'flatten', 'flat list', 'flat tuple', 'flatway'],
    project_urls={
        "Source": "https://github.com/Paiman-Rasoli/flatway",
    },
    package_dir={"": "src"},
    packages=["flatway"],
    install_requires=[
        'pytest'
    ],
    cmdclass={
        'test': RunTestsCommand,
    },
)
