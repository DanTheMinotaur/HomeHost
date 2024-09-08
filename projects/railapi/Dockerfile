FROM php:7.2-apache

ADD app.tar.gz /var/www/html/

RUN a2enmod rewrite

RUN service apache2 restart