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

pushd ./install
pip install -r requirements.txt
python install.py "${os}"
popd

