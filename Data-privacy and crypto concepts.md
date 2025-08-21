# Data-privacy


### +=============================================================+
    |        **PUBLIC KEY INFRASTRUCTURE (PKI) - CENTRALIZED**      |
    +=============================================================+

    
<img width="2215" height="3840" alt="Untitled diagram _ Mermaid Chart-2025-08-21-173959" src="https://github.com/user-attachments/assets/c8c9beaa-b2e5-4fa5-a0ff-064b404e32b9" />




### +=============================================================+
     |  **DECENTRALIZED IDENTITY (DID + VERIFIABLE CREDENTIALS)**    |
    +=============================================================+
<img width="3001" height="3840" alt="Untitled diagram _ Mermaid Chart-2025-08-21-174951" src="https://github.com/user-attachments/assets/83f91598-68b2-45e5-b716-1d4bf03f1988" />



| Feature               | PKI / x.509       | DID + Verifiable Credentials       |
| --------------------- | ----------------- | ---------------------------------- |
| **Trust Model**       | Centralized (CAs) | Decentralized / User-Controlled    |
| **Identity Owner**    | Website (via CA)  | The individual (Holder)            |
| **Credential Format** | x.509 Certificate | Verifiable Credential (W3C)        |
| **Key Management**    | CA-controlled     | User-controlled DIDs               |
| **Privacy Features**  | Minimal           | Supports Selective Disclosure      |
| **Use Cases**         | HTTPS, Email, VPN | Identity, KYC, Credentials, Access |

### Real world example :

| PKI (x.509)                          | DID + Verifiable Credentials                              |
| ------------------------------------ | --------------------------------------------------------- |
| Driver’s license issued by DMV       | Digital ID card issued by your university                 |
| Passport issued by government        | Digital diploma in your mobile wallet                     |
| Trusted because of issuing authority | Trusted because of cryptographic proof (ZKPs, signatures) |

<img width="3840" height="2476" alt="Untitled diagram _ Mermaid Chart-2025-08-21-172630" src="https://github.com/user-attachments/assets/6121135b-40e5-4113-ac67-5b7d58440c72" />


| Category             | Core Algorithms / Technologies          | Related Topics                                          |
| -------------------- | --------------------------------------- | ------------------------------------------------------- |
| **Symmetric**        | AES, TLS, CT, RingCT, HE                | Forward Secrecy, Confidentiality, PETs                  |
| **Asymmetric / PKI** | RSA, ECDSA, x.509, VCs, DIDs            | Signatures, SSI, zk-SNARKs, zkCP, PGP, Group Signatures |
| **Hybrid / Layered** | TLS (asymmetric + symmetric), PAKE, MPC | zk-Rollups, Secure Messaging                            |


🔐 Cryptography

Cryptography is the science of securing information through encoding so that only intended recipients can access or understand it.

🔐 Symmetric Cryptography

Definition: Uses a single shared key for both encryption and decryption.

Use Cases: Fast and efficient, ideal for bulk data encryption.

▶️ AES, TLS, etc.

AES (Advanced Encryption Standard): A widely used symmetric encryption algorithm.

TLS (Transport Layer Security): Uses AES (among others) to encrypt internet communication.

▶️ Confidentiality

Ensures that information is accessible only to those authorized to view it.

▶️ AES in TLS

AES encrypts data during secure web communication via TLS (used in HTTPS).

▶️ End-to-End Messaging

Messages are encrypted on the sender's side and decrypted only by the receiver (e.g., Signal, WhatsApp).

🧾 Asymmetric Cryptography

Definition: Uses a pair of keys: a public key (shared) and a private key (kept secret).

Use Cases: Digital signatures, secure key exchange, identity authentication.

▶️ RSA, ECC, ECDSA

RSA: One of the first public-key encryption systems.

ECC (Elliptic Curve Cryptography): More efficient than RSA with smaller keys.

ECDSA (Elliptic Curve Digital Signature Algorithm): A digital signature scheme used in cryptocurrencies like Bitcoin.

▶️ Digital Signatures

Provide integrity, authenticity, and non-repudiation of data.

▶️ ECDSA (e.g., Bitcoin)

Proves ownership of a Bitcoin wallet by signing a transaction with a private key.

🧾 PKI / x.509 Certificates

Public Key Infrastructure (PKI): A system that binds public keys to identities through digital certificates.

x.509 Certificates: Standard for SSL/TLS certificates (used in HTTPS).

▶️ HTTPS / SSL / TLS

Protocols that secure web traffic. HTTPS uses TLS and certificates to encrypt communication.

▶️ Certificate Authorities (CAs)

Trusted organizations that issue and manage digital certificates. Central point of trust.

👥 Threshold Signatures

A type of multi-party cryptography where multiple private key holders jointly sign a message.

Use Case: Used in cryptocurrency custody wallets where multiple approvals are needed to move funds.

🆔 Verifiable Credentials and DIDs

Verifiable Credentials (VCs): Digitally signed claims about a person or entity.

DIDs (Decentralized Identifiers): A standard for self-owned, decentralized digital identities.

🔒 Self-Sovereign Identity (SSI)

A model where individuals own and control their identity and credentials without relying on a central authority.

Identity Mixer: A cryptographic tool allowing selective disclosure (only reveal necessary info).

🧰 Privacy Enhancing Technologies (PETs)

A broad set of tools and protocols designed to enhance privacy and limit data exposure.

🕵️ Anonymity Techniques

These methods aim to hide identities or transaction metadata.

▶️ Ring Signatures (Monero)

Allows someone in a group to sign a message without revealing which member signed it.

▶️ zk-SNARKs (Zcash)

Zero-Knowledge Succinct Non-Interactive Argument of Knowledge: Proves you know a secret (like an amount or key) without revealing it.

Used in Zcash for private transactions.

▶️ Blind Signatures

A signer signs a message without knowing its contents.

Used in anonymous e-cash systems.

▶️ Mixers and Tumblers

Pool and shuffle cryptocurrency transactions to break the on-chain link between sender and recipient.

▶️ CoinJoin and CoinShuffle

CoinJoin: Users combine their transactions into one to make it hard to link inputs to outputs.

CoinShuffle: An improved, more decentralized version of CoinJoin.

▶️ Stealth Addresses

One-time addresses generated for each transaction to protect recipient identity (used in Monero).

▶️ Dandelion Protocol

Obscures the origin of cryptocurrency transactions by relaying them over random paths before broadcasting.

▶️ Pseudonymity

Using consistent but fake identifiers (like Bitcoin addresses) that don’t reveal your real identity but can still be tracked over time.

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

| Concept             | Belongs Under                                        | Justification                                                         |
| ------------------- | ---------------------------------------------------- | --------------------------------------------------------------------- |
| **Confidentiality** | Symmetric Cryptography (AES, TLS)                    | Used to encrypt and hide message content                              |
| **Anonymity**       | Privacy-Preserving Protocols under Asymmetric / PETs | Achieved via advanced crypto like ZKPs, Ring Signatures, Mixers, etc. |

