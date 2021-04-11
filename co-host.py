import amino
client = amino.Client()
client.login(input("Email: "), input("Password: "))
print("\nCommunity list: ")
sub_clients = client.sub_clients(start=0, size=500)
for x, name in enumerate(sub_clients.name, 0):
    print(f"{x}. {name}")
selectSub = input("\nCommunity number: ")
comId = sub_clients.comId[int(selectSub)]
while True:
    sub_client = amino.SubClient(comId=comId, profile=client.profile)
    url=input("CHAT URL : ")
    courl=client.get_from_code(url)
    chatid=courl.objectId
    comid=courl.path[1:courl.path.index('/')]
    choice = input("Host / Cohost? (1/2)")
    if choice == "1":
        sub_client.kick(userId=chat.author.userId, chatId=chatid, allowRejoin=True)
    elif choice == "2":
        userid=input("Type СoHost Link: ")
        userid=client.get_from_code(userid).objectId    
        sub_client.kick(userId=userid ,chatId=chatid, allowRejoin=False)
