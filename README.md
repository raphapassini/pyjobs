pyjobs
======

Its a crawler with the goal of extract offers of python jobs from websites, mostly Brazilian websites.

How to install
---------------

1) Check if you have libxml2-dev and libffi-dev, if you doesn't install it:

```sudo apt-get install libxml2-dev libffi-dev```

2) Install project requirements

```pip install -e requirements.txt```

Please, be kind with yourself and install it in an virtualenv! :)

How to run it
--------------

```scrapy crawl ceviu -o ceviu.json```

IMPORTANT
---------

The only working spider is CEVIU, but you can help, see the Roadmap bellow.

ROADMAP
-------

[ ] - Iterate over CEVIU search pages

[ ] - Store items in database, preferably a NoSQL database such as MongoDB

[ ] - Implement Catho.com.br spider

[ ] - Implement Empregos.com.br spider

[ ] - Implement Vagas.com.br spider
