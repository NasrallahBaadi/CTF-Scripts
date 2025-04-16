# PwnTillDawn Silence

This script is written for the `Silence` machine aka `10.150.150.55` which loops through multiple private ssh keys until it find the correct one.

## Usage

To run the script cd to the private directory where the keys are then run the script with `bash id_loop.sh` or `chmod +x id_loop.sh & ./id_loop.sh`.

```terminal
┌──[10.66.66.230]─[sirius💀parrot]-[~/ctf/ptd/silence/private]
└──╼[★]$ bash ../id_loop.sh 
[*] Trying id_rsa1
[-] 'id_rsa1' Wrong Key', skipping
[*] Trying id_rsa10
[-] 'id_rsa10' Wrong Key', skipping
[...]
[*] Trying id_rsa[REDACTED]                  
[+] Success with id_rsa[REDACTED]
```
