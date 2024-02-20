# import random
#
#
# # Function to generate a super-increasing sequence for the public key
# def generate_super_increasing_sequence(n):
#     sequence = [random.randint(1, 100)]
#     while len(sequence) < n:
#         next_element = sum(sequence) + random.randint(1, 10)
#         sequence.append(next_element)
#     return sequence
#
#
# # Function to generate the private key from the public key
# def generate_private_key(public_key, q, r):
#     private_key = [(r * element) % q for element in public_key]
#     return private_key
#
#
# # Function to encrypt the plaintext using the public key
# def knapsack_encrypt(plaintext, public_key):
#     # binary_message = ''.join(format(ord(char), '08b') for char in plaintext)
#
#     encrypted_message = sum(public_key[i] for i in range(len(plaintext)) if plaintext[i] == '1')
#     return encrypted_message
#
#
# # Function to decrypt the ciphertext using the private key
# def knapsack_decrypt(ciphertext, private_key, q, r):
#     r_inverse = pow(r, -1, q)  # Modular multiplicative inverse of r
#     decrypted_message = ''
#     for element in reversed(private_key):
#         if (ciphertext * r_inverse) % q >= element:
#             decrypted_message = '1' + decrypted_message
#             ciphertext -= element
#         else:
#             decrypted_message = '0' + decrypted_message
#     return decrypted_message
#
#


import random
from gmpy2 import invert
import time

MAX_CHARS = 32
BINARY_LENGTH = MAX_CHARS * 8


class MerkleHellman:

    def __init__(self, b=[], w=[], q=0, r=0):
        self.b = b
        self.w = w
        self.q = q
        self.r = r

    def getPublicKey(self):
        return self.b

    def getPrivateKey(self):
        return self.w, self.q, self.r

    def genKeys(self, randomNumber):
        maxBits = 5
        # random.seed(time.time())
        self.w.append(randomNumber)
        sum = self.w[0]
        for i in range(1, BINARY_LENGTH):
            self.w.append(sum + randomNumber)
            sum += self.w[i]

        self.q = sum + randomNumber
        self.r = self.q - 1
        for i in range(BINARY_LENGTH):
            self.b.append((self.w[i] * self.r) % self.q)

    # @profile
    def encryptKey(self, message, publicKey):

        if len(message) > MAX_CHARS:
            print("\nYour message should have at most ", MAX_CHARS, "characters! Please try again.\n\n")
        elif len(message) <= 0:
            print("\nYou message should not be empty! Please try again.\n\n")

        msgBinary = ''.join('{:08b}'.format(publicKey) for publicKey in message.encode('utf8'))

        if len(msgBinary) < BINARY_LENGTH:
            msgBinary = msgBinary.zfill(BINARY_LENGTH)

        result = 0

        for i in range(len(msgBinary)):
            result += publicKey[i] * int(msgBinary[i], 2)

        return str(result)

    def decryptKey(self, ciphertext, w, q, r):

        decrypted_binary = ''
        ciphertext = int(ciphertext)

        tmp = (ciphertext * invert(r, q)) % q

        for i in range(len(w) - 1, -1, -1):
            if w[i] <= tmp:
                tmp -= w[i]
                decrypted_binary += '1'
            else:
                decrypted_binary += '0'
        return int(decrypted_binary[::-1], 2).to_bytes((len(decrypted_binary) + 7) // 8, 'big').decode()



# Example usage
mh = MerkleHellman()
randomNumber = random.randint(1, 10)  # Example random number for key generation
mh.genKeys(randomNumber)

publicKey = mh.getPublicKey()
privateKey = mh.getPrivateKey()
message = "1a2b3c4d5e6f70819293a4b5c6d7e8f9"

encrypted = mh.encryptKey(message, publicKey)
print(f"Encrypted message: {encrypted}")

decrypted = mh.decryptKey(encrypted, *privateKey)
print(f"Decrypted message: {decrypted}")
