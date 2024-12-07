import requests

url = input("Enter the base URL (e.g., http://example.com/): ")
wordlist = ["admin", "login", "dashboard", "config", "uploads"]
print("Starting directory brute force...")

for word in wordlist:
    full_url = f"{url}/{word}"
    response = requests.get(full_url)
    if response.status_code == 200:
        print(f"Found directory: {full_url}")
    else:
        print(f"Not found: {full_url}")
