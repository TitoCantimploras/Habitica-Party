<div align="center">

[简体中文](/README.md) /[繁体中文](/README/README_zh-TW.md) /[English](/README/README_en.md) /[Français](/README/README_fr.md) /[Deutsch](/README/README_de.md) /[日本語](/README/README_ja.md)

</div>

# 🎉 Sistema de Gestión de Party Automatizado 📈

¡Bienvenido al proyecto **Sistema de Gestión de Party Automatizado**! Nuestro objetivo es proporcionar a los usuarios de Habitica herramientas de gestión de Party eficientes y convenientes. ¡Ya seas un líder apasionado por la gestión o un miembro que desea participar activamente, aquí encontrarás las herramientas y documentos que necesitas! ✨

## 🚀 Estructura del Proyecto

```
.
├── .github
│   └── workflows
│       └── automated_party_management.yml    # Archivo de flujo de trabajo de GitHub Actions
├── LICENSE                                    # Licencia del proyecto
├── documents                                  # Carpeta de documentos del proyecto
│   ├── brief_description.md                   # Documento de breve descripción 
│   ├── new_members.md                         # Documento de lista de nuevos miembros 
│   ├── party_description.md                   # Documento de descripción de la Party 
│   ├── remove_PM.md                           # Plantilla de notificación para eliminación de miembros 
│   └── remove_members.md                      # Plantilla de registro de eliminación de miembros 
├── logs                                        # Carpeta de logs
│   ├── manage_members.log                     # Registro de gestión de miembros
│   └── update_description.log                 # Registro de actualización de descripción
├── requirements.txt                           # Archivo de dependencias 
└── scripts                                     # Directorio de scripts
    ├── manage_members.py                      # Script para gestionar miembros 
    └── update_description.py                  # Script para actualizar la descripción de la Party 
```

## 📄 Introducción a los Archivos

| Nombre del Archivo                        | Descripción                                                 |
|---------------------------------------|------------------------------------------------------------|
| **automated_party_management.yml**    | Archivo de flujo de trabajo de GitHub Actions que se ejecuta cada 10 minutos, encargado de gestionar las tareas del equipo. Configura el entorno Python, instala las dependencias y ejecuta scripts de gestión de miembros y actualización de descripciones, ¡asegurando que tu Party se mantenga siempre activa! 🎯 |
| **brief_description.md**              | Proporciona una cita del día y su traducción, promoviendo el aprendizaje de idiomas y la participación en la comunidad. Este documento también se actualiza automáticamente con la información de los nuevos miembros, garantizando contenido fresco. 🌱 |
| **new_members.md**                    | Registra las invitaciones a nuevos miembros, destacando la participación activa de la comunidad. Este documento se actualiza a través de operaciones programadas, ¡asegurando que no te pierdas la llegada de nuevos compañeros! 👥 |
| **party_description.md**              | Explica la misión y reglas de la Party, animando a los miembros a compartir experiencias personales y participar activamente en las tareas. Además, el contenido incluye discusiones sobre el existencialismo y el nihilismo, ayudándote a explorar un significado más profundo en la vida. 📚 |
| **remove_PM.md**                      | Una plantilla de notificación amigable, que informa a los miembros que fueron eliminados por inactividad, ofreciendo opciones para volver a unirse, mejorando la amabilidad y eficiencia en la comunicación. 🤝 |
| **remove_members.md**                 | Registra las razones para la eliminación de miembros y enlaces relacionados, asegurando que el proceso de gestión sea transparente y se actualice regularmente para auditoría y registro. 🔍 |
| **requirements.txt**                  | Lista las dependencias de Python necesarias, asegurando que tu entorno esté configurado de manera uniforme para facilitar la instalación de las bibliotecas requeridas. ⚙️ |
| **manage_members.py**                 | Script para gestionar miembros de la Party, incluyendo la eliminación de miembros inactivos, el envío de invitaciones y el registro de logs, simplificando el proceso de gestión. ⚡️ |
| **update_description.py**             | Script que actualiza automáticamente la descripción de la Party, asegurando que tengas contenido actualizado para compartir con los miembros cada día, mejorando el sentido de participación. 🌟 |

## Cómo Usar

1. **Hacer Fork de este proyecto**: Haz clic en el botón "**Fork**" en la esquina superior derecha.
2. **Configurar API Token**: Configura tu token API de Habitica y ID en los secretos de Actions de tu proyecto clonado.
3. **Personalizar Plantillas**: Modifica las plantillas en la carpeta `documents` según sea necesario, asegurándote de no alterar los marcadores.
4. **Disfrutar de la gestión automatizada**: ¡Después de completar los pasos anteriores, podrás lograr la gestión automatizada que deseas! 🚀

## 🌟 Cómo Contribuir

Si consideras que este proyecto te ha sido útil, o si deseas ser parte de él, ¡te invitamos a darle una ⭐️ a nuestro proyecto! ¡Tu apoyo es nuestra mayor motivación! Esperamos tus sugerencias, reportes de problemas o contribuciones de código, ¡bienvenido a participar! 💪

## 📧 Contáctanos

Si tienes alguna pregunta o sugerencia, no dudes en contactarnos a través de Issues y te responderemos lo antes posible. 😉 

¡Gracias por tu interés en el Sistema de Gestión de Party Automatizado, y que disfrutes su uso! 🎉