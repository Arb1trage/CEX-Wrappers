import logging
import random
import argparse
from time import sleep
from binance.spot import Spot as Client
from binance.lib.utils import config_logging
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
wallets = []

config_logging(logging, logging.DEBUG)

api_key = config["keys"]["api_key"]
api_secret = config["keys"]["api_secret"]

try:
    min_delay = int(config["options"]["min_delay"])
    max_delay = int(config["options"]["max_delay"])
    delay_exists = True
except:
    delay_exists = False

def main():
    spot_client = Client(api_key, api_secret, show_header=True)

    with open("wallets.txt", "r") as f:
        for line in f:
            if "#" not in line and len(line.strip()) > 5:
                wallets.append(line.split()[-4:])

    print("STARTING WITHDRAWALS...", end="\n\n")
    for index, wallet in enumerate(wallets):
        if delay_exists is True:
            logging.info(spot_client.withdraw(address=wallet[0], amount=float(wallet[1]), coin=wallet[2], network=wallet[3]))
            print()
            if index == len(wallets)-1:
                pass
            else:
                sleep(random.randint(min_delay, max_delay))
        else:
            logging.info(spot_client.withdraw(address=wallet[0], amount=float(wallet[1]), coin=wallet[2], network=wallet[3]))
            print()
            if index == len(wallets)-1:
                pass
            else:
                sleep(2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Script that automates asset withdrawals using the API. '
        'Supports withdrawal to multiple wallet addresses, custom asset amounts and randomized delay between withdrawals.')
    parser.add_argument('-V, --version',
                        action='version',
                        version='Binance Withdrawer by Arb1trage - Version 1.0')
    args = parser.parse_args()
    main()
