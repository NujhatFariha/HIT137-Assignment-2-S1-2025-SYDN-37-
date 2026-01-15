import string

def encrypt_text(shift1, shift2):
    """
    Reads 'raw_text.txt', encrypts content based on user-defined shifts, 
    and writes to 'encrypted_text.txt'.
    """
    try:
        with open("raw_text.txt", 'r') as f:
            raw_text = f.read()
    except FileNotFoundError:
        print("Error: 'raw_text.txt' not found.")
        return

    encrypted_text = ""
    for char in raw_text:
        if 'a' <= char <= 'm':
            # Lowercase, first half: shift forward by shift1 * shift2
            shifted = ord(char) + (shift1 * shift2)
            # Wrap around using modulo arithmetic if needed
            if shifted > ord('m'):
                shifted = ord('a') + (shifted - ord('m') - 1) % 13
            encrypted_text += chr(shifted)
        elif 'n' <= char <= 'z':
            # Lowercase, second half: shift backward by shift1 + shift2
            shifted = ord(char) - (shift1 + shift2)
            # Wrap around
            if shifted < ord('n'):
                shifted = ord('z') - (ord('n') - shifted - 1) % 13
            encrypted_text += chr(shifted)
        elif 'A' <= char <= 'M':
            # Uppercase, first half: shift backward by shift1
            shifted = ord(char) - shift1
            # Wrap around
            if shifted < ord('A'):
                shifted = ord('M') - (ord('A') - shifted - 1) % 13
            encrypted_text += chr(shifted)
        elif 'N' <= char <= 'Z':
            # Uppercase, second half: shift forward by shift2 squared
            shifted = ord(char) + (shift2 ** 2)
            # Wrap around
            if shifted > ord('Z'):
                shifted = ord('N') + (shifted - ord('Z') - 1) % 13
            encrypted_text += chr(shifted)
        else:
            # Other characters remain unchanged
            encrypted_text += char

    with open("encrypted_text.txt", 'w') as f:
        f.write(encrypted_text)
    print("Encryption complete. Encrypted text written to 'encrypted_text.txt'.")

def decrypt_text(shift1, shift2):
    """
    Reads 'encrypted_text.txt', decrypts the content, 
    and writes to 'decrypted_text.txt'.
    """
    try:
        with open("encrypted_text.txt", 'r') as f:
            encrypted_text = f.read()
    except FileNotFoundError:
        print("Error: 'encrypted_text.txt' not found. Run encryption first.")
        return

    decrypted_text = ""
    for char in encrypted_text:
        if 'a' <= char <= 'm':
            # Lowercase, first half: reverse of forward by shift1 * shift2
            shifted = ord(char) - (shift1 * shift2)
            if shifted < ord('a'):
                shifted = ord('m') - (ord('a') - shifted - 1) % 13
            decrypted_text += chr(shifted)
        elif 'n' <= char <= 'z':
            # Lowercase, second half: reverse of backward by shift1 + shift2
            shifted = ord(char) + (shift1 + shift2)
            if shifted > ord('z'):
                shifted = ord('n') + (shifted - ord('z') - 1) % 13
            decrypted_text += chr(shifted)
        elif 'A' <= char <= 'M':
            # Uppercase, first half: reverse of backward by shift1
            shifted = ord(char) + shift1
            if shifted > ord('M'):
                shifted = ord('A') + (shifted - ord('M') - 1) % 13
            decrypted_text += chr(shifted)
        elif 'N' <= char <= 'Z':
            # Uppercase, second half: reverse of forward by shift2 squared
            shifted = ord(char) - (shift2 ** 2)
            if shifted < ord('N'):
                shifted = ord('Z') - (ord('N') - shifted - 1) % 13
            decrypted_text += chr(shifted)
        else:
            # Other characters remain unchanged
            decrypted_text += char

    with open("decrypted_text.txt", 'w') as f:
        f.write(decrypted_text)
    print("Decryption complete. Decrypted text written to 'decrypted_text.txt'.")

def verify_decryption():
    """
    Compares 'raw_text.txt' and 'decrypted_text.txt' to verify success.
    """
    try:
        with open("raw_text.txt", 'r') as f_raw:
            raw_text = f_raw.read()
        with open("decrypted_text.txt", 'r') as f_decrypted:
            decrypted_text = f_decrypted.read()
    except FileNotFoundError as e:
        print(f"Error during verification: {e}. Ensure all files exist.")
        return

    if raw_text == decrypted_text:
        print("Verification successful: Decrypted text matches the original raw text.")
    else:
        print("Verification failed: Decrypted text does not match the original raw text.")

if __name__ == "__main__":
    # Create a dummy raw_text.txt for testing if it doesn't exist
    try:
        with open("raw_text.txt", "x") as f:
            f.write("Hello, World! This is a test for the encryption program 123.\nIt includes uppercase (N-Z) and lowercase letters (a-m, n-z).\nEnjoy! @#$")
        print("'raw_text.txt' created with sample data.")
    except FileExistsError:
        print("'raw_text.txt' already exists. Using existing file.")

    # Prompt user for inputs
    try:
        shift1 = int(input("Enter value for shift1 (integer): "))
        shift2 = int(input("Enter value for shift2 (integer): "))
    except ValueError:
        print("Invalid input. Please enter integers for shifts.")
    else:
        print("-" * 20)
        # 2. Encrypt the contents
        encrypt_text(shift1, shift2)
        print("-" * 20)
        # 3. Decrypt the encrypted file
        decrypt_text(shift1, shift2)
        print("-" * 20)
        # 4. Verify the decryption
        verify_decryption()
        print("-" * 20)

# ---------------- ENCRYPTION FUNCTION ----------------
def encrypt_text(shift1, shift2):
    with open("raw_text.txt", "r") as file:
        text = file.read()

    encrypted = ""

    for ch in text:
        # lowercase letters
        if 'a' <= ch <= 'm':
            encrypted += chr((ord(ch) - ord('a') + shift1 * shift2) % 26 + ord('a'))

        elif 'n' <= ch <= 'z':
            encrypted += chr((ord(ch) - ord('a') - (shift1 + shift2)) % 26 + ord('a'))

        # uppercase letters
        elif 'A' <= ch <= 'M':
            encrypted += chr((ord(ch) - ord('A') - shift1) % 26 + ord('A'))

        elif 'N' <= ch <= 'Z':
            encrypted += chr((ord(ch) - ord('A') + (shift2 ** 2)) % 26 + ord('A'))

        # other characters
        else:
            encrypted += ch

    with open("encrypted_text.txt", "w") as file:
        file.write(encrypted)


# ---------------- DECRYPTION FUNCTION ----------------
def decrypt_text(shift1, shift2):
    with open("encrypted_text.txt", "r") as file:
        text = file.read()

    decrypted = ""

    for ch in text:
        # lowercase letters
        if 'a' <= ch <= 'm':
            decrypted += chr((ord(ch) - ord('a') - shift1 * shift2) % 26 + ord('a'))

        elif 'n' <= ch <= 'z':
            decrypted += chr((ord(ch) - ord('a') + (shift1 + shift2)) % 26 + ord('a'))

        # uppercase letters
        elif 'A' <= ch <= 'M':
            decrypted += chr((ord(ch) - ord('A') + shift1) % 26 + ord('A'))

        elif 'N' <= ch <= 'Z':
            decrypted += chr((ord(ch) - ord('A') - (shift2 ** 2)) % 26 + ord('A'))

        # other characters
        else:
            decrypted += ch

    with open("decrypted_text.txt", "w") as file:
        file.write(decrypted)


# ---------------- VERIFICATION FUNCTION ----------------
def verify_decryption():
    with open("raw_text.txt", "r") as f1, open("decrypted_text.txt", "r") as f2:
        if f1.read() == f2.read():
            print("✅ Decryption successful! Texts match.")
        else:
            print("❌ Decryption failed! Texts do not match.")


# ---------------- MAIN PROGRAM ----------------
shift1 = int(input("Enter shift1: "))
shift2 = int(input("Enter shift2: "))

encrypt_text(shift1, shift2)
decrypt_text(shift1, shift2)
verify_decryption()
