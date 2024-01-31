import json

users = json.load(open("users_100.json", "r", encoding="utf-8"))

qtd_amigos = 0

for user in users:
    #print(user["name"], len(users["friends"]))
    qtd_amigos += len(user["friends"])

media = qtd_amigos/len(users)

print("Quantidade de amigos:", qtd_amigos)
print("Média de amigos:", media)

for key in users[0].keys():
    print(key)

print("="*60)

for value in users[0].values():
    print(value)

first_user = users[0]

del first_user["friends"]

print(first_user)
print(users[0])