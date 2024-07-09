#!/bin/sh

executable_name=wizard
distro=`bin/distro.sh`

executable=./bin/${executable_name}-${distro}
if [ -f ${executable} ]; then
    ${executable}
else
    echo "Unsupported distro ${distro}, please run 'make build' first. You might need to install Rust first"
    exit 1
fi
