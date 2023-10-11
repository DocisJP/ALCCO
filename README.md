Pagina Web Oficial del Partido Libertario de Cutral-Có/Neuquén

Recursos: 
Django, PostgreSQL, Poetry, Django-HTML, CSS, SASS, JavaScript

¿Qué tiene? 
Es una apiclación armada de manera tal que se pueda mostrar y modificar la información de manera fácil utilizando los custom templates de Django en la opción de administrador. 
Contiene una sección "About", un "FAQ" y un "Index" dinamico. 
Como funcionalidad: 
  1) Brinda la posibilidad de contactarse con las personas a cargo de la organización enviando un mail desde la página misma.
  2) Permite realizar donaciones

How to run: 
Ejectuar 'Poetry': 
  - poetry shell
  - poetry install
Ir al Directory CoreRoot\
  - poetry run python manage.py makemigrations
  - poetry run python manage.py migrate
  - poetry run python manage.py runserver
