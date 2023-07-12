import os
import pandas as pd
import json

def excel_to_json(excel_file):
    # Obtener la ruta absoluta del archivo de Python
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Ruta del archivo JSON en el mismo directorio que el archivo de Python
    json_file = os.path.join(script_dir, 'data.json')

    # Leer el archivo Excel
    df = pd.read_excel(excel_file)
    
    # Convertir el DataFrame a JSON
    json_data = df.to_json(orient='records')
    
    # Escribir los datos en un archivo JSON
    with open(json_file, 'w') as f:
        json.dump(json_data, f)
    
    print(f"Los datos se han guardado exitosamente en {json_file}")

# Ruta del archivo Excel
excel_file = '/Users/macbook/GO/src/Proyect/Backend/Base/Estilo_Inteligencia.xlsx'

# Llamar a la función para convertir a JSON y guardar en archivo
excel_to_json(excel_file)