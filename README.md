Página Web Oficial del Partido Libertario de Cutral-Có/Neuquén

Esta aplicación web ha sido creada con el propósito de ofrecer una plataforma informativa y funcional para el Partido Libertario de Cutral-Có/Neuquén. Desarrollada con tecnologías de vanguardia como Django, PostgreSQL y Poetry, proporciona una interfaz intuitiva y adaptable.

Características Principales:

Facilidad de Gestión: Gracias a la utilización de templates personalizados de Django, administrar y modificar el contenido es un proceso sencillo y directo a través del panel de administrador.

Secciones: La página está estructurada en diversas secciones para facilitar la navegación. Esto incluye "About" para conocer más sobre el partido, un "FAQ" para resolver dudas comunes, y un "Index" dinámico para las últimas actualizaciones y noticias.

Funcionalidades Destacadas:

Comunicación Directa: Los visitantes pueden ponerse en contacto con los líderes y responsables del partido enviando un correo electrónico directamente desde la página.
Donaciones: La plataforma facilita el proceso de donación para aquellos que desean contribuir al partido.
Calendario de Eventos: Una herramienta integrada permite organizar, agendar y visualizar eventos importantes.
Tecnologías y Recursos Utilizados:

Backend: Django, PostgreSQL
Manejo de dependencias: Poetry
Frontend: Django-HTML, CSS, SASS, JavaScript
Instrucciones para la Ejecución:

Para ejecutar la aplicación, sigue los siguientes pasos:

Iniciar Poetry:

poetry shell
poetry install
Navegar al directorio principal:


cd CoreRoot\
Preparar y ejecutar la base de datos:


poetry run python manage.py makemigrations
poetry run python manage.py migrate
Iniciar el servidor:
poetry run python manage.py runserver
