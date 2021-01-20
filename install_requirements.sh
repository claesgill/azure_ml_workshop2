#!/bin/bash

GREEN="\e[32m"
YELLOW="\e[33m"
RED="\e[91m"
NORMAL="\e[0m"
SUCCSESS="$GREEN Success! $NORMAL"
FAIL="$RED Failed ... $NORMAL"

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
    sudo apt-get install azure-cli && echo -e $SUCCSESS || echo -e $FAIL
    echo -e "$GREEN Done installing Azure CLI! $NORMAL"
fi

# Install pip3
echo -e "$YELLOW Installing pip3 $NORMAL"
sudo apt install python3-pip && echo -e $SUCCSESS || echo -e $FAIL

# Install Python requirements
echo -e "$YELLOW Installing Python requirements $NORMAL"
#pip3 install -r requirements.txt && echo -e $SUCCSESS || echo -e $FAIL
pip3 install azureml-core && echo -e $SUCCSESS || echo -e $FAIL
pip3 install azureml-dataprep && echo -e $SUCCSESS || echo -e $FAIL
# pip3 install azureml-train
pip3 install azureml-train-core && echo -e $SUCCSESS || echo -e $FAIL
pip3 install pandas && echo -e $SUCCSESS || echo -e $FAIL
pip3 install torch && echo -e $SUCCSESS || echo -e $FAIL
pip3 install torchvision && echo -e $SUCCSESS || echo -e $FAIL
pip3 install tqdm && echo -e $SUCCSESS || echo -e $FAIL
pip3 install Unidecode && echo -e $SUCCSESS || echo -e $FAIL

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
