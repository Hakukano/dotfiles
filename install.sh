#!/bin/sh

uname=`uname`

executable_name=wizard

executable=./bin/${executable_name}-${uname}
if [ -f ${executable} ]; then
    ${executable}
else
    echo "Unsupported distro ${uname}, please run 'make build' first. You might need to install Rust first"
    exit 1
fi
