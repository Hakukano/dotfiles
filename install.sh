#!/bin/sh

if [[ ! `command -v python3` ]]; then
  echo 'Please install python 3 before run this script!'
  exit 1
fi

os=`awk -F= '/^ID/{print $2}' /etc/os-release`

case "${os}" in
  'arch')
    pushd ./setup-arch
    pip install -r requirements.txt
    python setup.py
    popd
    ;;
  *)
    echo 'Unsupported OS:' ${os}
    ;;
esac

