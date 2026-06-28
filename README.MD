# kader

## why did you name it kader ?
 caz why not :) it's way more like `john`
## what is kader ?

**Kader** is a Python-based CPU password hash auditing tool designed for educational purposes and authorized security testing. It supports multiple hashing algorithms and performs high-speed dictionary-based hash verification using only the CPU.


## Features

- Fast CPU-based hash verification
- Supports multiple hash algorithms (MD5, SHA-1, SHA-2, SHA-3, BLAKE2, and more) -- i'll add more in the future

- Dictionary-based password testing

- Written entirely in Python

- Optimized for high performance

## Performance

On supported hardware, `Kader` can process **up to ~10.3 million hash comparisons per second** during benchmark tests. Actual performance depends on:

- CPU model
- Number of CPU cores
- Selected hash algorithm
- Wordlist size and storage speed

## Requirements

- Python 3.10+ (crucial)
- computer (optional)


---
# HOW TO USE IT 

- First set up your wordlist you can just install ready one from [this_lien](https://github.com/kkrypt0nn/wordlists/tree/main/wordlists/passwords)
- second run the python code to test it 

   ```bash 
   python3 kader.py 
   ```

- now install it directly 

  ```bash 
     git clone https://github.com/Mohamedboukerche22/kader.git && cd kader && chmod +x install.sh && ./install.sh 
  ```

## example 
```bash
[mohamed@archlinux kader]$ python3 kader.py
=============================================
         KADER HASH CRACKER
=============================================

Enter the hash: 14ee22eaba297944c96afdbe5b16c65b

Available algorithms:

1. md5
2. sha1
3. sha224
4. sha256
5. sha384
6. sha512
7. sha3_224
8. sha3_256
9. sha3_384
10. sha3_512
11. blake2b
12. blake2s

Pick an algorithm: 1

Starting attack...

Cracking |████████████████████████████████████████| 100001/100001 [100%] in 2.7s (37391.14/s)

[+] Password found: 100000
[mohamed@archlinux kader]$ ls
install.sh  kader.py  LICENSE  README.MD  wordlist.txt

```



-  and voila 
