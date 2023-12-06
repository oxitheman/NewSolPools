import httpx
import time
from flask import Flask
import threading

class TokenTracker:
    def __init__(self):
        self.previous_tokens = set()
        self.new_tokens = set()
        self.printtokens = set()
        self.r = 1
        
    def getraydium(self):
        response = httpx.get("https://api.raydium.io/v2/sdk/token/raydium.mainnet.json")

        if response.status_code == 200:
            return [j["mint"] for j in response.json()["unNamed"]]
        else:
            print("ERR")
            return None
        
    def track(self):
        while True:
            time.sleep(15)
            current_tokens = set(self.getraydium())

            self.new_tokens = current_tokens - self.previous_tokens
            
            if self.new_tokens:
                self.printtokens = self.new_tokens.copy()
                self.r+=1
                print(f"New tokens added {self.new_tokens}")
            self.previous_tokens = current_tokens
                
            
        
tr = TokenTracker()
        
tracking_thread = threading.Thread(target=tr.track)
tracking_thread.start()
app = Flask(__name__)

@app.route('/new_tokens', methods=['GET'])
def get_new_tokens():


    return list(tr.printtokens), 200

if __name__ == '__main__':
    app.run(port=5000)

