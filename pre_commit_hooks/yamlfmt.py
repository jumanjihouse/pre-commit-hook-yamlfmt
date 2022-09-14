"""Format YAML files."""

import sys
import argparse
from ruamel.yaml import YAML  # pylint: disable=import-error

DEFAULT_INDENT = {
    "mapping": 4,
    "sequence": 6,
    "offset": 4,
    }


class Cli:
    # pylint: disable=too-few-public-methods
    """Command-line-interface."""

    def __init__(self):
        """Initialize the CLI."""
        parser = argparse.ArgumentParser(
            description="Format YAML files",
            formatter_class=argparse.ArgumentDefaultsHelpFormatter,
            epilog="Tips at https://yaml.readthedocs.io/en/latest/detail.html",
            )
        parser.add_argument(
            "-m",
            "--mapping",
            type=int,
            default=DEFAULT_INDENT["mapping"],
            help="number of spaces to indent mappings (dictionaries)",
            )
        parser.add_argument(
            "-s",
            "--sequence",
            type=int,
            default=DEFAULT_INDENT["sequence"],
            help="number of spaces to indent sequences (arrays/lists)",
            )
        parser.add_argument(
            "-o",
            "--offset",
            type=int,
            default=DEFAULT_INDENT["offset"],
            help="number of spaces to offset the dash from sequences",
            )
        parser.add_argument(
            "-c",
            "--colons",
            action="store_true",
            help="whether to align top-level colons",
            )
        parser.add_argument(
            "-w",
            "--width",
            type=int,
            default=150,
            help="maximum line width",
            )
        parser.add_argument(
            "-p",
            "--preserve-quotes",
            action="store_true",
            help="whether to keep existing string quoting"
            )

        document_start = parser.add_mutually_exclusive_group()
        document_start.add_argument(
            "--implicit_start",
            "-e",
            action="store_false",
            dest="explicit_start",
            default=argparse.SUPPRESS,
            help="whether to remove the explicit document start"
            )
        document_start.add_argument(
            "--explicit_start",
            action="store_true",
            dest="explicit_start",
            default=True,
            help="whether to add the explicit document start"
            )

        document_end = parser.add_mutually_exclusive_group()
        document_end.add_argument(
            "--implicit_end",
            action="store_false",
            dest="explicit_end",
            default=argparse.SUPPRESS,
            help="whether to remove the explicit document end"
            )
        document_end.add_argument(
            "--explicit_end",
            action="store_true",
            dest="explicit_end",
            default=False,
            help="whether to add the explicit document end"
            )

        parser.add_argument(
            "-n",
            "--preserve_null",
            action="store_true",
            help="whether to keep null values"
            )
        parser.add_argument(
            "file_names",
            metavar="FILE_NAME",
            nargs="*",
            help="space-separated list of YAML file names",
            )

        self.parser = parser


class Formatter:
    """
    Reformat a yaml file with proper indentation.

    Preserve comments.
    """

    def __init__(self, **kwargs):
        """Initialize the formatter."""
        yaml = YAML()
        yaml.indent(
            mapping=kwargs.get("mapping", DEFAULT_INDENT["mapping"]),
            sequence=kwargs.get("sequence", DEFAULT_INDENT["sequence"]),
            offset=kwargs.get("offset", DEFAULT_INDENT["offset"]),
            )
        yaml.top_level_colon_align = kwargs.get("colons", False)
        yaml.explicit_start = kwargs.get("explicit_start", True)
        yaml.explicit_end = kwargs.get("explicit_end", False)
        yaml.width = kwargs.get("width", None)
        yaml.preserve_quotes = kwargs.get("preserve_quotes", False)

        if kwargs.get("preserve_null"):
            def represent_none(self, _data):
                return self.represent_scalar('tag:yaml.org,2002:null', 'null')
            yaml.representer.add_representer(type(None), represent_none)

        self.yaml = yaml
        self.path = kwargs.get("path", None)
        self.content = list({})

    def format(self, path=None):
        """Read file and write it out to same path."""
        if not path:
            path = self.path
        print(path, end="")
        self.parse_file(path)
        self.write_file(path)
        print("  Done")

    def parse_file(self, path=None):
        """Read the file."""
        if not path:
            path = self.path
        try:
            with open(path, "r", encoding='utf-8') as stream:
                self.content = list(self.yaml.load_all(stream))
        except IOError:
            self.fail(f"Unable to read {path}")

    def write_file(self, path=None):
        """Write the file."""
        if not path:
            path = self.path
        try:
            with open(path, "w", encoding='utf-8') as stream:
                self.yaml.dump_all(self.content, stream)
        except IOError:
            self.fail(f"Unable to write {path}")

    @staticmethod
    def fail(msg):
        """Abort."""
        sys.stderr.write(msg)
        sys.exit(1)


def main():
    """Fit formatter."""
    args = Cli().parser.parse_args()
    formatter = Formatter(
        mapping=args.mapping,
        sequence=args.sequence,
        offset=args.offset,
        colons=args.colons,
        width=args.width,
        preserve_quotes=args.preserve_quotes,
        preserve_null=args.preserve_null,
        explicit_start=args.explicit_start,
        explicit_end=args.explicit_end
        )
    for file_name in args.file_names:
        formatter.format(file_name)


if __name__ == "__main__":
    main()
