# Function to generate a super-increasing sequence for the public key
import random


def generate_super_increasing_sequence(n):
    sequence = [random.randint(1, 100)]
    while len(sequence) < n:
        next_element = sum(sequence) + random.randint(1, 10)
        sequence.append(next_element)
    return sequence


# Function to generate the private key from the public key
def generate_private_key(public_key, q, r):
    private_key = [(r * element) % q for element in public_key]
    return private_key



def encrypt_message(message, public_key):
    # Ensure the message is in binary and its length matches the public key length
    binary_message = bin(message)[2:].zfill(len(public_key))

    # Encrypt the message by summing elements of the public key based on the binary message
    encrypted_message = sum(element if bit == '1' else 0 for bit, element in zip(binary_message, public_key))

    return encrypted_message


def modular_inverse(a, m):
    # Find the modular inverse of a modulo m
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None


def decrypt_message(encrypted_message, private_key, q, r):
    # Find the modular multiplicative inverse of r modulo q
    r_inverse = modular_inverse(r, q)

    # Adjust the encrypted message using the inverse
    adjusted_message = (encrypted_message * r_inverse) % q

    # Decrypt the adjusted message using the private key (super-increasing sequence)
    binary_message = ''
    sum_so_far = adjusted_message
    for element in reversed(private_key):
        if element <= sum_so_far:
            binary_message = '1' + binary_message
            sum_so_far -= element
        else:
            binary_message = '0' + binary_message

    # Convert binary message to integer
    return int(binary_message, 2)




n = 8  # Number of elements in the super-increasing sequence
q = 103  # Modulus (should be greater than the sum of the super-increasing sequence)
r = 3  # Multiplier for generating private key

# Generate the public key and private key
public_key = generate_super_increasing_sequence(n)
private_key = generate_private_key(public_key, q, r)
print(private_key, public_key)



# Encrypt the message
encrypted_message = encrypt_message(12346, public_key)
print(f"Encrypted message: {encrypted_message}")

# Decrypt the message
decrypted_message = decrypt_message(encrypted_message, public_key, q, r)  # Use public_key as it's the original super-increasing sequence
print(f"Decrypted message: {decrypted_message}")





