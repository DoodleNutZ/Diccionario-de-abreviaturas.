breve_dict = {
            "CRINGE": "Algo excepcionalmente raro o embarazoso",
            "LOL": "Una respuesta común a algo gracioso",
            "ROFL": "una respuesta a una broma", 
            "SHEESH": "ligera desaprobación", 
            "CREEPY": "aterrador, siniestro", 
            "AGGRO": "ponerse agresivo/enojado"
            }
            
word = input("Escribe una palabra que no entiendas: ")
word = word.upper()

if word in breve_dict.keys():
    print(breve_dict[word])
else:
    print("Lo siento, esa palabra no está en mi diccionario :(")
