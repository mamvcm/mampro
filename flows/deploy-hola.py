from prefect import flow

flow.from_source(
    source="https://github.com/mamvcm/mampro.git",
    entrypoint="flows/hola.py:hola",
).deploy(
    name="prueba-hola",
    work_pool_name="prod-docker-pool",
    image="prefecthq/prefect:3.8.7-python3.12.14",
    build=False,
    push=False,
)
