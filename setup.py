"""Fake setup for pre-commit hook."""

from setuptools import setup, find_packages

setup(
    name='yamlfmt',
    description='A pre-commit hook to format YAML files',
    url='https://github.com/jumanjihouse/pre-commit-hook-yamlfmt',
    version='0.4.0',

    install_requires=[
        'ruamel.yaml >=0.16.10, <=0.17.21',
    ],

    entry_points={
        'console_scripts': [
            'yamlfmt = pre_commit_hooks.yamlfmt:main',
        ],
    },

    # explicitly declare packages so setuptools does not attempt auto discovery
    # taken from https://github.com/pypa/setuptools/issues/3197
    packages=find_packages(),
)
