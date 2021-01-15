#!/usr/bin/env bash

set -eo pipefail

git checkout -q @^
previous_version="$(python -c 'import markdown_lt; print(markdown_lt.__version__)')"

git checkout -q feature/Spelling
current_version="$(python -c 'import markdown_lt; print(markdown_lt.__version__)')"

if [ "$previous_version" != "$current_version" ] && [ "$CIRCLE_BRANCH" = "master" ]; then
  rm -rf build/ dist/
  python setup.py sdist bdist_wheel
  twine check dist/*
  twine upload dist/* --verbose --username "__token__" --password "$PYPI_TOKEN_MARKDOWN_LT"
fi
