import httpx
import concurrent.futures

with open("./ssrf-reqs", "r") as f:
    endpoints = [line.strip() for line in f.readlines()]

for i in endpoints:
    print(i)

headers = {"User-Agent": "Mozilla"}


def check_endpoint(endpoint):
    try:
        resp = httpx.get(endpoint, headers=headers, timeout=5)
        if resp.status_code == 200:
            print(f"[+] Success: {endpoint} | Code: {resp.status_code}")
    except Exception as e:
        print(f"[!] Error: {endpoint} | {e}")


with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    executor.map(check_endpoint, endpoints)
