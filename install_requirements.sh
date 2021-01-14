#!/bin/bash

# Install Azure CLI
# TODO: Check if azure cli exists before installing
if command -v az > /dev/null 2>&1; then
  echo "az CLI exists! Skipping installation."
else
    echo "Installing Azure CLI"
    sudo apt-get update
    sudo apt-get install ca-certificates curl apt-transport-https lsb-release gnupg
    curl -sL https://packages.microsoft.com/keys/microsoft.asc |
        gpg --dearmor |
        sudo tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null
    AZ_REPO=$(lsb_release -cs)
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" |
        sudo tee /etc/apt/sources.list.d/azure-cli.list
    sudo apt-get update
    sudo apt-get install azure-cli
    echo "Done installing Azure CLI"
fi

# Install pip3
sudo apt-get install python3-pip

# Install Python requirements
pip3 install -r reqirements.txt

# Install VS Code
sudo snap install --classic code

# Install VS Code extentions
code --install-extension ms-python.python
code --install-extension ms-toolsai.jupyter
code --install-extension liviuschera.noctis

# Git clone repo
git clone https://github.com/claesgill/azure_ml_workshop2.git

# Install Terraform?
