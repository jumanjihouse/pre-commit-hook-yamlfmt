################################################################################
# Style file for markdownlint.
#
# https://github.com/markdownlint/markdownlint/blob/master/docs/configuration.md
#
# This file is referenced by the project `.mdlrc`.
################################################################################

# Start with all built-in rules.
all

# Allow both fenced and indented code blocks.
rule 'MD046', style: ['fenced', 'indented']

# Ignore line length in code blocks.
rule 'MD013', code_blocks: false

# I prefer two blank lines before each heading.
exclude_rule 'MD012' # Multiple consecutive blank lines

# I find it necessary to use '<br/>' to force line breaks.
exclude_rule 'MD033' # Inline HTML

# If a page is printed, it helps if the URL is viewable.
exclude_rule 'MD034' # Bare URL used
