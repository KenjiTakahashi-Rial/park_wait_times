#!/bin/bash

set -e

sudo apt-get update
sudo apt install -y \
    make \
    build-essential \
    libssl-dev zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget curl llvm \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev \
    pip

# Pyenv setup
PYENV_ROOT="$HOME/.pyenv"
PYENV_VIRUALENV_DIR="$PYENV_ROOT/plugins/pyenv-virtualenv"

if [ ! -d $PYENV_ROOT ]; then
    git clone https://github.com/pyenv/pyenv.git $PYENV_ROOT
else
    cd $PYENV_ROOT
    git pull
    cd -
fi

if [ ! -d $PYENV_VIRTUALENV_DIR ]; then
    git clone https://github.com/pyenv/pyenv-virtualenv.git $PYENV_VIRTUALENV_DIR
fi

echo "export PYENV_ROOT=\"$PYENV_ROOT\"" >> ~/.bashrc
echo "export PATH=\"$PYENV_ROOT/bin:\$HOME/.local/bin:\$PATH"" >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n eval "$(pyenv init --path)"\nfi' >> ~/.bashrc
exec $SHELL

dir="$(cd "$(dirname "$0")" && pwd)"
$dir/inflate.sh
