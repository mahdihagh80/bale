from hashlib import sha256
import base64


def hash_base64_shorten(url: str, short_url_length: int = 7):
    hashed_url = sha256(url.encode('utf-8')).hexdigest()
    encoded = base64.b64encode(bytes(hashed_url, encoding='utf-8'))
    return encoded[:short_url_length].decode('utf-8')
