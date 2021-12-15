import requests
import os


def baixa_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open(endereco, "wb") as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("Download finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()

def PaginaHTML():
    pagina=open("Controle.html","w")

    pagina.write("<html>")
    pagina.write("<head>")
    pagina.write("<meta charset = \"UTF-8\"/>")
    pagina.write("<title> Document </title>")
    pagina.write("<style>")
    pagina.write("img"
                 "{ width:45%;"
                 "height:45%;"
                 "float:left;"
                 "border:2px solid black"
                 "}")
    pagina.write("</style>")
    pagina.write("</head>")
    pagina.write("<body>")
    pagina.write("<img src = \"Foto1.jpg\" alt = \"Imagem do universo\" / >")
    pagina.write("<img src = \"Foto2.jpg\" alt = \"Imagem do universo\" / >")
    pagina.write("<img src = \"Foto3.jpg\" alt = \"Imagem' do universo\" / >")
    pagina.write("<img src = \"Foto4.jpg\" alt = \"Imagem do universo\" / >")
    pagina.write("<img src = \"Foto5.jpg\" alt = \"Imagem do universo\" / >")
    pagina.write("</body>")
    pagina.write("</html>")

if __name__ == "__main__":
    urls = ['https://apod.nasa.gov/apod/image/2112/HH666_HubbleOzsarac_4347.jpg',
            'https://apod.nasa.gov/apod/image/2112/auroraemeteors_boardman_4591.jpg',
            'https://apod.nasa.gov/apod/image/2112/M3Leonard_Bartlett_3843.jpg',
            'https://apod.nasa.gov/apod/image/2112/eclipse_apod.jpg',
            'https://apod.nasa.gov/apod/image/2112/Eclipseclock-final2.JPG']
    output_dir = "C:\\Users\tar27\PycharmProjects\Prova\Bora que Bora\output"
    nomes_arquivos = ['Foto1.jpg', 'Foto2.jpg', 'Foto3.jpg', 'Foto4.jpg', 'Foto5.jpg']

    for x in range(len(urls)):
        baixa_arquivo(urls[x].format(1), nomes_arquivos[x])
        os.path.join(output_dir, nomes_arquivos[x].format(1))

html=PaginaHTML()