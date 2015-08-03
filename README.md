pyjobs
======

Its a crawler with the goal of extract offers of python jobs from websites, mostly Brazilian websites.

How to install
---------------

1) Check if you have libxml2-dev, libffi-dev, libssl-dev libxml2-dev libxslt-dev and mongodb, if you doesn't install it:

```sudo apt-get install libxml2-dev libffi-dev libssl-dev libxml2-dev libxslt-dev mongodb```

2) Install project requirements

```pip install -e requirements.txt```

Please, be kind with yourself and install it in an virtualenv! :)

How to run it
--------------

```scrapy crawl ceviu```
```scrapy crawl catho```
```scrapy crawl vagas```
```scrapy crawl empregos```

ROADMAP
-------

[x] - Iterate over CEVIU search pages

[x] - Store items in database, preferably a NoSQL database such as MongoDB

[x] - Implement Catho.com.br spider

[ ] - Implement Empregos.com.br spider

[ ] - Implement Vagas.com.br spider

[ ] - Build an web interface to search for jobs
