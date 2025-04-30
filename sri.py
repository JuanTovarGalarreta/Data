import pandas as pd

def exportar_dataset_ficticio(ruta_salida):
    """
    Crea un dataset ficticio y lo exporta a un archivo CSV.
    """
    # Crear dataset ficticio
    datos = {
        'Nombre': ['Ana', 'Luis', 'Carlos', 'María'],
        'Edad': [23, 35, 29, 42],
        'Ciudad': ['Lima', 'Bogotá', 'México DF', 'Buenos Aires']
    }

    # Convertir a DataFrame
    df = pd.DataFrame(datos)

    # Exportar a CSV
    try:
        df.to_csv(ruta_salida, index=False)
        print(f"✅ Dataset ficticio exportado exitosamente a {ruta_salida}")
    except Exception as e:
        print(f"❌ Error al exportar el dataset: {e}")

# 📌 Ejemplo de uso:
if __name__ == "__main__":
    ruta_salida = "dataset_ficticio.csv"
    exportar_dataset_ficticio(ruta_salida)
