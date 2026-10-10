import requests

cep = input("digite o seu cep")

url=f"https://viacep.com.br/ws/[/cep]/json/"

dados=requests.get(url)
respostas=dados.json()
 
print(F"voce mora na (resposta)["logradouro"]). no barrio[resposta["bairro]). na cidade de (resposta["localidade"])

