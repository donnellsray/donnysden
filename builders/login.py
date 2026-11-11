# makes login.json with a one-time admin login URL (never printed)
import json,subprocess
D="./"
raw=subprocess.run(["sh",D+"ab.sh","novamira/create-admin-access-link","{}"],capture_output=True,text=True).stdout
d=json.loads(raw)["data"]
r=subprocess.run(["curl","-sS","-X","POST",d["exchange_url"].replace("\\/","/"),"-H",d["token_header"]+": "+d["access_token"],"-H",d["nonce_header"]+": "+d["access_nonce"],"-H","Content-Type: application/json","-d","{}"],capture_output=True,text=True).stdout
j=json.loads(r); j=j.get("data",j)
json.dump({"login_url":j["login_url"]},open(D+"login.json","w")); print("login link ready")
