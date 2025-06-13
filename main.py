import hashlib
import re
import os

# === File Integrity Checker ===
def generate_file_hash(filename):
    sha256_hash = hashlib.sha256()
    try:
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        print(f"\n✅ SHA256 Hash of {filename}:")
        print(sha256_hash.hexdigest())
    except FileNotFoundError:
        print("❌ File not found! Check the path again.")

# === Phishing URL Detector ===
def detect_phishing_link(text):
    patterns = [
        r"http[s]?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}",
        r"http[s]?://[a-zA-Z0-9\-\.]*\.(xyz|top|ml|ga|cf)",
        r"http[s]?://.*(login|verify|secure|update).*",
        r"http[s]?://[a-zA-Z0-9\-\.]*\.(com|in|org)/(free|offer|win|gift).*",
        r"http[s]?://[^\s]*@[^\s]*",
    ]
    for pattern in patterns:
        if re.search(pattern, text):
            return True
    return False

# === Main CLI Menu ===
def main_menu():
    while True:
        print("\n====== Mini Threat Detector CLI ======")
        print("1. File Integrity Checker (SHA256)")
        print("2. Phishing Link Detector")
        print("3. Exit")

        choice = input("Choose an option (1/2/3): ").strip()

        if choice == "1":
            filename = input("Enter file path: ").strip()
            generate_file_hash(filename)
        elif choice == "2":
            text = input("Paste a URL or message: ").strip()
            if detect_phishing_link(text):
                print("⚠️ Phishing Pattern Detected!")
            else:
                print("✅ No phishing pattern found.")
        elif choice == "3":
            print("👋 Exiting tool. Stay safe online!")
            break
        else:
            print("❌ Invalid input. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main_menu()
