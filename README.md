# Proyecto académico

## Descripción

Este proyecto es un proyecto académico que tiene como objetivo la creación de un sistema de   gestión de cruceros. Este sistema estará conectado con una base de datos y permitirá realizar operaciones CRUD.

## Tecnologías utilizadas

- Python 3.10
- uv (manejador de dependencias)
- MySQL
- Docker

## Pasos para conectarse con DB

> Se debe tener instalado Docker para la ejecución de estos pasos.

1. Ejecutar el siguiente comando para levantar el contenedor de MySQL:

```bash
docker-compose up -d
```

2. Verificar con el siguiente comando que el contenedor está corriendo:

```bash
docker ps
```

3. Conectarse al contenedor de MySQL:

```bash
docker exec -it mysql_container bash
```
