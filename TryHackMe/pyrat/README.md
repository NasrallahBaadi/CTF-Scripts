# PyRAT brute force.

The script is written for the `pyrat` room on TryHackMe. 

It launches a brute force attack against a service to find the admin password which allows us to escalate our privileges to root.

## Usage

```bash
python3 pyrat_brute.py -i <target_ip> -f <path_to_wordlist>
```

## Arguments

    -i, --ip : IP address of the target machine.

    -f, --file : Path to the password wordlist file.

## Example

```bash
python3 pyrat_brute.py -i 10.10.10.10 -f /usr/share/wordlists/rockyou.txt
```

This example runs the script against the target at IP 10.10.10.10, using the rockyou.txt wordlist.