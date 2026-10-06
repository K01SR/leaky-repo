#!/usr/bin/env python3
import argparse
import hashlib
import sys

EXPECTED_HASH = "77048a2f7cc07cda8eff15cb3bf0d0004d2aa313dd87b84d5cff19a931033f6b"
FLAG = "LTCOE{g1t_d4ngl1ng_c0mm1ts_4nd_d3c0ys_c4nt_h1d3}"

def main():
    parser = argparse.ArgumentParser(description="Internal Auth Verification Tool")
    parser.add_argument("--key", required=True, help="Developer master vault token")
    args = parser.parse_args()

    input_hash = hashlib.sha256(args.key.strip().encode()).hexdigest()
    if input_hash == EXPECTED_HASH:
        print("[+] Access Granted! Welcome normie69k.")
        print(f"[+] Master Secret Unlocked: {FLAG}")
    else:
        print("[-] Access Denied: Invalid master token signature.")
        if "LTCOE{" in args.key:
            print("[!] Troll alert: You submitted a decoy string! Keep digging.")
        sys.exit(1)

if __name__ == "__main__":
    main()
