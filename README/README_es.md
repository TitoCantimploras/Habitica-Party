<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 🎉 Sistema de Gestión de Partidos Automatizado 📈

¡Bienvenido al proyecto del **Sistema de Gestión de Partidos Automatizado**! Nuestro objetivo es proporcionar herramientas eficientes y convenientes para la gestión de partidos a los usuarios de Habitica. ¡Ya seas un líder apasionado por la gestión o un miembro que desea participar activamente, aquí encontrarás las herramientas y la documentación que necesitas! ✨

## 🚀 Estructura del Proyecto

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml    # Archivo de flujo de trabajo de GitHub Actions
├── LICENSE                                    # Licencia del proyecto
├── documents                                  # Carpeta de documentación del proyecto
│   ├── brief_description.md                   # Documento de descripción breve
│   ├── new_members.md                         # Documento de lista de nuevos miembros
│   ├── party_description.md                   # Documento de descripción del partido
│   ├── remove_PM.md                           # Plantilla de notificación para la eliminación de miembros
│   └── remove_members.md                      # Plantilla de registro de miembros eliminados
├── logs                                        # Carpeta de logs
│   ├── manage_members.log                     # Registro de gestión de miembros
│   └── update_description.log                 # Registro de actualizaciones de descripción
├── requirements.txt                           # Archivo de dependencias
└── scripts                                     # Directorio de scripts
    ├── manage_members.py                      # Script para gestionar miembros
    └── update_description.py                  # Script para actualizar la descripción del partido
```

## 📄 Resumen de Archivos

| Nombre del archivo                         | Descripción                                                       |
|------------------------------------------|------------------------------------------------------------------|
| **automated_party_management.yml**       | Archivo de flujo de trabajo de GitHub Actions que se ejecuta cada 10 minutos, encargado de gestionar tareas del equipo. Configura el entorno de Python, instala dependencias y ejecuta scripts de gestión de miembros y actualizaciones de descripción, ¡asegurando que tu partido esté siempre activo! 🎯 |
| **brief_description.md**                 | Proporciona una cita diaria y su traducción, fomentando el aprendizaje de idiomas y la participación comunitaria. Este documento también se actualiza automáticamente con la información más reciente de los miembros, garantizando contenido fresco. 🌱 |
| **new_members.md**                       | Registra las invitaciones a nuevos miembros, destacando la participación activa de la comunidad. Este documento se actualiza a través de operaciones programadas, ¡asegurando que no te pierdas la llegada de nuevos compañeros! 👥 |
| **party_description.md**                 | Explica los objetivos y reglas del partido, alentando a los miembros a compartir experiencias personales y participar activamente en las tareas. Además, contiene discusiones sobre existencialismo y nihilismo, ayudándote a explorar significados más profundos en la vida. 📚 |
| **remove_PM.md**                         | Plantilla de notificación amigable para informar a los miembros que han sido eliminados por baja actividad, ofreciendo opciones para reintegrarse y mejorando la comunicación y la eficiencia. 🤝 |
| **remove_members.md**                    | Registra las razones por las que los miembros fueron eliminados y enlaces relacionados, asegurando un proceso de gestión transparente y actualizándose regularmente para auditoría y registro. 🔍 |
| **requirements.txt**                     | Lista las dependencias de Python necesarias, asegurando que la configuración de tu entorno sea consistente para facilitar la instalación de las bibliotecas requeridas. ⚙️ |
| **manage_members.py**                    | Script para gestionar a los miembros del partido, incluyendo la eliminación de miembros inactivos, envíos de invitaciones y registro de logs, simplificando el proceso de gestión. ⚡️ |
| **update_description.py**                | Script que actualiza automáticamente la descripción del partido, asegurando que tengas contenido actualizado cada día para compartir con los miembros, aumentando el sentido de participación. 🌟 |

## Cómo Usar

1. **Forkea este proyecto**: Haz clic en el botón "**Fork**" en la esquina superior derecha.
2. **Configura el API Token**: Configura tu token de API de Habitica y ID en los secretos de Actions de tu proyecto clonado.
3. **Personaliza las plantillas**: Modifica según sea necesario las plantillas en la carpeta `documents`, asegurándote de no dañar los marcadores de posición.
4. **¡Disfruta de la gestión automatizada!**: ¡Una vez completados estos pasos, podrás disfrutar de la gestión automatizada que esperabas! 🚀

## 🌟 Cómo Contribuir

Si consideras que este proyecto te ha sido útil o deseas participar, ¡te invitamos a darle un ⭐️ a nuestro proyecto! ¡Tu apoyo es nuestra mayor motivación! Esperamos tus sugerencias, reportes de problemas o contribuciones de código, ¡tu participación es bienvenida! 💪

## 📧 Contáctanos

Si tienes alguna pregunta o sugerencia, no dudes en contactarnos a través de Issues, ¡te responderemos lo antes posible! 😉

¡Gracias por tu interés en el Sistema de Gestión de Partidos Automatizado y que tengas una excelente experiencia usando la herramienta! 🎉