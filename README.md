# markdown_lt

[![aokellermann](https://circleci.com/gh/aokellermann/markdown_lt.svg?style=svg)](https://app.circleci.com/pipelines/github/aokellermann/markdown_lt)

[LanguageTool](https://languagetool.org/) for markdown files.

## Setup

<<<<<<< HEAD
Install the tool:
=======
Install the environment:
>>>>>>> master

```bash
git clone https://github.com/aokellermann/markdown_lt.git
cd markdown_lt
pip install -e .
```

## Usage

```console
$ python -m markdown_lt --help
Usage: python -m markdown_lt [OPTION]... FILE
 FILE                           markdown file to check
 Available options:
  -h, --help                    print usage information
  -l, --language LANG           the language code of the text
  -m, --mother-tongue LANG      the language code of your mother tongue
  -w, --wordlist DICT           a newline separated file of valid words
  -o, --enabled-only            disable all rules except those specified in -e
  -e, --enable RULES            comma-separated list of rule IDs to enable
  -d, --disable RULES           comma-separated list of rule IDs to disable
 Exit code:
  0                             no errors
  1                             language errors
  2                             user error
```
