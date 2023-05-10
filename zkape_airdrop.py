import requests

with open("wallets.txt", "r") as f:
    recepients = [row.strip() for row in f]

for adresss in recepients:

    json_data = {
        'address': f'{adresss}',
    }

    try:
        response = requests.post('https://zksync-ape-apis.zkape.io/airdrop/index/getcertificate', json=json_data)
        if len(response.json()['Data']['value']) != 0:
            print(f"{adresss} rewards - {int(response.json()['Data']['value']) / 10**18}")
    except:
        pass

print("Всё, конец!")
