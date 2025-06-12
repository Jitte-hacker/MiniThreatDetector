import re

def detect_phishing_link(text):
    # Common suspicious patterns
    patterns = [
        r"http[s]?://(?:[0-9]{1,3}\.){3}[0-9]{1,3}",  # IP address in URL
        r"http[s]?://[a-zA-Z0-9\-\.]*\.(xyz|top|ml|ga|cf)",  # cheap domain extensions
        r"http[s]?://.*(login|verify|secure|update).*",  # phishing keywords
        r"http[s]?://[a-zA-Z0-9\-\.]*\.(com|in|org)/(free|offer|win|gift).*",  # suspicious paths
        r"http[s]?://[^\s]*@[^\s]*",  # username in URL (fake redirects)
    ]

    for pattern in patterns:
        if re.search(pattern, text):
            return True
    return False

# Example usage
input_text = input("Paste a URL or message to scan: ").strip()

if detect_phishing_link(input_text):
    print("⚠️ Warning: This link/message may be a phishing attempt!")
else:
    print("✅ Safe: No phishing patterns detected.")
