# Aplicación Web Blog con Flask

## Descripción

Esta es una aplicación web de blog desarrollada con Flask, que incluye funcionalidades como autenticación de usuarios, creación, actualización y eliminación de blogs. La aplicación utiliza SQLAlchemy para la gestión de la base de datos y Flask-Login para manejar las sesiones de usuario.

## Estructura del Proyecto

La estructura del proyecto se divide en varios módulos y carpetas:

- **blog_app**: Contiene los modelos de la base de datos y las rutas de la aplicación.
  - **models**: Define los modelos de Usuario y Blog.
  - **routes**: Contiene dos blueprints, `auth` para la autenticación y `blogs` para gestionar los blogs.
- **templates**: Almacena los archivos HTML utilizados por la aplicación.

## Configuración

Para configurar la aplicación, asegúrate de tener instalado Python y luego instala las dependencias necesarias ejecutando: pip install`flask flask-sqlalchemy flask-login`

Crea un archivo `config.py` en la raíz del proyecto para definir la configuración de la base de datos y otras variables de entorno necesarias.

## Uso

Para iniciar la aplicación, ejecuta el siguiente comando desde la terminal: `flask run`

Esto iniciará el servidor de desarrollo de Flask y podrás acceder a la aplicación a través de tu navegador web en http://127.0.0.1:5000/.

## Funcionalidades

- **Autenticación de Usuarios**: Los usuarios pueden registrarse, iniciar sesión y cerrar sesión.
- **Gestión de Blogs**: Los usuarios pueden ver, crear, actualizar y eliminar blogs. Solo los administradores tienen permisos para crear y modificar blogs.
- **Filtro de Plantilla Personalizado**: Se ha implementado un filtro de plantilla `b64encode` para codificar imágenes en base64 directamente en las plantillas.

## Contribuciones

Las contribuciones son bienvenidas. Por favor, crea un fork del repositorio, realiza tus cambios y envía una solicitud de pull.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo LICENSE para más detalles.
