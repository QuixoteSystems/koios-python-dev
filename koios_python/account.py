#!/usr/bin/env python

import json
import requests


def get_account_list():
    """
    Get a list of all accounts.

    return: string list of account (stake address: stake1...  bech32 format) IDs
    """
    address_list = requests.get("https://api.koios.rest/api/v0/account_list")
    address_list = json.loads(address_list.content)
    return address_list


def get_account_info(address):
    """
    Get the account info of any (payment or staking) address.

    param: staking address in bech32 format (stake1...)
    return: list with all address data.
    """
    info = requests.get("https://api.koios.rest/api/v0/account_info?_address="+str(address))
    info = json.loads(info.content)
    return info


def get_account_rewards(address, epoch=None):
    """
    Get the full rewards history (including MIR) for a stake address, or certain epoch if specified.

    param: Cardano staking address (reward account) in bech32 format (stake1...)
    param: epoch (optional)
    return: list with all account rewards.
    """
    if epoch is None:
        info = requests.get("https://api.koios.rest/api/v0/account_rewards?_stake_address=" \
            +str(address))
        info = json.loads(info.content)
    else:
        info = requests.get("https://api.koios.rest/api/v0/account_rewards?_stake_address=" \
            +str(address)+"&_epoch_no="+str(epoch))
        info = json.loads(info.content)
    return info


def get_account_updates(address):
    """
    Get the account updates (registration, deregistration, delegation and withdrawals).

    param: staking address in bech32 format (stake1...)
    return: list with all account updates.
    """
    info = requests.get("https://api.koios.rest/api/v0/account_updates?_stake_address="+str(address))
    info = json.loads(info.content)
    return info


def get_account_addresses(address):
    """
    Get all addresses associated with an account.

    param: staking address in bech32 format (stake1...)
    return: list with all account addresses.
    """
    info = requests.get("https://api.koios.rest/api/v0/account_addresses?_address="+str(address))
    info = json.loads(info.content)
    return info


def get_account_assets(address):
    """
    Get the native asset balance of an account.

    param: staking address in bech32 format (stake1...)
    return: list with all account assets.
    """
    info = requests.get("https://api.koios.rest/api/v0/account_assets?_address="+str(address))
    info = json.loads(info.content)
    return info


def get_account_history(address):
    """
    Get the staking history of an account.

    param: staking address in bech32 format (stake1...)
    return: list with all account history.
    """
    info = requests.get("https://api.koios.rest/api/v0/account_history?_address="+str(address))
    info = json.loads(info.content)
    return info