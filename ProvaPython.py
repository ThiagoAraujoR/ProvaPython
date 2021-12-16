import requests
import bs4
import HTML


def baixa_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, "wb") as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Download finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()


#Definição da data requisitada
print("Data minima 150101")
data_hoje=int(input("Insira a data com formato yy/mm/dd (EX:211216):"))

data_inicio=data_hoje-4
numero_arquivo = 1

while data_inicio <= data_hoje:
    url = f"https://apod.nasa.gov/apod/ap{data_inicio}.html"
    data_inicio += 1
    headers = {
        'User-Agente': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/96.0.4664.45 Safari/537.36 OPR/82.0.4227.23 "
    }

    site = requests.get(url, headers=headers)
    soup = bs4.BeautifulSoup(site.content, 'html.parser')

    contador = 0
    for a in soup.find_all(href=True):
        link = a["href"]
        if contador == 1:
            break
        contador += 1
    print(link)

    url1 = f"https://apod.nasa.gov/apod/{link}"

    nomes_arquivos = f'Foto{numero_arquivo}.jpg'
    baixa_arquivo(url1.format(1), nomes_arquivos)

    numero_arquivo += 1
HTML.PaginaHTML()
