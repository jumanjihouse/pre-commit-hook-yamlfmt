"""Fake setup for pre-commit hook."""

from setuptools import setup
from setuptools import find_packages

setup(
    name='yamlfmt',
    description='A pre-commit hook to format YAML files',
    url='https://github.com/jumanjihouse/pre-commit-hook-yamlfmt',
    version='0.0.0',

    install_requires=[
        'ruamel.yaml>=0.16.10',
    ],

    packages=find_packages(),

    entry_points={
        'console_scripts':
            ['yamlfmt = pre_commit_hooks.yamlfmt:main']},
)
