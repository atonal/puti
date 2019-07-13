#!/usr/bin/env bash

set -eo pipefail

DIR=$(readlink -f "$(dirname "${BASH_SOURCE[0]}")")

export PYTHONPATH=${PYTHONPATH}:${DIR}/../blog-generator
export PYTHONPATH=${PYTHONPATH}:${DIR}/../putisplain
export FLASK_APP=${DIR}/putify.py
export FLASK_ENV=development
cd "${DIR}"
pipenv run flask run --host=0.0.0.0
