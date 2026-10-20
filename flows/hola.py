from prefect import flow, get_run_logger


@flow(log_prints=True)
def hola(nombre: str = "mundo"):
    print(f"Hola, {nombre}!")
    logger = get_run_logger()
    logger.info("Este flow se ejecutó dentro de un contenedor Docker")


if __name__ == "__main__":
    hola()
