#!/bin/bash

errexit () {
    echo "Error: $1" >&2
    exit "${2:-1}"  # exit 1 by default
}

SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
VENV_DIR="$SCRIPT_DIR/.venv"

[ -d "$VENV_DIR" ] || errexit "No .venv"


run() {
    PATH="$VENV_DIR/bin" "$@"
}

run "$@"
