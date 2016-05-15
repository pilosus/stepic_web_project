### Создание проекта в рамках курса на stepic.org

# $ mkdir -p /home/box/web
# $ git clone https://github.com/pilosus/stepic_web_project.git /home/box/web
# $ bash /home/box/web/init.sh
# if git files changed locally, stash or reset:
# $ git reset --hard

# it's better to run script with sudo
# sudo bash /home/box/web/init.sh
sudo ﻿ln -sf /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

# in /etc/nginx/sites-enabled/default
# first two comment lines with listen 80 /server_default
