FROM centos:latest
RUN yum install -y zlib-devel bzip2-devel openssl-devel ncurses-devel wget \
sqlite-devel readline-devel tk-devel gcc make libffi-devel mysql-devel httpd mod_wsgi \
&& wget https://www.python.org/ftp/python/3.7.3/Python-3.7.3.tgz \
&& tar -zxvf Python-3.7.3.tgz \
&& cd Python-3.7.3 \
&& ./configure \
&& make&&make install \
&& ln -s /usr/local/bin/python3 /usr/bin/python3 \
&& ln -s /usr/local/bin/pip3 /usr/bin/pip
RUN mkdir ~/.pip \
&& cd ~/.pip \
&& touch pip.conf \
&& echo "#" > pip.conf \
&& sed -i '1a [global]' pip.conf \
&& sed -i '2a timeout = 60' pip.conf \
&& sed -i '3a index-url = https://pypi.doubanio.com/simple/' pip.conf \
&& sed -i '4a trusted-host = pypi.doubanio.com' pip.conf
WORKDIR /var/www/demo
COPY demo .
RUN pip install -r requirements.txt
CMD []
