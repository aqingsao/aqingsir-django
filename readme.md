# installation
1. 
sudo pip install django-disqus
sudo pip install pygments
sudo pip install markdown
sudo pip install django-suit
2. 
CREATE DATABASE aqingsir CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

3. 
nohup gunicorn aqingsir.wsgi:application -b 127.0.0.1:8001 --reload&

4. 
