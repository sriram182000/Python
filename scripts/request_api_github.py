import requests

response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")

complete_detail=response.json()

for i in complete_detail:
    print(i["author_association"])
