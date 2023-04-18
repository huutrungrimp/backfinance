Problems no such table: customers_customers:

1 - delete all migrations and database tables.

2 - Run migrations for the custom user app. For examples:

python manage.py makemigrations customAuth
python manage.py migrate customAuth

3 - Then run migration for the project level.

python manage.py makemigrations
python manage.py migrate