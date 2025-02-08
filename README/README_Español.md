[Back to main language README](README.md)

# 🥳 Herramienta de Gestión Automática del Equipo README

¡Bienvenido a nuestra herramienta de gestión automática del equipo! Este proyecto está diseñado para mejorar la eficiencia y participación en la gestión de equipos mediante la integración con la API de Habitica.💼✨

## 📁 Resumen de Archivos

### 1. Flujo de Trabajo de GitHub Actions
- **Ruta**: `.github/workflows/automated_party_management.yml`
- **Función**: Este flujo de trabajo se activa cada 10 minutos (también se puede ejecutar manualmente) e incluye los siguientes pasos clave:
  - Clonación del código
  - Configuración del entorno de Python
  - Instalación de dependencias
  - Ejecución del script de gestión para manejar los miembros del equipo en la plataforma Habitica
  - Ejecución de un script de actualización para registrar cambios
- **Características**: Incluye una función de pausa para gestionar la tasa de solicitudes, y finalmente, envía cualquier cambio de registro y lo empuja al repositorio de código.🔄

### 2. Licencia
- **Nombre del Archivo**: `LICENSE`
- **Contenido**: Contiene la licencia Apache, versión 2.0, que describe los términos y condiciones de uso, copia y distribución del software y obras relacionadas, incluyendo definiciones, derechos del usuario, requisitos de redistribución y cláusulas de exención de responsabilidad.📜

### 3. Script de Gestión de Miembros
- **Nombre del Archivo**: `manage_members.py`
- **Función**: Este script de Python está diseñado para gestionar los miembros del equipo en la plataforma Habitica, y sus principales funciones incluyen:
  - **Configuración de Log**: Inicializa el registro para hacer seguimiento de las operaciones del script, incluyendo errores e información general.
  - **Limitación de Tasa**: Implementa mecanismos para cumplir con las restricciones de solicitudes de la API, gestionando el tiempo de las solicitudes.
  - **Gestión de Miembros**:
    - Identificar y recuperar miembros inactivos del equipo basados en el tiempo de última conexión.
    - Enviar notificaciones privadas antes de eliminar miembros.
    - Enviar notificaciones de eliminación de miembros al chat del equipo.
  - **Función de Invitación**: Buscar usuarios que estén buscando equipo y enviarles invitaciones, incluyendo un mensaje formateado que enumera a los miembros invitados.
  - **Herramientas Útiles**: Incluye funciones auxiliares que manejan las respuestas de la API, envían mensajes y calculan el tiempo según la actividad del usuario.

En resumen, este script mejora la gestión del equipo en Habitica al automatizar la eliminación de usuarios inactivos y la invitación de nuevos usuarios, promoviendo una mejor participación de los usuarios.🎉

### 4. Script de Actualización de Descripción
- **Nombre del Archivo**: `update_description.py`
- **Función**: Este script de Python está diseñado para actualizar la descripción del equipo en Habitica, con funciones que incluyen:
  - Obtener diariamente una frase y los detalles de última conexión de los miembros.
  - Registro de logs y aplicación de limitaciones de tasa en las solicitudes a la API.
  - Actualizar dinámicamente la descripción del equipo según los datos recuperados.
  - Leer el formato de descripción desde un archivo plantilla, compilar la información de los miembros y enviar solicitudes de actualización a la API de Habitica.
  - Registrar el éxito y errores durante la operación.

## 🛠️ Instalación y Uso

1. Clona este repositorio:
   ```bash
   git clone https://github.com/yourusername/repository.git
   cd repository
   ```

2. Configura el entorno de Python:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. Instala dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Configura el flujo de trabajo de GitHub Actions (si es necesario) y genera una clave válida en la API de Habitica.

5. Ejecuta los scripts:
   ```bash
   python manage_members.py
   python update_description.py
   ```

## 💡 Contribuciones

¡Se agradecen contribuciones de cualquier tipo! Si tienes sugerencias o preguntas, por favor presenta un issue o inicia un pull request.😊

## 📞 Contacto

Si tienes alguna pregunta o comentario, no dudes en contactarme a través de:
- Correo: your_email@example.com
- GitHub: [TuNombreDeUsuarioGitHub](https://github.com/yourusername)

¡Gracias por usar nuestra herramienta y que la gestión de tu equipo en Habitica sea mucho más fluida!🎊