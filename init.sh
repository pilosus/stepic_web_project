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

# run MySQL & create DB
sudo -s /etc/init.d/mysql start
mysql -uroot -e "create database django"

# creare symbolic links to gunicorn configs
sudo -s ln -sf /home/box/web/etc/hello.py  /etc/gunicorn.d/hello.py
sudo -s ln -sf /home/box/web/etc/django-gunicorn.conf  /etc/gunicorn.d/django-gunicorn.conf

# 
cd /home/box/web && \
    virtualenv venv && \
    source /home/box/web/venv/bin/activate && \
    pip install -r requirements/list.txt && \
    cd /home/box/web/ask && \
    gunicorn -с ../etc/django-gunicorn.conf ask.wsgi:application

#sudo -s gunicorn -с /etc/gunicorn.d/hello.py hello:app
#sudo -s gunicorn -с /etc/gunicorn.d/django-gunicorn.conf ask.wsgi:application
