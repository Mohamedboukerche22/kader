#!/usr/bin/env python3

import hashlib
# github acc = mohamedboukerche22
# tool name = kader
WORDLIST = "./wordlist.txt"
# create a Password list first or downloads ready one
# or you can steel one from john's the ripper


# some hashing algorithms i'll add more dw soon
ALGORITHMS = [
    "md5",
    "sha1",
    "sha224",
    "sha256",
    "sha384",
    "sha512",
    "sha3_224",
    "sha3_256",
    "sha3_384",
    "sha3_512",
    "blake2b",
    "blake2s"
]

def select_algorithm():
    for i, algo in enumerate(ALGORITHMS, start=1):
        print(f"{i}. {algo}")

    while True:
        try:
            choice = int(input("\npick an algorithm: "))
            if 1 <= choice <= len(ALGORITHMS):
                return ALGORITHMS[choice - 1]
        except ValueError:
            pass

        print("Invalid choice.")

def crack_hash(target_hash, algorithm, wordlist):
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        for line in f:
            word = line.strip()

            digest = hashlib.new(
                algorithm,
                word.encode("utf-8")
            ).hexdigest()

            if digest.lower()==target_hash.lower():
                return word

    return None


target = input("Enter the hash: ").strip()
algorithm = select_algorithm()

result = crack_hash(target, algorithm, WORDLIST)

if result:
    print(f"\n[+] Password found: {result}")
else:
    print("\n[-] Password not found in wordlist.")