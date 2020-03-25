from setuptools import setup

setup(
    name='require-ascii',
    description='A pre-commit hook to check that text files are ascii-encoded',
    url='https://github.com/jumanjihouse/pre-commit-hooks',
    version='0.0.0',

    packages=[
        'pre_commit_hooks',
    ],

    install_requires=[
        'rueaml',
    ],

    scripts=[
        'pre_commit_hooks/yamlfmt.py',
    ],
)
