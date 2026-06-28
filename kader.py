#!/usr/bin/env python3

import hashlib
from alive_progress import alive_bar

# GitHub: mohamedboukerche22
# Tool name: kader

WORDLIST = "./wordlist.txt"

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
    print("\nAvailable algorithms:\n")

    for i, algo in enumerate(ALGORITHMS, start=1):
        print(f"{i}. {algo}")

    while True:
        try:
            choice = int(input("\nPick an algorithm: "))
            if 1 <= choice <= len(ALGORITHMS):
                return ALGORITHMS[choice - 1]
        except ValueError:
            pass

        print("Invalid choice.")


def crack_hash(target_hash, algorithm, wordlist):
    # Count total passwords
    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        total = sum(1 for _ in f)

    with open(wordlist, "r", encoding="utf-8", errors="ignore") as f:
        with alive_bar(
            total,
            title="Cracking",
            enrich_print=False,
            force_tty=True
        ) as bar:

            for line in f:
                word = line.strip()

                digest = hashlib.new(
                    algorithm,
                    word.encode("utf-8")
                ).hexdigest()

                # Show current word
                bar.text(f"Testing: {word}")

                if digest.lower() == target_hash.lower():
                    bar()
                    return word

                bar()

    return None


def main():
    print("=" * 45)
    print("         KADER HASH CRACKER")
    print("=" * 45)

    target = input("\nEnter the hash: ").strip()
    algorithm = select_algorithm()

    print("\nStarting attack...\n")

    result = crack_hash(target, algorithm, WORDLIST)

    print()

    if result:
        print(f"[+] Password found: {result}")
    else:
        print("[-] Password not found in the wordlist.")


if __name__ == "__main__":
    main()
