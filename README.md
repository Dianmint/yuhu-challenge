# Task Manager

Este proyecto es un sistema de gestión de tareas desarrollado en Django, utilizando PostgreSQL como base de datos. Permite a los usuarios crear, listar, editar y eliminar tareas, además de marcar las tareas como completadas. Incluye notificaciones por correo electrónico cuando se actualizan o eliminan tareas.

## Funcionalidades

- **Crear nuevas tareas** con título, correo electrónico, descripción y fecha de vencimiento opcional.
- **Listar todas las tareas** separadas en "To do" y "Done".
- **Editar una tarea existente** para actualizar su información.
- **Eliminar una tarea** con confirmación.
- **Marcar tareas como completadas** con un simple check.
- **Notificaciones por correo electrónico** al actualizar o eliminar una tarea.
- **Interfaz adaptable** y fácil de usar, con un diseño claro que incluye botones de acción y un botón flotante para añadir nuevas tareas.

## Tecnologías y Dependencias

- **Backend**: Django
- **Base de datos**: PostgreSQL
- **Tareas en segundo plano**: Celery y Redis
- **API REST**: Django REST Framework
- **Notificaciones por correo**: Gmail SMTP (configurable mediante variables de entorno)
- **Frontend**: HTML, CSS (con variables CSS), y iconos emoji para editar y eliminar.

## Requisitos

- Python 3.x
- Django
- psycopg2
- Celery
- Redis
- PostgreSQL
- Django REST Framework
- `python-dotenv` para manejar variables de entorno

## Instalación

1. **Clona el repositorio**:

   ```bash
   git clone <URL_DEL_REPOSITORIO>
   cd task-manager
    ```

2. **Crea y activa un entorno virtual**:

   ```bash
   python -m venv env
   source env/bin/activate  # En Windows: env\Scripts\activate
    ```


3. **Instala las dependencias**:

   ```bash
   pip install -r requirements.txt
    ```

4. **Configura las variables de entorno**: Puedes utilizar el archivo env.sample proporcionado como base. Renómbralo a .env, agregalo a la carpeta task_manger y actualiza los valores según tus configuraciones.

   ```bash
   cp env.sample .env
    ```

5. **Configura PostgreSQL**: Asegúrate de tener PostgreSQL instalado y crea una base de datos.

6. **Realiza las migraciones de Django**:

   ```bash
    python manage.py migrate
    ```

7. **Inicia el worker de Celery**: para manejar las tareas en segundo plano (asegúrate de tener Redis corriendo)

   ```bash
    celery -A task_manager worker --loglevel=info
    ```

8. **Inicia el worker de Celery**: para manejar las tareas en segundo plano (asegúrate de tener Redis corriendo)

   ```bash
    python manage.py runserver
    ```

## Uso de la Aplicación

### Vista de lista de tareas
La interfaz principal muestra una lista de tareas divididas en dos secciones:

- **To do**: Tareas pendientes.
- **Done**: Tareas completadas.

### Botón flotante
Un botón flotante en la esquina inferior derecha permite crear nuevas tareas fácilmente.

### Acciones en las tareas

- **Editar**: Haciendo clic en el icono ✏️ puedes editar una tarea.
- **Eliminar**: Haciendo clic en el icono 🗑️ te redirige a una página de confirmación antes de eliminar la tarea.
- **Marcar como completada**: Al marcar la casilla de verificación, puedes cambiar el estado de la tarea a "Done".

### Notificaciones por correo
Cuando una tarea es actualizada o eliminada, se envía una notificación por correo electrónico al destinatario especificado en la tarea.

## API

Este proyecto incluye una API para manejar las tareas de manera programática. La API está construida con Django REST Framework.

### Endpoints

- `GET /api/tasks/`: Lista todas las tareas.
- `POST /api/tasks/`: Crea una nueva tarea.
- `GET /api/tasks/<id>/`: Detalles de una tarea específica.
- `PATCH /api/tasks/<id>/`: Actualiza parcialmente una tarea.
- `DELETE /api/tasks/<id>/`: Elimina una tarea.
- `PATCH /api/tasks/<id>/complete/`: Marca una tarea como completada.

## Colección de Postman

Para facilitar el uso de la API, se ha creado una colección de Postman con todos los endpoints necesarios.

### Instrucciones de Uso

1. **Descarga el archivo de la colección**: El archivo JSON de la colección se encuentra en este repositorio con el nombre `Task Manager API.postman_collection.json`.

2. **Importa la colección en Postman**:
   - Abre Postman.
   - Haz clic en el botón de "Importar" en la esquina superior izquierda.
   - Selecciona el archivo `Task Manager API.postman_collection.json` y confirma la importación.

3. **Configura la URL base**:
   - La colección utiliza una variable llamada `base_url`, configurada por defecto en `http://127.0.0.1:8000`.
   - Si estás ejecutando el proyecto en una URL diferente o en un entorno de producción, actualiza esta variable en Postman para reflejar la URL correcta.

4. **Modifica los valores de los parámetros**:
   - Para endpoints que requieren un `id` de tarea, reemplaza `:id` con el identificador correspondiente en cada solicitud.

Esta colección te permitirá probar y explorar la API de manera rápida y sencilla.

## Ejecutar los Tests

Este proyecto incluye un conjunto de tests para verificar que las funcionalidades principales funcionan correctamente.

### Ejecución de Tests

1. **Asegúrate de tener las dependencias instaladas** y la base de datos configurada.
2. **Ejecuta los tests** usando el siguiente comando:

   ```bash
   python manage.py test
    ```

