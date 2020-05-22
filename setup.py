from setuptools import setup

import os
import re

setup(
    name='caratpost',
    version='0.1',
    packages=[
        'caratpost',
    ],
    author='Thomas Oberbichler',
    author_email='thomas.oberbichler@tum.de',
    install_requires=[
        'numpy',
    ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'carat-post=caratpost.main:main'
        ]
    }
)