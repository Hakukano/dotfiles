#!/bin/sh

uname=`uname`
if [ ${uname} = 'Linux' ]; then
    uname=`cat /etc/os-release | grep '^ID' | sed 's/^ID=//'`
fi
printf '%s' "${uname}"
