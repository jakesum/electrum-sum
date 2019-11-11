# -*- coding: utf-8 -*-
#
# Electrum - lightweight Bitcoin client
# Copyright (C) 2018 The Electrum developers
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation files
# (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge,
# publish, distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to do so,
# subject to the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import os
import json

from .util import inv_dict


def read_json(filename, default):
    path = os.path.join(os.path.dirname(__file__), filename)
    try:
        with open(path, 'r') as f:
            r = json.loads(f.read())
    except:
        r = default
    return r


GIT_REPO_URL = "https://github.com/Tech1k/electrum-sum"
GIT_REPO_ISSUES_URL = "https://github.com/Tech1k/electrum-sum/issues"


class AbstractNet:

    @classmethod
    def max_checkpoint(cls) -> int:
        return max(0, len(cls.CHECKPOINTS) * 2880 - 1) # Sumcoin deedle difficulty measure


class BitcoinMainnet(AbstractNet):

    TESTNET = False
    WIF_PREFIX = 0xBF # Sumcoin TODO: verify WIF prefix
    ADDRTYPE_P2PKH = 63 # 63 is Verified Sumcoin Value  - TODO: verify P2PKH prefix
    ADDRTYPE_P2SH = 200 # 200 is Verified Sumcoin Value - TODO: verify P2SH prefix
    SEGWIT_HRP = "sum"
    GENESIS = "37d4696c5072cd012f3b7c651e5ce56a1383577e4edacc2d289ec9b25eebfd5e" # Sumcoin TODO: verify mainnet genesis
    DEFAULT_PORTS = {'t': '53332', 's': '53333'}
    DEFAULT_SERVERS = read_json('servers.json', {})
    CHECKPOINTS = read_json('checkpoints.json', [])

    XPRV_HEADERS = {
        'standard':    0x0488b41c,  # xprv  ## Sumcoin TODO: verify xprv header
        'p2wpkh-p2sh': 0x049d7878,  # yprv
        'p2wsh-p2sh':  0x0295b005,  # Yprv
        'p2wpkh':      0x04b2430c,  # zprv
        'p2wsh':       0x02aa7a99,  # Zprv
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard':    0x0488abe6,  # xpub  ## Sumcoin TODO: verify xpub header
        'p2wpkh-p2sh': 0x049d7cb2,  # ypub
        'p2wsh-p2sh':  0x0295b43f,  # Ypub
        'p2wpkh':      0x04b24746,  # zpub
        'p2wsh':       0x02aa7ed3,  # Zpub
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BIP44_COIN_TYPE = 2


class BitcoinTestnet(AbstractNet):

    TESTNET = True
    WIF_PREFIX = 0xbf # Sumcoin TODO: verify WIF prefix
    ADDRTYPE_P2PKH = 125 # Sumcoin TODO: verify P2PKH prefix
    ADDRTYPE_P2SH = 8 # Sumcoin TODO: verify P2SH prefix
    SEGWIT_HRP = "tsum"
    GENESIS = "8f4af36aa0bdb9ae5a34d191bcbd80748569e4ef2e47587f0a3f5749dde17eea" # Sumcoin TODO: verify testnet genesis
    DEFAULT_PORTS = {'t': '54332', 's': '54333'}
    DEFAULT_SERVERS = read_json('servers_testnet.json', {})
    CHECKPOINTS = read_json('checkpoints_testnet.json', [])

    XPRV_HEADERS = {
        'standard':    0x063289cc,  # tprv  ## Sumcoin TODO: verify tprv header
        'p2wpkh-p2sh': 0x044a4e28,  # uprv
        'p2wsh-p2sh':  0x024285b5,  # Uprv
        'p2wpkh':      0x045f18bc,  # vprv
        'p2wsh':       0x02575048,  # Vprv
    }
    XPRV_HEADERS_INV = inv_dict(XPRV_HEADERS)
    XPUB_HEADERS = {
        'standard':    0x01378096,  # tpub  ## Sumcoin TODO: verify tpub header
        'p2wpkh-p2sh': 0x044a5262,  # upub
        'p2wsh-p2sh':  0x024289ef,  # Upub
        'p2wpkh':      0x045f1cf6,  # vpub
        'p2wsh':       0x02575483,  # Vpub
    }
    XPUB_HEADERS_INV = inv_dict(XPUB_HEADERS)
    BIP44_COIN_TYPE = 1


class BitcoinRegtest(BitcoinTestnet):

    SEGWIT_HRP = "rsum"
    GENESIS = "19decb2815da5a7779c72af78fe6268c2a76ec94e940503a6c3ffafb282ef397" # Sumcoin TODO: verify regtest genesis
    DEFAULT_SERVERS = read_json('servers_regtest.json', {})
    CHECKPOINTS = []


class BitcoinSimnet(BitcoinTestnet):

    SEGWIT_HRP = "ss"
    GENESIS = "19decb2815da5a7779c72af78fe6268c2a76ec94e940503a6c3ffafb282ef397"
    DEFAULT_SERVERS = read_json('servers_regtest.json', {})
    CHECKPOINTS = []


# don't import net directly, import the module instead (so that net is singleton)
net = BitcoinMainnet

def set_simnet():
    global net
    net = BitcoinSimnet

def set_mainnet():
    global net
    net = BitcoinMainnet


def set_testnet():
    global net
    net = BitcoinTestnet


def set_regtest():
    global net
    net = BitcoinRegtest
