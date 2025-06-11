import hashlib

def generate_hash(filename):
    sha256_hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        print(f"SHA256 for {filename}:\n{sha256_hash.hexdigest()}")
    except FileNotFoundError:
        print("File not found!")

# Example Usage
filename = input("Enter the path to the file: ")
generate_hash(filename)
