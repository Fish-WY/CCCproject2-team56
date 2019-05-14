#!/bin/bash

sudo apt-get -y remove docker docker-engine docker.io docker-ce docker-ce-cli containerd.io runc
sudo rm -rf /var/lib/docker

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get -y update
sudo apt-get -y install docker-ce docker-ce-cli containerd.io

