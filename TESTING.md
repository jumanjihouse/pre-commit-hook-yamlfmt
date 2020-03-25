# Test harness

## Dependencies

* [`bash`](https://www.gnu.org/software/bash/bash.html)
* [`git`](https://github.com/git/git)
* [`pip3`](http://www.pip-installer.org) command


## How-to

Run:

    ci/build && ci/test

Output resembles:

    [RUN] ci/toc
          ./README.md OK
          ./CONTRIBUTING.md OK

    [PASS] ci/build OK

    [RUN] pre_commit_hooks/yamlfmt --help
    usage: yamlfmt [-h] [-m MAPPING] [-s SEQUENCE] [-o OFFSET] [-c] [FILE_NAME [FILE_NAME ...]]

    Format YAML files

    positional arguments:
      FILE_NAME             space-separated list of YAML file names (default: None)

    optional arguments:
      -h, --help            show this help message and exit
      -m MAPPING, --mapping MAPPING
                            number of spaces to indent mappings (dictionaries) (default: 4)
      -s SEQUENCE, --sequence SEQUENCE
                            number of spaces to indent sequences (arrays/lists) (default: 6)
      -o OFFSET, --offset OFFSET
                            number of spaces to offset the dash from sequences (default: 4)
      -c, --colons          whether to align top-level colons (default: False)

    Tips at https://yaml.readthedocs.io/en/latest/detail.html


    [RUN] pre_commit_hooks/yamlfmt --mapping 4 --sequence 6 --offset 4 ./.pre-commit-config.yaml
    ./.pre-commit-config.yaml  Done

    [RUN] pre_commit_hooks/yamlfmt --mapping 4 --sequence 6 --offset 4 ./.pre-commit-hooks.yaml
    ./.pre-commit-hooks.yaml  Done

    [INFO] Use with xargs
    ./.pre-commit-config.yaml  Done
    ./.pre-commit-hooks.yaml  Done

    [RUN] pre_commit_hooks/yamlfmt -m 2 -s 2 -o 0 .pre-commit-hooks.yaml
    .pre-commit-hooks.yaml  Done

    [RUN] pre-commit run --all-files --hook-stage manual
    yamllint......................................................................Passed
    Format YAML files.............................................................Passed
    Format YAML files with overrides..............................................Passed
    Detect if an email address needs to be added to mailmap.......................Passed
    Forbid binaries...........................................(no files to check)Skipped
    Check for conflict markers and core.whitespace errors.........................Passed
    Check if the git tree is dirty................................................Passed
    Check markdown files..........................................................Passed
    Check file encoding...........................................................Passed
    Non-executable shell script filename ends in .sh..............................Passed
    Executable shell script omits the filename extension..........................Passed
    Test shell scripts with shellcheck............................................Passed
    Check shell style with shfmt..................................................Passed
    Check for added large files...................................................Passed
    Check for byte-order marker...................................................Passed
    Check for case conflicts......................................................Passed
    Check that executables have shebangs..........................................Passed
    Check JSON................................................(no files to check)Skipped
    Check for merge conflicts.....................................................Passed
    Check for broken symlinks.................................(no files to check)Skipped
    Check vcs permalinks..........................................................Passed
    Check Toml................................................(no files to check)Skipped
    Check Xml.................................................(no files to check)Skipped
    Check Yaml....................................................................Passed
    Detect Private Key............................................................Passed
    Fix requirements.txt..........................................................Passed
    Sort simple YAML files....................................(no files to check)Skipped
    CRLF end-lines checker........................................................Passed
    No-tabs checker...............................................................Passed
    gitlint.......................................................................Passed
    Detect secrets................................................................Passed

    [PASS] ci/test OK
