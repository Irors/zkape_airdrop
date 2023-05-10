import requests



with open("wallets.txt") as wallet:
    wallets = wallet.readlines()

for adresss in wallets:
    json_data = {
        'address': f'{adresss}',
    }

    if adresss == wallets[-1]:
        response = requests.post('https://zksync-ape-apis.zkape.io/airdrop/index/getcertificate', json=json_data)
        if int(response.json()['Data']['value']) / 10**18 != 0:
            print(f"{response.json()['Data']['owner']} rewards - {int(response.json()['Data']['value']) / 10**18}")


    else:
        response = requests.post('https://zksync-ape-apis.zkape.io/airdrop/index/getcertificate', json=json_data)
        if int(response.json()['Data']['value']) / 10**18 != 0:
            print(f"{response.json()['Data']['owner']} rewards - {int(response.json()['Data']['value']) / 10**18}")



print("Всё, конец!")
