#!/bin/sh

uname=`uname`
if [ ${uname} = 'Linux' ]; then
    uname=`cat /etc/os-release | grep '^NAME' | sed 's/^NAME="//' | sed 's/"$//'`
fi
echo -n ${uname}
