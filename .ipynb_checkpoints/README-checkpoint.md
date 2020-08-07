# Multi-Blockchain Wallet in Python

## Description

In this project we create an HD-Wallet (universal crypto wallet).
* We use `hd-wallet-derive` that supports BIP32, BIP39, and BIP44 standards to create a  multi coin wallet from a specific mnemonic
* We use the universal wallet to create and execute transaction on our local testnet (for ethereum) using POA consensus and on bitcoin testnet

# INSTALLATION
---
### hd-wallet:

```
Windows users, use CMD, not git bash for the PHP step

git clone https://github.com/dan-da/hd-wallet-derive
cd hd-wallet-derive
php.exe -r "readfile('https://getcomposer.org/installer');" | php
php.exe -d pcre.jit=0 composer.phar install
```

 ```shell 
 git clone https://github.com/dan-da/hd-wallet-derive
 cd hd-wallet-derive
 php -r "readfile('https://getcomposer.org/installer');" | php
 php -d pcre.jit=0 composer.phar install
 ```

* You should now have a folder called `hd-wallet-derive` containing the PHP library.

## hd-wallet-derive Execution

Last step! Execute the `hd-wallet-derive` library to derive `BIP32` addresses and private keys for Bitcoin and other alternative coins.

* Navigate to your `hd-wallet-derive` folder.

* Then execute the following commands (these are examples from the GitHub website).

 ```shell
 ./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c
 ```

 ```shell
 ./hd-wallet-derive.php -g --key=xprv9tyUQV64JT5qs3RSTJkXCWKMyUgoQp7F3hA1xzG6ZGu6u6Q9VMNjGr67Lctvy5P8oyaYAL9CAWrUE9i6GoNMKUga5biW6Hx4tws2six3b9c --numderive=3 --preset=bitcoincore --cols=path,address --path-change
 ```


* The `hd-wallet-derive` library should now be working and good to go!


#### Enable Symbolic link

- PC Users will need to enable creation of symbolic links
- export MSYS=winsymlinks:nativestrict

Everyone, in admin mode, run
- ln -s hd-wallet-derive/hd-wallet-derive.php derive
```


# HD-WALLET
---

![bitcoinTransaction](Images/hdwallet.png)

# BITCOIN
---

> ### Code to execute bitcoin test

```bash
accountB = priv_key_to_account(BTCTEST, coins[BTCTEST][0]['privkey'])        
send_tx(BTCTEST, accountB, "mjMoK8zFxYaYmQNcG1eUTjtBKWUGAVMorq", 0.00002)
```

> ### bitcoin transaction screenshot from  [block explorer](https://tbtc.bitaps.com/)
---

![bitcoinTransaction](Images/bitcoinTransaction.png)

# ETHEREUM
---

> ## Code to execute ETH test
```bash
accountE = priv_key_to_account(ETH, coins[ETH][0]['privkey'])
send_tx(ETH, accountE, "0xc470b0A110C03636d5a6B8821aa34aED59E9f920", 1)
```
> ## ETH transaction screenshot from MyCrypto after connecting to local testnet and searching for the transaction hex from above execution

![ETHtransaction](Images/transactionSentETH.png)

> ## transaction hex
![ETHtransaction](Images/ETHtransaction.png)

---


