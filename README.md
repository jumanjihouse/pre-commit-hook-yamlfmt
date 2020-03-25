# Pre-commit git hooks

YAML formatter for [pre-commit](http://pre-commit.com).

This hook formats the indentation of YAML files and
optionally aligns top-level colons.<br/>
It uses [ruamel.yaml](https://yaml.readthedocs.io/en/latest/)
to do the heavy lifting and preserve comments within YAML files.

<!--TOC-->

- [How-to](#how-to)
  - [Configure pre-commit](#configure-pre-commit)
    - [Use defaults](#use-defaults)
    - [Combine with `yamllint`](#combine-with-yamllint)
    - [Override defaults](#override-defaults)
  - [Invoke pre-commit](#invoke-pre-commit)
    - [On every commit](#on-every-commit)
    - [On demand](#on-demand)
- [Contributing](#contributing)
- [Testing](#testing)
- [License](#license)

<!--TOC-->

## How-to

### Configure pre-commit

#### Use defaults

Add to `.pre-commit-config.yaml` in your git repo:

    - repo: https://github.com/jumanjihouse/yamlfmt
      rev:  # valid tag
      hooks:
          - id: yamlfmt


#### Combine with `yamllint`

`yamlfmt` only works with valid YAML files, so
I recommend to use `yamllint` and `yamlfmt` together.

    - repo: https://github.com/adrienverge/yamllint.git
      rev: v1.21.0
      hooks:
          - id: yamllint
            args: [--format, parsable, --strict]

    - repo: https://github.com/jumanjihouse/yamlfmt
      rev:  # valid tag
      hooks:
          - id: yamlfmt


#### Override defaults

Add to `.pre-commit-config.yaml` in your git repo:

    - repo: https://github.com/jumanjihouse/yamlfmt
      rev:  # valid tag
      hooks:
          - id: yamlfmt
            args: [--mapping, '2', --sequence, '2', --offset, '0', --colons]


### Invoke pre-commit

#### On every commit

If you want to invoke the checks as a git pre-commit hook, run:

    # Run on every commit.
    pre-commit install


#### On demand

If you want to run the checks on-demand (outside of git hooks), run:

    # Run on-demand.
    pre-commit run --all-files

The [test harness](TESTING.md) of this git repo uses this approach.


## Contributing

Please see [CONTRIBUTING.md](CONTRIBUTING.md).


## Testing

Please see [TESTING.md](TESTING.md).


## License

The code in this repo is licensed under the [MIT License](LICENSE).
