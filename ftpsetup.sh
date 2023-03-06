#!/bin/bash

echo "Starting PureFTP setup"
echo "Adding group and user..."
sudo groupadd ftpgroup
sudo useradd -g ftpgroup -d /dev/null -s /etc ftpuser

echo "Adding PureFTP user..."
sudo pure-pw useradd offsec -u ftpuser -d /ftphome
sudo pure-pw mkdb

echo "Creating DB Link..."
cd /etc/pure-ftpd/auth/
sudo ln -s ../conf/PureDB 60pdb

echo "Making FTP dir..."
sudo mkdir -p /ftphome
sudo chown -R ftpuser:ftpgroup /ftphome/

echo "Restarting PureFTP..."
sudo systemctl restart pure-ftpd

echo "Done!"