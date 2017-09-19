puerto para pgadmin 5432




ALTER DATABASE goodreads OWNER TO goodreads_user;

ALTER USER goodreads_user WITH PASSWORD 'goodreads123';


python manage.py startapp Books modules/Books/



http://localhost:8000/admin/

pip install djangorestframework



# Respaldar base de datos de aplicacion 

./manage.py dumpdata Authors > authors.json


./manage.py dumpdata Books > books.json


### Ahora se borran todas las tablas desde pgAdmin4

./manage.py loaddata authors.json

./manage.py loaddata books.json 

### Creando un superUser

./manage.py createsuperuser
