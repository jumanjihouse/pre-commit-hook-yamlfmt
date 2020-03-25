#!/bin/bash
set -eEu
set -o pipefail

################################################################################
# Prepare the local dev environment.
# Invoke from the root of the git repo as "ci/bootstrap".
################################################################################

PROG="$(basename "$0")"
readonly PROG

finish() {
    declare -ri RC=$?

    if [[ $RC -eq 0 ]]; then
        pass "$0 OK"
    else
        err "$0 failed with exit status $RC"
    fi
}

trap finish EXIT

err() {
    echo "[ERROR] $*" >&2
}

info() {
    echo "[INFO] $*" >&2
}

pass() {
    echo "[PASS] $*" >&2
    echo
}

run() {
    echo "[RUN] $*" >&2
    "$@"
    echo
}

needs_bootstrap() {
    if [[ "${PROG}" == bootstrap ]]; then
        return 1
    fi
    readonly SEMAPHORE="ci/.bootstrap"
    if [[ ci/bootstrap -nt "${SEMAPHORE}" ]] ||
        [[ ci/requirements.txt -nt "${SEMAPHORE}" ]]; then
        return 0
    fi
    return 1
}

if needs_bootstrap; then
    ci/bootstrap
fi
