#pip install cryptography

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives.serialization import BestAvailableEncryption

# ---------------------
# GENERATE RSA KEYPAIR
# ---------------------
def generate_keys():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )
    public_key = private_key.public_key()
    return private_key, public_key


# ---------------------
# SIGN DOCUMENT
# ---------------------
def sign_document(private_key, data):
    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature


# ---------------------
# VERIFY DOCUMENT
# ---------------------
def verify_document(public_key, data, signature):
    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False


# ---------------------
# MAIN DEMONSTRATION
# ---------------------
if __name__ == "__main__":
    # Step 1: Generate RSA private/public keys
    private_key, public_key = generate_keys()
    print("Keys generated.\n")

    # Step 2: Read the document to be signed
    file_data = b"This is a confidential document."
    print("Document content:", file_data.decode())

    # Step 3: Sender signs the document
    signature = sign_document(private_key, file_data)
    print("\nSignature created.")
    
    # → Simulate sending: send (document + signature + public_key)
    print("\nSending document and signature...\n")

    # Step 4: Receiver verifies document
    is_valid = verify_document(public_key, file_data, signature)

    if is_valid:
        print("✔ Document is authentic. Signature is valid.")
    else:
        print("❌ Signature invalid! Document may be tampered.")
