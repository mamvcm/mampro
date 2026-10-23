from prefect import flow

flow.from_source(
    source="https://github.com/mamvcm/mampro-scripts.git",
    entrypoint="flows/hola.py:hola",
).deploy(
    name="prueba-hola",
    work_pool_name="prod-docker-pool",
    image="prefecthq/prefect:3.8.7-python3.11",
    build=False,
    push=False,
)
