import hashlib
import os

def calculate_hash(file_path):
    """Calculate SHA256 hash of the given file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def save_hash(file_path, hash_value):
    """Save hash to a .txt file for later comparison."""
    with open(file_path + ".hash.txt", "w") as f:
        f.write(hash_value)

def load_saved_hash(file_path):
    """Load previously saved hash from .txt file."""
    try:
        with open(file_path + ".hash.txt", "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def check_file_integrity(file_path):
    """Compare current file hash with saved hash and print result."""
    current_hash = calculate_hash(file_path)
    if current_hash is None:
        print("❌ File not found!")
        return

    saved_hash = load_saved_hash(file_path)

    if saved_hash is None:
        print("🔐 No previous hash found. Saving current hash...")
        save_hash(file_path, current_hash)
    elif saved_hash == current_hash:
        print("✅ File is intact. No changes detected.")
    else:
        print("⚠️ File has been modified!")

# -------- Main Execution --------
if __name__ == "__main__":
    file_path = input("Enter the path of the file to check: ")
    check_file_integrity(file_path)
