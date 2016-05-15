### Создание проекта в рамках курса на stepic.org

# $ mkdir -p /home/box/web
# $ git clone https://github.com/pilosus/stepic_web_project.git /home/box/web
# $ bash /home/box/web/init.sh
# if git files changed locally, stash or reset:
# $ git reset --hard

# it's better to run script with sudo
# sudo bash /home/box/web/init.sh
﻿ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
/etc/init.d/nginx restart


#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
#sudo /etc/init.d/gunicorn restart
