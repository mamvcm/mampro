from prefect import flow, task

@task
def extraer() -> list[int]:
    print("Extrayendo datos...")
    return [1, 2, 3, 4, 5]

@task
def transformar(datos: list[int]) -> list[int]:
    print("Transformando datos...")
    return [n * 10 for n in datos]

@task
def cargar(datos: list[int]) -> None:
    print(f"Cargando {len(datos)} registros: {datos}")

# Cambia el nombre de 'etl' a 'hola'
@flow(log_prints=True)
def hola(): 
    crudos = extraer()
    limpios = transformar(crudos)
    cargar(limpios)

if __name__ == "__main__":
    hola()
