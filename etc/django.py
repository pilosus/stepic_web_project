# gunicorn configuration file
# $ gunicorn -c path_to_this_file

pythonpath = '/home/box/web'
bind = "0.0.0.0:8000"
workers = 4
