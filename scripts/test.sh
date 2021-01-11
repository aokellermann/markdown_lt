#!/usr/bin/env bash

set -eo pipefail

coverage run --source markdown_lt -m pytest --junitxml=test_results/markdown_lt/report.xml markdown_lt/tests
