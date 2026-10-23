from prefect import flow


@flow(log_prints=True)
def hola(nombre: str = "mundo"):
    print(f"Hola, {nombre}!")


if __name__ == "__main__":
    hola()
