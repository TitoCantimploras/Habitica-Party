- [切换语言: 简体中文](/README.md)
- [切換語言: 繁體中文](/README/README_繁体中文.md)
- [Switch Language: English](/README/README_English.md)
- [Changer de langue: Français](/README/README_Français.md)
- [Sprache wechseln: Deutsch](/README/README_Deutsch.md)
- [言語を切り替える: 日本語](/README/README_日本語.md)

# Introducción al Proyecto 📚

¡Bienvenido al **Proyecto de Gestión Automática de Equipos Habitica**! 🎉 Este proyecto se dedica a optimizar la gestión de miembros del equipo a través de herramientas y scripts automáticos, mejorando así tu experiencia en la plataforma Habitica. Ya seas parte del juego o simplemente desees gestionar tu equipo de manera más sencilla, ¡nuestras herramientas te ayudarán mucho!

## Estructura del Proyecto 📂

A continuación, se presenta la estructura del proyecto, asegurando que puedas encontrar fácilmente los archivos que necesites:

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml
├── LICENSE
├── README.md
├── README
│   ├── README_Deutsch.md
│   ├── README_English.md
│   ├── README_Español.md
│   ├── README_Français.md
│   ├── README_日本語.md
│   └── README_繁体中文.md
├── documents
│   ├── brief_description.md
│   ├── new_members.md
│   ├── party_description.md
│   ├── remove_PM.md
│   └── remove_members.md
├── logs
│   ├── manage_members.log
│   └── update_description.log
├── requirements.txt
└── scripts
    ├── manage_members.py
    └── update_description.py
```

## Descripción de Archivos 🔍

### Gestión Automática de Equipos (`.github/workflows/automated_party_management.yml`)
Este archivo define un flujo de trabajo de GitHub Actions llamado "Gestión Automática de Equipos". Se ejecuta automáticamente cada 10 minutos o se puede activar manualmente, realizando las siguientes funciones:
- Extraer el repositorio de código
- Configurar el entorno de Python 3.8
- Instalar las bibliotecas de dependencias necesarias (como `requests`)
- Ejecutar los scripts de gestión (`manage_members.py` y `update_description.py`), interactuando con la API de Habitica
- Configurar retrasos entre la ejecución de scripts para no exceder los límites de tasa de la API
- Confirmar y enviar los cambios de registro, para documentar actualizaciones de los scripts de gestión

### Licencia (`LICENSE`)
Este proyecto sigue la Licencia Apache 2.0, diseñada para fomentar la colaboración de código abierto y proteger los derechos de creadores y usuarios. La licencia detalla los términos y condiciones para el uso, copia y distribución de software y otras obras.

### Archivo de Dependencias (`requirements.txt`)
Este archivo enumera las bibliotecas y dependencias externas necesarias para el proyecto, que en este caso incluye únicamente la biblioteca "requests", proporcionando una forma sencilla de enviar solicitudes HTTP y manejar respuestas.

### Script de Gestión de Miembros (`scripts/manage_members.py`)
Este script se utiliza para gestionar a los miembros en la plataforma Habitica, automatizando las siguientes tareas:
- Remover miembros inactivos y enviarles notificaciones
- Invitar a nuevos usuarios que buscan unirse al equipo

### Script de Actualización de Descripción (`scripts/update_description.py`)
Este script es responsable de actualizar la descripción del equipo en Habitica, obteniendo dinámicamente contenido y renovándolo. Sus características clave incluyen:
- Obtener citas inspiradoras diarias de una API externa
- Actualizar automáticamente la descripción del equipo, asegurando que la información esté siempre fresca y actualizada.

## Archivos de Registro 📜
Todos los registros de operaciones ejecutadas se almacenan en la carpeta `logs`, facilitando la revisión del historial de ejecuciones y la identificación de posibles problemas.

## Comenzar a Usar 🚀

1. Clona el repositorio del proyecto
2. Instala las dependencias: `pip install -r requirements.txt`
3. Usa el flujo de trabajo automatizado de GitHub Actions y disfruta de una experiencia de gestión de miembros sin fisuras.

## Contribuciones 💡
¡Si deseas contribuir a este proyecto, no dudes en enviar un PR o plantear preguntas! ¡Hagamos que Habitica sea aún más emocionante juntos! ⭐️

¡Gracias por leer el archivo README de este proyecto! Esperamos contar con tu apoyo y participación, ¡ven y ⭐️ este proyecto!