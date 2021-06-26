import PyPDF2
import json

def extraer_pagina(numero):

    pdf_file = open('./assets/book.pdf', 'rb')

    read_pdf = PyPDF2.PdfFileReader(pdf_file)

    page = read_pdf.getPage(numero)

    return page.extractText()


def crear_diccionario(texto):

    contenido = texto

    caracteres = ["\u0152","\n",":","\u00f3","\u00fa","\ufb01","\u00ae","\ufb02","\u2122","\u00bd","\u00ae","\u0142","\u00b0","\u00bb","\u00ab"]
    
    for caracter in caracteres:

        contenido = contenido.replace(caracter,"")

    llaves = ["**Brand Name**","**Generic Name**","**Indications**","**Dose**","**Route**","**Levels and Metabolism**",
              "**Precautions**","**Extemporaneuos Preparation**","**Preparation**", "**References**"]

    llaves2 = [ (item.replace("**","").strip(),item) for item in llaves ]

    diccionario = {}

    for llave in llaves2:

        if llave[0] in contenido:

            contenido = contenido.replace(llave[0],llave[1])

    cachitos = contenido.split("**")

    for i,cachito in enumerate(cachitos,start=0):

        if cachito in [ item.replace("**","").strip() for item in llaves ]:

            diccionario[cachito.strip()] = cachitos[i + 1].strip()

    return diccionario


def main():

    farmacos = dict()

    #pages 166 (10-138)
    for i in range(10,138):

        texto = extraer_pagina(i)

        resultado = crear_diccionario(texto) 



        farmacos[resultado["Generic Name"]] = resultado

        print(f"-------------\n{resultado['Generic Name']} agregado")

    with open("farmacos.json","w",encoding="utf-8") as file:

        file.write(json.dumps(farmacos))    
    

if __name__=="__main__":

    farmacos = json.loads(open("./farmacos.json","r",encoding="utf-8").read())

    omeprazol = farmacos["Omeprazole"]

    dosis = omeprazol["Dose"]

    dosis = dosis.replace("mg","mg**").replace("mL","mL**")

    cachitos = dosis.split("**")

    for cachito in cachitos:

        print(cachito)




