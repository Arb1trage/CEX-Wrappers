import random
import argparse
from time import sleep
from kucoin.client import User
from configparser import ConfigParser

config = ConfigParser()
config.read("config.ini")
wallets = []

api_key = config['keys']['API_KEY']
api_secret = config['keys']['API_SECRET']
api_passphrase = config['keys']['API_PASSPHRASE']

try:
    min_delay = int(config["options"]["min_delay"])
    max_delay = int(config["options"]["max_delay"])
    delay_exists = True
except:
    delay_exists = False

def main():
    client = User(api_key, api_secret, api_passphrase)

    with open("wallets.txt", "r") as f:
        for line in f:
            if "#" not in line and len(line.strip()) > 5:
                wallets.append(line.split()[-3:])

    print("STARTING WITHDRAWALS...", end="\n\n")
    for index, wallet in enumerate(wallets):
        # print(f"You are withdrawing {wallet[1]} {wallet[2]} to {wallet[0]}.", end=" ")
        # input("Press Enter to continue...")
        if delay_exists is True:
            client.apply_withdrawal(address=wallet[0], amount=float(wallet[1]), currency=wallet[2])
            if index == len(wallets)-1:
                pass
            else:
                sleep(random.randint(min_delay, max_delay))
        else:
            client.apply_withdrawal(address=wallet[0], amount=float(wallet[1]), currency=wallet[2])
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
                        version='KuCoin Withdrawer by Arb1trage - Version 1.0')
    args = parser.parse_args()
    main()