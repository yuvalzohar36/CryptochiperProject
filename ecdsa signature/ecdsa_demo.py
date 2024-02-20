from ecdsa_implementation import secp256k1
import hashlib


def main():
    # Initialize ECDSA with the secp256k1 curve
    dsa = secp256k1()

    # Step 1: Key Generation
    # Alice generates her private key and corresponding public key
    alice_private_key = 0x123456789abcdef  # Example private key, replace with secure random value
    alice_public_key = dsa.calcpub(alice_private_key)

    print("Alice's Public Key:", alice_public_key)

    # Step 2: Signing a Message
    # Alice wants to send a secure message
    message = "Hello, Bob!"
    # Hashing the message for signing
    message_hash = int(hashlib.sha256(message.encode('utf-8')).hexdigest(), 16)

    # Alice signs the message
    signsecret = 0xdeadbeef  # Example sign secret, replace with a secure random value for each signature
    r, s = dsa.sign(message_hash, alice_private_key, signsecret)

    print("Signature (r, s):", (r, s))

    # Step 3: Verifying the Signature
    # Bob receives the message and signature, and uses Alice's public key to verify it
    verification_result = dsa.verify(message_hash, alice_public_key, r, s)

    if verification_result:
        print("Verification successful: The message is authentic and untampered.")
    else:
        print("Verification failed: The message's authenticity could not be verified.")


if __name__ == "__main__":
    main()

# This script demonstrates the use of the Elliptic Curve Digital Signature Algorithm (ECDSA) for secure message
# signing and verification.

# Step 0: Import the necessary modules
# - `secp256k1` from our custom ECDSA implementation for cryptographic operations.
# - `hashlib` for creating message digests.

# Step 1: Key Generation - Alice generates a private key, which is a secret number she must keep secure. - Using the
# `secp256k1` curve, Alice calculates her public key from her private key. The public key can be shared with anyone.

# Step 2: Signing a Message - Alice prepares a message intended for Bob. - She hashes the message using SHA-256 to
# create a fixed-size message digest. This is necessary because the ECDSA signing process operates on numbers,
# and hashing provides a way to consistently turn any message of arbitrary length into a number. - Alice then signs
# the hash of the message using her private key and a randomly chosen secret number (signsecret). This produces two
# numbers, `r` and `s`, which together constitute the digital signature.

# Step 3: Verifying the Signature - Bob receives Alice's message and the signature (`r`, `s`). - Bob hashes the
# message using the same hash function Alice used (SHA-256) to ensure consistency. - He then uses Alice's public key
# to verify the signature against the hash of the message. The verification process checks if the signature (`r`,
# `s`) was indeed created using the corresponding private key of the public key provided, without revealing the
# private key itself.

# The verification process either confirms the signature is valid (meaning the message is authentic and hasn't been
# tampered with since Alice signed it) or fails (indicating the message may not be authentic or has been altered).

# This script encapsulates the principles of digital signatures and public key cryptography, demonstrating how ECDSA
# can be used to ensure the integrity and authenticity of communications between parties.
