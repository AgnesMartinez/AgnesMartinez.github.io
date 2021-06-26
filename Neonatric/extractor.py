import PyPDF2
import json

def extraer_pagina(numero):

    pdf_file = open('./assets/books/book.pdf', 'rb')

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


    farmacos = json.loads(open("./assets/farmacos.json","r",encoding="utf-8").read())

    #Algunos farmacos vienen con tabla, parece que lo regresa como string sin separadores
    #Omeprazol es un ejemplo, tengo que buscar mas en el documento. 
    #Esta dentro de assets/books, se llama "book.pdf"
    #Ahi puedes consultar las paginas que tienen tabla, apartir de la 10 a la 138

    omeprazol = farmacos["Omeprazole"]

    dosis = omeprazol["Dose"]

    dosis = dosis.replace("mg","mg**").replace("mL","mL**").replace("Volume","Volumen**").strip()

    cachitos = dosis.split("**")
    
    # (1 mg,0.5 mL)

    #Sugerencia tener la informacion en tuplas, (dosis,volumen), asi podemos calcular balance de liquidos. 
    #Requerimiento de agua al dia de un bebe de 3 kg = 300 ml/24hrs (ejemplo)
    #Si le tocan 5mg de omeprazol cada 12 hrs, son 2.5ml de agua.
    #A la solucion de 300ml, le tienes que quitar 2.5ml, porque vas a inyectar 2.5ml con 5 mg de omeprazol
    #Eso se conoce como aforar una solucion.
    
    #6 mg serian 5mg + 1mg
    tuplas = [ (cachitos[i],"4 mL") if i == 5 else (cachitos[i],cachitos[i + 8]) for i in range(6) ]

    #Lo malo es que tenemos que hacer esto por cada tabla x( 
    #Igual y no son tan diferentes a esta
    print(tuplas)
 



