FROM httpd:2.4.58-alpine
EXPOSE 80
WORKDIR /usr/local/apache2/htdocs/
COPY ./public .
RUN echo "ServerName localhost" >> /usr/local/apache2/conf/httpd.conf