#!/bin/bash
set -uo pipefail

mkdir -p /logs/verifier

pytest /tests/test_outputs.py \
    --ctrf=/logs/verifier/ctrf.json \
    -rA

EXIT_CODE=$?

if [ "$EXIT_CODE" -eq 0 ]; then
    echo "1" > /logs/verifier/reward.txt
else
    echo "0" > /logs/verifier/reward.txt
fi

exit "$EXIT_CODE"
