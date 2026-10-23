from prefect import flow, task, get_run_logger
from prefect.artifacts import create_markdown_artifact


@task
def generar_saludo(nombre: str) -> str:
    """Task que procesa el saludo."""
    logger = get_run_logger()
    mensaje = f"Hola, {nombre}!"
    print(mensaje)  # Se imprimirá en los logs gracias a log_prints=True
    logger.info("Este flow se ejecutó dentro de un contenedor Docker")
    return mensaje


@task
def crear_reporte_saludo(nombre: str, mensaje: str):
    """Task encargada de registrar el artefacto en la interfaz de Prefect."""
    # Estructuramos el contenido en formato Markdown
    contenido_markdown = f"""
    # 🚀 Reporte de Ejecución - Hola Mundo
    
    El flujo de saludo se ha completado correctamente dentro del contenedor.
    
    ### Detalles:
    - **Usuario saludado:** `{nombre}`
    - **Mensaje generado:** *"{mensaje}"*
    - **Entorno:** Contenedor Docker 🐳
    """
    
    # Creamos el artefacto visible en la UI
    create_markdown_artifact(
        key=f"reporte-saludo-{nombre.lower()}",
        markdown=contenido_markdown,
        description=f"Registro de saludo generado para {nombre}."
    )


@flow(log_prints=True)
def hola(nombre: str = "mundo"):
    # 1. Ejecutamos la tarea para obtener el saludo e imprimir logs
    resultado_saludo = generar_saludo(nombre)
    
    # 2. Generamos el artefacto pasando los datos obtenidos
    crear_reporte_saludo(nombre, resultado_saludo)


if __name__ == "__main__":
    hola()
