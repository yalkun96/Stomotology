source /Users/zzzzzz/PycharmProjects/Stomotology/venv/bin/activate
exec gunicorn --workers 3 --bind unix:/Users/zzzzzz/PycharmProjects/Stomotology/Stomotology.sock Stomotology.wsgi:application
