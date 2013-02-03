#!/usr/bin/env python
from setuptools import setup


setup(
    name = "pylicense",
    version = 1,
    description = """License extractor from the python eggs.""",
    author = "Ilja Livenson",
    author_email = "ilja.livenson@gmail.com",
    packages = ['pylicense'],
    license = 'BSD',
    entry_points = {'console_scripts': ['pylicense = pylicense.pylicense:run']
                   },
    install_requires = [
            "setuptools",
        ]
)
