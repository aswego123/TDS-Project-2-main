# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "httpx",
# ]
# ///


import httpx

# send a POST request to https:localhost:8000/receive_request with this json body
"""{
  "email": "your email", // Student email id 
  "secret": "your secret", // Student provided secret code
  "url": "https://tds-llm-analysis.s-anand.net/demo" // A unique task url 
}

"""

payload = {
    "email": "24ds100070@ds.study.iitm.ac.in",
    "secret": "anjali2025",
    "url": "https://tds-llm-analysis.s-anand.net/demo"
}

response = httpx.post("http://localhost:8000/receive_request", json=payload)

print("Response status code:", response.status_code)
print("Response json:", response.json())