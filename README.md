# Proyecto: Platos Típicos de Ecuador - Django

## Descripción
Este proyecto es una aplicación web desarrollada con el framework Django, diseñada para mostrar y gestionar algunos de los platos típicos de Ecuador. La aplicación cuenta con dos interfaces principales: una **vista para el cliente**, donde los usuarios pueden explorar los platos disponibles y realizar pedidos, y una **vista de administración**, donde se gestionan los datos de los platos.

La vista del cliente ha sido diseñada con un enfoque visual atractivo, implementando **CSS** para mejorar la experiencia del usuario. Los clientes pueden ver una lista de platos con detalles como nombre, descripción, región de origen y precio estimado, lo que facilita la exploración y selección de platos.

## Características
- **Modelos**: Se utiliza el modelo `PlatoTipico` para almacenar información sobre los platos típicos de Ecuador.
- **Vistas**:
  - **Cliente**: Una vista bonita y funcional, accesible en el puerto principal (`http://127.0.0.1:8000/`), donde los usuarios pueden ver la lista de platos y realizar pedidos.
  - **Administrador**: Una interfaz de gestión accesible en `http://127.0.0.1:8000/admin/`, donde se pueden agregar, editar o eliminar platos.
- **Diseño**: Se ha implementado **CSS** para mejorar la presentación de la vista del cliente, ofreciendo una experiencia visual agradable y profesional.
- **Funcionalidades**:
  - Visualización de platos con nombre, región, descripción y precio.
  - Panel de administración para gestionar los platos.
  - Interfaz intuitiva y fácil de usar tanto para clientes como para administradores.

## Tecnologías Usadas
- **Python 3.x**
- **Django 4.x**
- **HTML**
- **CSS**

## Instrucciones de Instalación
Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local:

1. **Haz un fork** de este repositorio.
2. **Navega al directorio del proyecto**:
   ```bash
   cd proyecto_ecuador
   ```
3. **Instala las dependencias** del proyecto:
   ```bash
   pip install -r requirements.txt
   ```
4. **Realiza las migraciones** de la base de datos:
   ```bash
   python manage.py migrate
   ```
5. **Ejecuta el servidor de desarrollo**:
   ```bash
   python manage.py runserver
   ```
6. **Accede a la aplicación** en tu navegador:
   - **Vista del Cliente**: `http://127.0.0.1:8000/`
   - **Vista del Administrador**: `http://127.0.0.1:8000/admin/`

7. **Configura el superusuario** (si no lo has hecho aún):
   ```bash
   python manage.py createsuperuser
   ```
   Ingresa con tus credenciales para acceder al panel de administración y gestionar los platos típicos.

## Uso del Administrador
Para gestionar los platos típicos, accede a la interfaz administrativa en:
```
http://127.0.0.1:8000/admin/
```
Desde aquí, podrás agregar, editar o eliminar platos, así como gestionar otros aspectos de la aplicación.

## Contribuciones
Si deseas contribuir a este proyecto, ¡eres bienvenido! Haz un fork del repositorio, realiza tus mejoras o correcciones, y envía un **pull request**. Agradecemos cualquier aporte que ayude a mejorar esta aplicación.

