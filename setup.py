"""Fake setup for pre-commit hook."""

from setuptools import setup

setup(
    name='yamlfmt',
    description='A pre-commit hook to format YAML files',
    url='https://github.com/jumanjihouse/pre-commit-hook-yamlfmt',
    version='0.0.0',

    # globally-unique name
    packages=[
        'jumanjihouse_precommit_yamlfmt',
    ],

    install_requires=[
        'ruamel.yaml>=0.16.10',
    ],

    scripts=[
        'pre_commit_hooks/yamlfmt',
    ],
)
