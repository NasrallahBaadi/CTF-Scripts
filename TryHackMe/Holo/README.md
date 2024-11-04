# TryHackMe Holo Network

## Initial Foothold

`holo.py` is a script that makes it easy to get the initial foothold on Holo.

### Usage

```bash
python3 holo.py -i 10.200.144.33 -u admin -p password
```

The script logs in to the admin dashboard on `admin.holo.live` and uses the `cmd` web shell to get a reverse shell.
