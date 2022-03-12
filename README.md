### FastAPI con MongoDB Atlas

- Creacion de servicios utilizando la API de Marvel
- Proyecto Dockerizado


![](https://cosasdedevs.com/media/sections/images/fastapi.png)

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)



### Descripción 

----
Creando microservicios en python, utilizando FASTAPI y guardando la data en MongoDB Atlas<br>

### Instalacion y despliege<br>

`$ git clone git@github.com:alonso-08/fastapi-mongodbatlas.git`<br>
`$ cd fastapi-mongodbatlas`<br>
`$ virtualenv env`<br>
`$ .\env\Scripts\activate  `<br>
`$ pip install -r requirements.txt`<br>

### Desplegando el servidor
`$ uvicorn app:app --reload` </br>

Ahora abra su navegador favorito  http://127.0.0.1:8000/docs y empiece a probar los servicios creados.

### Login y registro
Para la validacion del login y creacion de comics para usuarios registrados, utilizar la herramienta de login que nos proporciona FastApi

### Usar la imagen de docker para desplegar

### Repositorio de la imagen

docker pull dockeralonsoll/coppel:v1

### Docker
Para descargar la imagen hay que hacer pull

`$ docker pull dockeralonsoll/coppel:v1`</br>
### Pasos para levantar la imagen de Docker
Una vez teniendo la imagen en nuestro equipo, hay que utilizar el archivo docker-compose.yml

- Descargamos el docker-compose.yml en un directorio
- Abrimos la terminal y accedemos al directorio donde se descargo nuestro archivo.
- Verificar que docker este corriendo en nuestro equipo
- Ejecutar el siguiente comando  y se levantara nuestra aplicacion en la siguiente ruta
-- El puerto en el cual va correr la aplicacion es 5002, http://127.0.0.1:5002/docs
`$ docker-compose  up`</br>
### Archivo docker-compose.yml para más detalles.
```
version: '3'
services:
  coppel-api:
    image: 'dockeralonsoll/coppel:v1'

    build: .
    ports:
      - "5002:80"
```
### El puerto en el cual va correr la aplicacion es 5002, http://127.0.0.1:5002/docs
### Es importante usar http y no https