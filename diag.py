import os, sys, socket, pathlib, traceback
from urllib.parse import urlparse
from dotenv import load_dotenv

print("=== ENV/NET DIAG ===")
print("CWD:", pathlib.Path().resolve())
print(".env exists:", pathlib.Path(".env").exists())

load_dotenv()
url = os.getenv("SUPABASE_URL","").strip()
key = os.getenv("SUPABASE_KEY","")

print("URL:", repr(url))
print("KEY present:", bool(key), "len:", len(key))

if not url:
    sys.exit("FATAL: SUPABASE_URL missing")

u = urlparse(url) if "://" in url else urlparse("https://" + url)
host = (u.netloc or u.path).split("/")[0]
print("Host:", host)

try:
    infos = socket.getaddrinfo(host, 443, type=socket.SOCK_STREAM)
    print("DNS OK:", [i[4][0] for i in infos])
except Exception as e:
    print("DNS ERROR:", e)
    traceback.print_exc()
    sys.exit(2)

print("Done.")
