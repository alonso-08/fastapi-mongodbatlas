### FastAPI con MongoDB Atlas




![](https://cosasdedevs.com/media/sections/images/fastapi.png)

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)



###Descripción 

----
Creando microservicios en python, utilizando FASTAPI y guardando la data en MongoDB Atlas
###Instalación y despliege
`$ git clone git@github.com:alonso-08/fastapi-mongodbatlas.git`
`$ cd fastapi-mongodbatlas`
`$ virtualenv env`
`$ .\env\Scripts\activate  `
`$ pip install -r requirements.txt`

###Desplegando el servidor
`$ uvicorn app:app --reload`
Ahora abra su navegador favorito  http://localhost:8000/docs y empiece a probar los servicios creados.

###Login y registro
Para la validacion del login y creacion de comics para usuarios registrados, utilizar la herramienta de login que nos proporciona FastApi


###Docker
Para descargar la imagen hay que hacer pull al repositorio
`$ docker pull dockeralonsoll/coppel:v1`
Una vez teniendo la imagen en nuestro equipo, solamente resta ejecutar el siguiente comando.
`$ docker-compose up`
###Archivo docker-compose.yml para más detalles.
```
version: '3'
services:
  coppel-api:
    image: 'dockeralonsoll/coppel:v1'
	 build: .
    ports:
      - "5002:80"
```
###El puerto en el cual va correr la aplicacion es port:5002
