[Back to main language README](README.md)

# 🎉 Proyecto de Gestión de Equipos Automatizada

¡Bienvenido a nuestro **Proyecto de Gestión de Equipos Automatizada**! 🚀 Este proyecto tiene como objetivo gestionar fácilmente a los miembros del equipo en la plataforma Habitica mediante scripts automatizados, manteniendo al equipo activo y mejorando la eficiencia administrativa. ¡Veamos la estructura de este proyecto y sus funciones!

## 📁 Estructura del Proyecto

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "Flujo de trabajo de gestión de equipos automatizada"
    }
  },
  "LICENSE": "Archivo de licencia",
  "README.md": "Documento de descripción del proyecto",
  "README": {
    "README/README_Deutsch.md": "Documentación en alemán",
    "README/README_English.md": "Documentación en inglés",
    "README/README_Español.md": "Documentación en español",
    "README/README_Français.md": "Documentación en francés",
    "README/README_日本語.md": "Documentación en japonés",
    "README/README_繁体中文.md": "Documentación en chino tradicional"
  },
  "documents": {
    "documents/brief_description.md": "Descripción breve del proyecto",
    "documents/new_members.md": "Introducción de nuevos miembros",
    "documents/party_description.md": "Descripción del equipo",
    "documents/remove_PM.md": "Descripción para eliminar al gerente del proyecto",
    "documents/remove_members.md": "Descripción para eliminar miembros"
  },
  "logs": {
    "logs/manage_members.log": "Registro de gestión de miembros",
    "logs/update_description.log": "Registro de actualización de descripción"
  },
  "requirements.txt": "Requisitos de dependencias",
  "scripts": {
    "scripts/manage_members.py": "Script de gestión de miembros",
    "scripts/update_description.py": "Script para actualizar descripción"
  }
}
```

## 📜 Funciones del Proyecto

### 1. Flujo de Trabajo de Gestión de Equipos Automatizada 🤖
Hemos definido un flujo de trabajo llamado "Gestión Automatizada del Equipo" en `.github/workflows/automated_party_management.yml`. Se ejecuta automáticamente cada 10 minutos, y también se puede activar manualmente. El objetivo principal de este flujo de trabajo es gestionar y actualizar la información de los miembros del equipo a través de scripts de Python, que incluyen los siguientes pasos importantes:

- **Extraer Código**: Obtener la última versión del código del repositorio.
- **Configurar Entorno Python**: Instalar Python 3.8.
- **Instalar Dependencias**: Instalar la biblioteca `requests` necesaria para los scripts.
- **Ejecutar Script de Gestión**: Ejecutar el script `manage_members.py` para gestionar los miembros.
- **Limitar Frecuencia de Solicitudes**: Evitar sobrecargar la API mediante comandos de descanso.
- **Ejecutar Script de Actualización**: Ejecutar el script `update_description.py` para actualizar la descripción.
- **Registrar Cambios**: Registrar todas las operaciones y enviar los logs al repositorio.

### 2. Licencia 📝
El proyecto incluye un archivo `LICENSE`, que utiliza la Licencia Apache, Versión 2.0, proporcionándole términos y condiciones para usar, copiar y distribuir este software.

### 3. Dependencias 📦
El archivo `requirements.txt` en el proyecto enumera las bibliotecas externas necesarias para la ejecución del proyecto. La biblioteca requerida aquí es `requests`, una popular biblioteca HTTP para manejar solicitudes y respuestas de red.

### 4. Script de Gestión de Miembros 🧑‍🤝‍🧑
El script `manage_members.py` es responsable de gestionar a los miembros del equipo en la plataforma Habitica. Sus principales funciones incluyen:
- Registrar logs, establecer tasas de solicitud, detectar miembros inactivos, enviar invitaciones, etc., para asegurar que el equipo se mantenga activo y no se quede atrás.

### 5. Script de Actualización de Descripción 🔄
El script `update_description.py` actualiza cada cierto tiempo la descripción del equipo, combinando la información de los miembros con contenido de APIs externas, asegurando que la descripción de tu equipo sea siempre fresca y atractiva.

## 🛠️ Cómo Ejecutar
- Asegúrate de tener un entorno Python y de haber instalado las bibliotecas requeridas en `requirements.txt`.
- Ejecuta manualmente los scripts `manage_members.py` y `update_description.py` para gestionar a los miembros y actualizar descripciones.
- También puedes depender del flujo de trabajo automatizado, configurando tareas programadas para mantener fácilmente la información del equipo. 🎈

## 🌐 Soporte Multilenguaje
El proyecto viene con documentación en varios idiomas, incluyendo chino, alemán, inglés, español, francés y japonés, ¡asegurando que cada usuario pueda entender fácilmente el contenido del proyecto! 🌍

## 📬 Comentarios y Soporte
¡No dudes en enviarnos tus preguntas o sugerencias para mejorar este proyecto! 🙏

¡Gracias por leer! Que tu equipo en Habitica esté lleno de energía y siempre esté en el camino del éxito! 💪✨