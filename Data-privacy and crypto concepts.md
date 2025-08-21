# Data-privacy

+----------------------+
|    Cryptography      |
+----------------------+
           |
   +-------+-------+
   |               |
+------------------------+         +----------------------------+
| Symmetric Cryptography |         | Asymmetric Cryptography   |
+------------------------+         +----------------------------+
   | Shared Secret Key              | Key Pair (Public/Private)
   |                                |
+--------------------------+       +-----------------------------+
| AES, TLS, etc.           |       | RSA, ECC, ECDSA             |
| - Confidentiality        |       | - Signatures                |
| - Fast, Efficient        |       | - Key Exchange              |
+--------------------------+       +-----------------------------+
   |                                |
+--------------------------+       +-----------------------------+
| Confidentiality          |       | Digital Signatures          |
| - AES in TLS             |       | - ECDSA (e.g., Bitcoin)     |
| - End-to-End Messaging   |       | - RSA                       |
+--------------------------+       +-----------------------------+
                                        |
                       +----------------+----------------+
                       |                                 |
          +----------------------------+    +-----------------------------+
          | PKI / x.509 Certificates   |    | Threshold Signatures        |
          | - HTTPS, SSL/TLS           |    | - Multisig, Custody wallets |
          | - Certificate Authorities  |    +-----------------------------+
          +----------------------------+
                       |
       +------------------------------------------+
       | Verifiable Credentials & DIDs            |
       +------------------------------------------+
                       |
    +----------------------------------------------+
    | Self-Sovereign Identity (SSI), Identity Mixer|
    +----------------------------------------------+
                       |
        +-----------------------------+
        |  Privacy Enhancing Techs   |
        +-----------------------------+
                       |
        +-----------------------------+
        |       Anonymity            |
        +-----------------------------+
        | - Ring Signatures (Monero) |
        | - zk-SNARKs (Zcash)        |
        | - Blind Signatures         |
        | - Mixers / Tumblers        |
        | - CoinJoin / CoinShuffle   |
        | - Stealth Addresses        |
        | - Dandelion Protocol       |
        | - Pseudonymity             |
        +-----------------------------+



<img width="3840" height="344" alt="Untitled diagram _ Mermaid Chart-2025-08-21-152552" src="https://github.com/user-attachments/assets/d5e7cb21-3b32-473f-8474-5fb23adc8797" />


## **ANONYMITY :**

| Technique           | Description                                                                          |
| ------------------- | ------------------------------------------------------------------------------------ |
| **Interactive**     | Requires real-time communication (e.g., mixers, MPC, CoinJoin).                      |
| **Non-Interactive** | One-shot or stand-alone cryptographic techniques (e.g., zk-SNARKs, Ring Signatures). |


<img width="3840" height="212" alt="Untitled diagram _ Mermaid Chart-2025-08-21-154221" src="https://github.com/user-attachments/assets/904b9123-ec69-426d-8637-dec081f521d9" />

## Another way to achieve annonymity is to check at different levels :

| Category                        | Included Topics                                                     |
| ------------------------------- | ------------------------------------------------------------------- |
| **Network-Level Anonymity**     | Tor, Dandelion                                                      |
| **Transaction-Level Anonymity** | CoinJoin, CoinShuffle, Mixers, Stealth Addresses, CT, RingCT, Zcash |
| **Signature Schemes**           | Ring Signatures, Group Signatures, Blind Signatures                 |
| **Privacy-Preserving Identity** | Pseudonymity, Idemix, ZKPs                                          |
| **PETs (General)**              | ZKPs, Anonymous Credentials, HE                                     |

<img width="3840" height="320" alt="Untitled diagram _ Mermaid Chart-2025-08-21-152948" src="https://github.com/user-attachments/assets/f79537b8-8961-40f6-85ec-36ec42c0f12d" />

