from setuptools import setup

setup(
    name='yamlfmt',
    description='A pre-commit hook to format YAML files',
    url='https://github.com/jumanjihouse/yamlfmt',
    version='0.0.0',

    packages=[
        'pre_commit_hooks',
    ],

    install_requires=[
        'rueaml.yaml',
    ],

    scripts=[
        'pre_commit_hooks/yamlfmt',
    ],
)
