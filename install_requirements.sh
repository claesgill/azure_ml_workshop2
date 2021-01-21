#!/bin/bash

# Declaring helper variables
GREEN="\e[32m"
YELLOW="\e[33m"
RED="\e[91m"
NORMAL="\e[0m"
SUCCSESS="$GREEN Success! $NORMAL"
FAIL="$RED Failed ... $NORMAL"

# Install Gnome desktop
echo -e "$YELLOW Installing Gnome desktop! $NORMAL"
sudo apt-get -y update
sudo apt-get -y upgrade
sudo apt-get -y -q=2  install ubuntu-gnome-desktop gnome-tweaks gnome-shell-extensions
sudo apt-get -y -q=2  install xrdp
sudo adduser xrdp ssl-cert
sudo apt-get -y -q=2  install ca-certificates curl apt-transport-https lsb-release gnupg

echo -e "$YELLOW Trying to install Azure CLI! $NORMAL"
if command -v az > /dev/null 2>&1; then
  echo -e "$GREEN az CLI exists! Skipping installation. $NORMAL"
else
    echo -e "$YELLOW Installing Azure CLI $NORMAL"
    sudo apt-get update
    sudo apt-get install ca-certificates curl apt-transport-https lsb-release gnupg
    curl -sL https://packages.microsoft.com/keys/microsoft.asc |
        gpg --dearmor |
        sudo tee /etc/apt/trusted.gpg.d/microsoft.gpg > /dev/null
    AZ_REPO=$(lsb_release -cs)
    echo "deb [arch=amd64] https://packages.microsoft.com/repos/azure-cli/ $AZ_REPO main" |
        sudo tee /etc/apt/sources.list.d/azure-cli.list
    sudo apt-get update
    sudo apt-get -y install azure-cli && echo -e $SUCCSESS || echo -e $FAIL
    echo -e "$GREEN Done installing Azure CLI! $NORMAL"
fi

# Install pip3
echo -e "$YELLOW Installing pip3 $NORMAL"
sudo apt -y install python3-pip && echo -e $SUCCSESS || echo -e $FAIL

# Clean .locals folder: https://stackoverflow.com/a/55309683
echo -e "$YELLOW Cleaning '.locals' folder $NORMAL"
rm -rf ~/.local

# Install Python requirements
echo -e "$YELLOW Installing Python requirements $NORMAL"

#pip3 install -r requirements.txt && echo -e $SUCCSESS || echo -e $FAIL
echo -e "$YELLOW pip3 install azureml-core $NORMAL"
pip3 install azureml-core > /dev/null && echo -e $SUCCSESS || echo -e $FAIL
echo -e "$YELLOW Cleaning '.locals' folder $NORMAL"
rm -rf ~/.local

echo -e "$YELLOW pip3 install azureml-dataprep $NORMAL"
pip3 install azureml-dataprep > /dev/null && echo -e $SUCCSESS || echo -e $FAIL
echo -e "$YELLOW Cleaning '.locals' folder $NORMAL"
rm -rf ~/.local

# pip3 install azureml-train
echo -e "$YELLOW pip3 install azureml-train-core $NORMAL"
pip3 install azureml-train-core > /dev/null && echo -e $SUCCSESS || echo -e $FAIL
echo -e "$YELLOW Cleaning '.locals' folder $NORMAL"
rm -rf ~/.local

echo -e "$YELLOW pip3 install pandas $NORMAL"
pip3 install pandas > /dev/null && echo -e $SUCCSESS || echo -e $FAIL
echo -e "$YELLOW Cleaning '.locals' folder $NORMAL"
rm -rf ~/.local

echo -e "$YELLOW pip3 install torch $NORMAL"
pip3 install torch > /dev/null && echo -e $SUCCSESS || echo -e $FAIL
echo -e "$YELLOW Cleaning '.locals' folder $NORMAL"
rm -rf ~/.local

echo -e "$YELLOW pip3 install torchvision $NORMAL"
pip3 install torchvision > /dev/null && echo -e $SUCCSESS || echo -e $FAIL
echo -e "$YELLOW Cleaning '.locals' folder $NORMAL"
rm -rf ~/.local

echo -e "$YELLOW pip3 install tqdm $NORMAL"
pip3 install tqdm > /dev/null && echo -e $SUCCSESS || echo -e $FAIL
echo -e "$YELLOW Cleaning '.locals' folder $NORMAL"
rm -rf ~/.local

echo -e "$YELLOW pip3 install Unidecode $NORMAL"
pip3 install Unidecode > /dev/null && echo -e $SUCCSESS || echo -e $FAIL
echo -e "$YELLOW Cleaning '.locals' folder $NORMAL"
rm -rf ~/.local

echo -e "$YELLOW Trying to install VS Code $NORMAL"
if command -v code > /dev/null 2>&1; then
  echo -e "$GREEN VS Code exists! Skipping installation. $NORMAL"
else
  sudo snap install --classic code && echo -e $SUCCSESS || echo -e $FAIL
fi

# Install VS Code extentions
#code --install-extension ms-python.python
#code --install-extension ms-toolsai.jupyter
#code --install-extension liviuschera.noctis

echo -e "$GREEN Install complete! $NORMAL"
