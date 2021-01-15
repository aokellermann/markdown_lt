#!/usr/bin/env bash

set -eo pipefail

pylint --rcfile=setup.cfg markdown_lt setup.py
shellcheck scripts/hooks/* scripts/*.sh bin/markdown_lt
./bin/markdown_lt --language en-US --enabled-only --enable MORFOLOGIK_RULE_EN_US --wordlist dict.txt README.md
