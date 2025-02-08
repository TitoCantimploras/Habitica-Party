[Back to main language README](README.md)

切换语言: 简体中文
切換語言: 繁體中文
Switch Language: English
Changer de langue: Français
Sprache wechseln: Deutsch
言語を切り替える: 日本語

# Sistema de Autogestión de Proyectos README 🌟

¡Bienvenido a nuestro sistema de autogestión de proyectos! 🎉 Este proyecto está diseñado para la gestión de equipos en la plataforma Habitica, a través de la automatización de la gestión de miembros del equipo y la actualización de la descripción del equipo, ¡asegurando que cada equipo funcione en óptimas condiciones! 👏

## Estructura del Proyecto 🗂️

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

## Introducción a los Archivos del Proyecto 📁

### Archivos de flujo de trabajo 🔄
- **Flujo de trabajo de gestión automatizada**: Este archivo se encuentra en `.github/workflows/automated_party_management.yml`, y a través de GitHub Actions gestiona al equipo de manera regular. Se ejecuta cada 10 minutos, ¡asegurando que el estado del equipo esté siempre actualizado! 💼

### Licencia 📜
- **LICENSE**: Este proyecto utiliza la Licencia Apache 2.0, que especifica claramente los términos de uso, copia y distribución del software y otras obras, ¡para que todos lo tengan claro! ✨

### Archivos de Dependencias 📦
- **requirements.txt**: Este archivo lista las bibliotecas necesarias para el proyecto, que incluye una biblioteca importante: `requests`, que nos ayuda a enviar solicitudes HTTP de manera sencilla, ¡simplificando la escritura de código! 🚀

### Archivos de Scripts 🖥️
- **Script de gestión de miembros (manage_members.py)**: Este script es responsable de monitorear la actividad de los miembros, eliminar automáticamente a miembros inactivos, invitar a nuevos miembros, y más, ¡asegurando que nuestro equipo esté siempre lleno de energía! 💪

- **Script de actualización de descripción (update_description.py)**: La tarea de este script es actualizar la descripción del equipo, que incluye una frase motivacional diaria, información de miembros, hora actual, etc., ¡manteniendo nuestro equipo siempre lleno de energía positiva! 🌈

## Guía de Contribución 🤝

¡Cualquiera que esté interesado en este proyecto es bienvenido a contribuir! Asegúrate de seguir nuestra licencia y de comunicarte amablemente con otros colaboradores. 🌍

## Instrucciones de Uso 🛠️

1. **Clonar el proyecto**: Usa el siguiente comando para clonar el proyecto en tu máquina local:
   ```bash
   git clone https://github.com/your-repo-url.git
   ```

2. **Instalar dependencias**: Instala las bibliotecas necesarias de Python usando pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configurar secretos de GitHub**: Configura el ID de usuario y la clave API necesarios para el script de gestión, asegurándote de que tienes acceso a la interfaz API de Habitica.

4. **Iniciar el flujo de trabajo**: Activa manualmente el flujo de trabajo o espera a que se ejecute automáticamente cada 10 minutos, ¡disfruta de la gestión automatizada! 🥳

## Registro de Actividades 📊

En la carpeta `logs`, puedes encontrar los archivos de registro generados durante la gestión del equipo y la actualización de la descripción, ¡ayudándonos a rastrear cada acción! 🪄

## Contáctanos 📧

Si encuentras algún problema durante el uso del proyecto o deseas hacer sugerencias, ¡no dudes en contactarnos por correo electrónico! 😊

¡Gracias por tu interés y uso del proyecto! ¡Construyamos juntos un equipo más activo y eficiente! 🎊

---

¡Esperamos que esta introducción despierte tu interés en el proyecto, y que pronto puedas disfrutar de la gestión automatizada! 🚀✨