import httpx
import time


def getdata(token):
    url = "https://multichain-api.birdeye.so/solana/token/tokensecurity?token=" + token

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "agent-id": "43514db9-66d4-4715-9e21-25c054bwa93b",
        "Sec-Fetch-Site": "same-site",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Dest": "empty",
        "Referer": "https://birdeye.so/",
        "Connection": "keep-alive",
        "Origin": "https://birdeye.so",
    }

    resp = httpx.get(url, headers=headers)

    data = resp.json()["data"]["result"]["data"]
    liquidity = None
    price = None
    mut = str(data["mutable_metadata"])
    mint = str(data["mintable"])
    ownership = str(data["renounce"])
    print(f"{mut} {mint} {ownership}")
    resp = httpx.get(
        "https://multichain-api.birdeye.so/solana/overview/token?address=" + token,
        headers=headers,
    ).json()["data"]
    if "liquidity" in list(resp.keys()):
        liquidity = resp["liquidity"]

    if "price" in list(resp.keys()):
        price = resp["price"]

    return mut, mint, ownership, liquidity, price


def x():
    for values in httpx.get("http://localhost:5000/new_tokens").json():
        a, b, c, d, e = getdata(values)
        print(a, b, c, d, e)


while True:
    x()
    time.sleep(10)
