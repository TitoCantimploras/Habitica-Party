- [{main_language}](README.md)- [切換語言: 繁體中文](README/README_繁体中文.md)
- [Switch Language: English](README/README_English.md)
- [Changer de langue: Français](README/README_Français.md)
- [Sprache wechseln: Deutsch](README/README_Deutsch.md)
- [言語を切り替える: 日本語](README/README_日本語.md)

# 📚 Descripción del Proyecto README

¡Bienvenido a nuestro proyecto! 🎉 Aquí, nos comprometemos a gestionar los miembros de la comunidad de Habitica a través de herramientas automatizadas, haciendo que la gestión del equipo sea más eficiente y fácil. ¡A continuación, conozcamos la estructura y las funcionalidades de este proyecto!✨

## 📁 Estructura del Proyecto

```
{
  ".github": {
    ".github/workflows": {
      ".github/workflows/automated_party_management.yml": "automated_party_management.yml"
    }
  },
  "LICENSE": "LICENSE",
  "README.md": "README.md",
  "README": {
    "README/README_Deutsch.md": "README_Deutsch.md",
    "README/README_English.md": "README_English.md",
    "README/README_Español.md": "README_Español.md",
    "README/README_Français.md": "README_Français.md",
    "README/README_日本語.md": "README_日本語.md",
    "README/README_繁体中文.md": "README_繁体中文.md"
  },
  "documents": {
    "documents/brief_description.md": "brief_description.md",
    "documents/new_members.md": "new_members.md",
    "documents/party_description.md": "party_description.md",
    "documents/remove_PM.md": "remove_PM.md",
    "documents/remove_members.md": "remove_members.md"
  },
  "logs": {
    "logs/manage_members.log": "manage_members.log",
    "logs/update_description.log": "update_description.log"
  },
  "requirements.txt": "requirements.txt",
  "scripts": {
    "scripts/manage_members.py": "manage_members.py",
    "scripts/update_description.py": "update_description.py"
  }
}
```

## 📝 Descripción de Archivos

### Flujo de trabajo automatizado de GitHub Actions

En el archivo `.github/workflows/automated_party_management.yml`, se define un flujo de trabajo de GitHub Actions para gestionar automáticamente a los miembros del equipo. Se activa cada 10 minutos o se puede invocar manualmente, ejecutándose en un entorno de Ubuntu, e incluye varios pasos clave:

1. **Clonar el código**: Obtener el código del proyecto.
2. **Configurar el entorno de Python**: Configurar Python 3.8.
3. **Instalar dependencias**: Instalar la biblioteca `requests` necesaria.
4. **Ejecutar el script de gestión**: Correr el script de Python para gestionar miembros (`manage_members.py`), utilizando variables de entorno para manejar las credenciales de usuario.
5. **Límite de tasa**: Introducir pausas para gestionar la tasa de solicitudes.
6. **Ejecutar el script de actualización**: Correr el script que actualiza la descripción (`update_description.py`), también usando variables de entorno.
7. **Registrar cambios**: Actualizar el log generado por el script en el repositorio.
8. **Enviar cambios**: Pushear el log actualizado de regreso al repositorio remoto.

¡Este flujo de trabajo está diseñado para automatizar de manera eficiente la gestión de miembros del equipo y la actualización de registros; es un asistente inteligente! 🤖

### Archivo de Licencia

El archivo `LICENSE` contiene la Licencia Apache 2.0, que es una licencia de software de código abierto flexible. Establece los términos y condiciones para el uso, copia y distribución del software y otras obras. Otorga a los usuarios el derecho a modificar y redistribuir las obras, asegurando el adecuado reconocimiento a los autores originales. Además, incluye disposiciones sobre el uso de marcas registradas, exenciones de garantías y limitaciones de responsabilidad. Este documento busca promover la colaboración entre desarrolladores y la utilización por parte de los usuarios, manteniendo la libertad del software y protegiendo los derechos de los autores originales.

### Archivo de Dependencias

El archivo `requirements.txt` enumera los paquetes externos y bibliotecas necesarias para ejecutar el proyecto. En este proyecto, solo se menciona la biblioteca `requests`, que es un módulo de Python muy popular que permite a los desarrolladores enviar fácilmente solicitudes HTTP y interactuar con servicios web y APIs. Con el sencillo comando `pip install -r requirements.txt`, ¡puedes instalar estas dependencias fácilmente y comenzar tu aventura mágica! ✨

### Archivos de Script

- **Script de gestión de miembros `manage_members.py`**

  Este script se usa para gestionar a los miembros del equipo de Habitica, realizando las siguientes funciones principales:

  1. **Registro de logs**: Utiliza un módulo de logging para registrar operaciones y errores, almacenando la información en un archivo de logs rotativo y mostrando información importante en la consola.
  2. **Solicitudes API con límite de tasa**: Define una función auxiliar para asegurar que las solicitudes respeten el intervalo de tiempo especificado.
  3. **Gestión de usuarios**: Obtiene la lista de miembros del equipo, verifica miembros inactivos y los elimina.
  4. **Envío de mensajes**: Permite enviar mensajes directos a los usuarios y publicar mensajes de invitación o eliminación de miembros en el chat del equipo.
  5. **Invitar nuevos usuarios**: Envía invitaciones a nuevos usuarios que buscan un equipo, notificando al grupo en el chat.

  Gracias a estas funciones, este script simplifica enormemente la gestión de miembros del equipo de Habitica, ¡haciendo que la administración de la comunidad sea más fácil y agradable! 🎈

- **Script de actualización de descripción `update_description.py`**

  Este script actualiza automáticamente la descripción del equipo de Habitica al integrar citas diarias con la actividad de los miembros. Sus funciones principales incluyen:

  1. **Solicitudes API con límite de tasa**: Administra el intervalo de solicitudes para evitar sobrecargar la API de Habitica.
  2. **Obtención de citas diarias**: Recibe citas diarias de una API externa, incluyendo su contenido en inglés y su traducción.
  3. **Recopilación de datos de miembros**: Reúne información de los miembros del equipo, incluyendo la última hora de inicio de sesión y la duración de la última actividad.
  4. **Formato de descripción**: Lee plantillas en Markdown y formatea la descripción actual, la información de los miembros y la marca de tiempo.
  5. **Envío de actualización**: Envía la descripción actualizada de vuelta a la API de Habitica.

  Con estas medidas automatizadas, el script eleva constantemente la atracción de la descripción del equipo y la interacción entre miembros; ¡es como un amigo con un enfoque artístico! 🎨

---

¡Gracias por revisar nuestro proyecto! Esperamos que las herramientas que ofrecemos hagan más conveniente y divertida la gestión de tu comunidad en Habitica. Si tienes alguna pregunta, ¡no dudes en contactar! 🎈👋