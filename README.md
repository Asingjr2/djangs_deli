# DJANG'S DELI

Sample Deli App that displays menu items and store locations.  Project uses both Django and Angular version 5.2.0 (with cli version 1.7.3) so both must be installed. Documentation on downloading Angular can be found at https://angular.io/guide/quickstart. 


__Features in development include:__
 * Cart for checkout 
 * Ability to check distance of user from selected store 
 * Guard service use for cart during checkout


## DJANGO Installation
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic
python manage.py createsuperuser
python manage.py runserver
```

## ANGULAR 5 INSTALLATION
```bash
cd into "ngClient"
npm install
ng serve
```
