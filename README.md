# Instrucciones para ejecutar este proyecto

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/RafaRearte/ENTREGA1-REARTE.git

cd rearte_project

git checkout rearte_project

- Crear base de datos con los Modelos (hacer migraciones y migrar)
```bash
python manage.py makemigrations app_coder

python manage.py migrate
```

- Ejecutar proyecto
```bash
python manage.py runserver
```
