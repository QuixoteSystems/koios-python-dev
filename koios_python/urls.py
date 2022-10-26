#!/usr/bin/env python
"""
Provides all urls used in the library
"""

class URLs:
    # imported like class methods
    from .epoch import get_epoch_info, get_epoch_params
    from .network import get_tip, get_genesis, get_totals
    from .block import get_blocks, get_block_info, get_block_txs
    from .address import get_address_info, get_address_txs, get_address_assets, get_credential_txs
    from .account import get_account_info, get_account_list, get_account_rewards, get_account_updates, get_account_addresses, get_account_assets, get_account_history
    from .asset import get_asset_list, get_asset_address_list, get_asset_info, get_asset_history, get_asset_policy_info, get_asset_summary, get_asset_txs
    from .pool import get_pool_list, get_pool_info, get_pool_stake_snapshot, get_pool_delegators, get_pool_delegators_history, get_pool_blocks, get_pool_history, get_pool_updates, get_pool_relays, get_pool_metadata
    from .scripts import get_native_script_list, get_plutus_script_list, get_script_redeemers
    from .transactions import get_tx_info, get_tx_utxos, get_tx_metadata, get_tx_metalabels, submit_tx, get_tx_status
 
    
    def __init__(self, url='https://api.koios.rest/api/v0/', network='mainnet'):
        self.url = url
        self.network = network
        
        # change subdomain to network name 
        if self.network != 'mainnet':
            # replace any subdomain with "network" subdomain
            self.url = self.url.replace(self.url.split('.')[0], self.network)
        
        # Network URLs
        self.TIP_URL = url + "tip"
        self.GENESIS_URL = url + "genesis"
        self.TOTALS_URL = url + "totals"
        # Epoch URLs
        self.EPOCH_INFO_URL = url + "epoch_info"
        self.EPOCH_PARAMS_URL = url + "epoch_params"
        # Block URLs
        self.BLOCKS_URL = url + "blocks"
        self.BLOCK_INFO_URL = url + "block_info"
        self.BLOCK_TXS_URL = url + "block_txs"
        # Transaction URLs
        self.TX_INFO_URL = url + "tx_info"
        self.TX_UTXOS_URL = url + "tx_utxos"
        self.TX_METADATA_URL = url + "tx_metadata"
        self.TX_METALABELS_URL = url + "tx_metalabels"
        self.SUBMIT_TX_URL = url + "submittx"
        self.TX_STATUS_URL = url + "tx_status"
        # Address URLs
        self.ADDRESS_INFO_URL = url + "address_info"
        self.ADDRESS_TXS_URL = url + "address_txs"
        self.ADDRESS_ASSETS_URL = url + "address_assets"
        self.CREDENTIAL_TXS_URL = url + "credential_txs"
        # Account URLs
        self.ACCOUNT_LIST_URL = url + "account_list"
        self.ACCOUNT_INFO_URL = url + "account_info"
        self.ACCOUNT_REWARDS_URL = url + "account_rewards"
        self.ACCOUNT_UPDATES_URL = url + "account_updates"
        self.ACCOUNT_ADDRESSES_URL = url + "account_addresses"
        self.ACCOUNT_ASSETS_URL = url + "account_assets"
        self.ACCOUNT_HISTORY_URL = url + "account_history"
        # Asset URLs
        self.ASSET_LIST_URL = url + "asset_list"
        self.ASSET_ADDRESS_LIST_URL = url +  "asset_address_list?_asset_policy="
        self.ASSET_INFO_URL = url + "asset_info?_asset_policy="
        self.ASSET_HISTORY_URL = url + "asset_history?_asset_policy="
        self.ASSET_POLICY_INFO_URL = url + "asset_policy_info?_asset_policy="
        self.ASSET_SUMMARY_URL = url + "asset_summary?_asset_policy="
        self.ASSET_TXS_URL = url + "asset_txs?_asset_policy="
        # Pool URLs
        self.POOL_LIST_URL = url + "pool_list"
        self.POOL_INFO_URL = url + "pool_info"
        self.POOL_STAKE_SNAPSHOT = url + "pool_stake_snapshot?_pool_bech32="
        self.POOL_DELEGATORS_URL = url + "pool_delegators?_pool_bech32="
        self.POOL_DELEGATORS_HISTORY_URL = url + "pool_delegators_history?_pool_bech32="
        self.POOL_BLOCKS_URL = url + "pool_blocks?_pool_bech32="
        self.POOL_HISTORY_URL = url + "pool_history?_pool_bech32="
        self.POOL_UPDATES_URL = url + "pool_updates"
        self.POOL_RELAYS_URL = url + "pool_relays"
        self.POOL_METADATA_URL = url + "pool_metadata"

        # Scripts URLs
        self.NATIVE_SCRIPT_LIST_URL = url + "native_script_list"
        self.PLUTUS_SCRIPT_LIST_URL = url + "plutus_script_list"
        self.SCRIPT_REDEEMERS_URL = url + "script_redeemers?_script_hash="
