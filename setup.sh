#!/bin/bash

# Install necessary packages
sudo apt-get install -y wget apt-transport-https gnupg lsb-release

# Add Trivy's official GPG key
wget -qO - https://aquasecurity.github.io/trivy-repo/deb/public.key | gpg --dearmor | sudo tee /usr/share/keyrings/trivy.gpg > /dev/null

# Add the Trivy repository to APT sources
echo deb [signed-by=/usr/share/keyrings/trivy.gpg] https://aquasecurity.github.io/trivy-repo/deb $(lsb_release -sc) main | sudo tee /etc/apt/sources.list.d/trivy.list

# Update the package list
sudo apt-get update

# Install Trivy
sudo apt-get install -y trivy
