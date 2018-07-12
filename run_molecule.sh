#!/bin/bash -e

# because we can't spawn vagrant VMs in travis-ci, we use a little
# wrapper to determine what exactly gets run during CI

if [ "$CI" = "true" ]; then
    exec molecule lint
else
    exec molecule test
fi
