#!/usr/bin/env bash

set -eo pipefail

pylint --rcfile=setup.cfg markdown_lt setup.py
shellcheck scripts/hooks/* scripts/*.sh
