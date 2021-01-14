#!/usr/bin/env bash

set -eo pipefail

if [ "$#" -eq 0 ]; then
	yapf --diff --recursive markdown_lt setup.py
	shfmt -l -d scripts
elif [ "$1" == "-i" ]; then
	yapf --in-place --recursive markdown_lt setup.py 2>/dev/null
	shfmt -w scripts
else
	echo "Usage: format.sh [-i]"
	exit 1
fi
