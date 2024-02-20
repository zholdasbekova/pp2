import json

file = open("sample-data.json")
j_data = file.read()
data = json.loads(j_data)
print("Interface Status")
print("="*80)
print("DN" + " "*49 + "Description" + " "*11 + "Speed" + " "*4 + "MTU")
print("-"*50 +" " +"-"*20 + " " + "-"*6 + " "+ "-"*6 )
for i in data["imdata"] :
    print(i["l1PhysIf"]['attributes']["dn"], " "*18 , end = "")
    if(len(i["l1PhysIf"]['attributes']["dn"])==42):
        print( " "*9, i["l1PhysIf"]['attributes']["speed"], " ", i["l1PhysIf"]['attributes']["mtu"])
    else:
        print(" "*10, i["l1PhysIf"]['attributes']["speed"], " ", i["l1PhysIf"]['attributes']["mtu"])