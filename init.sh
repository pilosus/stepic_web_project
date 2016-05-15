### Создание проекта в рамках курса на stepic.org

# $ mkdir -p /home/box/web
# $ git clone https://github.com/your_account/stepic_web_project.git /home/box/web
# $ bash /home/box/web/init.sh

sudo ﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
