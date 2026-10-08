"""Encrypt data.json into data.enc.json for the passcode-locked page.

Usage: python3 tools/encrypt.py <path/to/data.json> <passcode>
Never commit data.json itself; only data.enc.json goes in the repo.
"""
import base64, json, os, sys
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

ITER = 600_000
src, passcode = sys.argv[1], sys.argv[2]
plain = json.dumps(json.load(open(src, encoding="utf-8")), ensure_ascii=False, separators=(",", ":")).encode()
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data.enc.json")
salt = None
if os.path.exists(out):  # keep the salt so devices that remember the key keep working
    try: salt = base64.b64decode(json.load(open(out))["salt"])
    except Exception: salt = None
salt, iv = salt or os.urandom(16), os.urandom(12)
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(passcode.encode())
ct = AESGCM(key).encrypt(iv, plain, None)
e = lambda b: base64.b64encode(b).decode()
json.dump({"v": 1, "iter": ITER, "salt": e(salt), "iv": e(iv), "ct": e(ct)}, open(out, "w"))
print("wrote", os.path.normpath(out))
