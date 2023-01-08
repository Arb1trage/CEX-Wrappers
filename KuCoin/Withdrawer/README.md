## Usage
```
usage: kucoin_withdrawer.py [-h] [-V, --version]

options:
  -h, --help            show the help message and exit
  
  -V, --version         show program's version number and exit
```
Make sure to adjust the values in "config.ini" and "wallets.txt".

## KuCoin API Keys
You can generate API keys for your account under "https://www.kucoin.com/account/api". Enable "Withdrawal" permissions during the generation and **DO NOT SHARE THEM WITH ANYONE**.


## Installation
Install dependencies listed in requirements.txt:
```sh
python3 -m pip install -r requirements.txt
```
then execute like any other .py script:
```sh
chmod +x kucoin_withdrawer.py
./kucoin_withdrawer.py [OPTIONS]
```
NOTE: Tool was programmed to use with Python 3.10, but should work with any Python 3.6+ version.
