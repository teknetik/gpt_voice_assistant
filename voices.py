import requests
import json
url = "https://api.elevenlabs.io/v1/voices"

headers = {
  "Accept": "application/json",
  "xi-api-key": "06dadcb30178b8ad0e19f25598461771"
}

response = requests.get(url, headers=headers)

print(response.text)
