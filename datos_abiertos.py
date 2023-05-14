## Importar las librerias basicas para el trabajo
import urllib.request
import json
import csv

## Definir la url para la extraccion de datos
url = "http://datos.congreso.gov.py/opendata/api/data/proyecto"
f = urllib.request.urlopen(url)
data = f.read().decode("utf-8")
readfile = json.loads(data)

with open('datos_abiertos.csv', 'w') as datos_abiertos:
    csvwriter = csv.writer(datos_abiertos)
    count = 0
    for result in readfile:
        if count == 0:
            header = result.keys()
            csvwriter.writerow(header)
            count+=1
        csvwriter.writerow(result.values())
