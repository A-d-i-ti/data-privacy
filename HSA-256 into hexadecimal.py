import hashlib

def sha256_hash(password):
    # Encode the password into bytes
    password_bytes = password.encode()
    
    # Create SHA-256 hash object
    hash_object = hashlib.sha256(password_bytes)
    
    # Return hexadecimal digest
    return hash_object.hexdigest()


# --- Main Program ---
password = input("Enter a password: ")
hashed = sha256_hash(password)
print("SHA-256 Hash:", hashed)
