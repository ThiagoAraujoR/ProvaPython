def PaginaHTML():
    pagina=open("ProvaPython.html","w")

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