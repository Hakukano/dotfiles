#!/bin/bash

if [[ ! `command -v python3` ]]; then
  echo 'Please install python3 before run this script!'
  exit 1
fi

if [[ ! `command -v pip3` ]]; then
  echo 'Please install pip3 before run this script!'
  exit 1
fi

un=`uname`
os='unknown'
case "$un" in
  'Linux')
    os=`awk -F= '/^ID=/{print $2}' /etc/os-release`
    ;;
  'Darwin')
    os='macos'
    ;;
  *)
    echo 'Unsupported Unix:' ${un}
    ;;
esac

case "${os}" in
  'arch')
    pushd ./setup-arch
    pip install -r requirements.txt
    python setup.py
    popd
    ;;
  'debian')
    pushd ./setup-debian
    pip install -r requirements.txt
    python setup.py
    popd
    ;;
  'pop')
    pushd ./setup-pop
    pip install -r requirements.txt
    python setup.py
    popd
    ;;
  'macos')
    pushd ./setup-macos
    pip install -r requirements.txt
    python setup.py
    popd
    ;;
  *)
    echo 'Unsupported OS:' ${os}
    ;;
esac

