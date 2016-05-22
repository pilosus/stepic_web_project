### Создание проекта в рамках курса на stepic.org

# $ mkdir -p /home/box/web
# $ git clone https://github.com/pilosus/stepic_web_project.git /home/box/web
# $ bash /home/box/web/init.sh
# if git files changed locally, stash or reset:
# $ git reset --hard

# create symbolic link to a new nginx config
sudo -s ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/django.conf
sudo -s rm /etc/nginx/sites-enabled/default

# restart nginx
sudo -s /etc/init.d/nginx restart

# in /etc/nginx/sites-enabled/default
# first two comment lines with listen 80 /server_default

# install lib needed for mysql-python package
#sudo -s apt-get install libmysqlclient-dev

# run MySQL & create DB
sudo -s /etc/init.d/mysql start && \
    mysql -uroot -e "create database django"

# creare symbolic links to gunicorn configs
#sudo -s ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
#sudo -s ln -sf /home/box/web/etc/django-gunicorn.conf  /etc/gunicorn.d/django-gunicorn.conf

# 
cd /home/box/web && \
    virtualenv venv && \
    source venv/bin/activate && \
    pip install -r requirements/production.txt && \
    export PYTHONPATH=$(pwd):$PYTHONPATH && \
    cd /home/box/web/ask && \
    python manage.py migrate && \
    exec gunicorn --bind=0.0.0.0:8000 --workers=4 ask.wsgi:application

#exec gunicorn -с ../etc/django-gunicorn.conf ask.wsgi:application
