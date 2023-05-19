# Installation

```
sudo apt install libnss3-tools
curl -JLO "https://dl.filippo.io/mkcert/latest?for=linux/amd64"
chmod +x mkcert-v*-linux-amd64
ln -s mkcert-v*-linux-amd64 mkcert

# Run on the machine to trust the cert

./mkcert -install
# Creates the CA and installs it in the trust chain

./mkcert vault 192.168.1.2 papa localhost 127.0.0.1
# Creates vault+4-key.pem and vault+4.pem


ln -s vault+4.pem vault.crt
ln -s vault+4-key.pem vault.key

```
