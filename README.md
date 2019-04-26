# Scrape Biblioteca National Argentina website

Scrapy project to import data from bn.gov.ar to Wikicommons and Wikidata.


## Install

```
python3 -m venv venv
. venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage

Pass the "Ver todos" link of a content category visible [here](https://catalogo.bn.gov.ar/F/EI9EATR4HRDBGB6HNDML9LMILE7JKPNM7I7NHGFRE2JVT9H4RD-03105?func=find-m).

```
. venv/bin/activate
 scrapy crawl catalogo -a "urls=https://catalogo.bn.gov.ar/F/EI9EATR4HRDBGB6HNDML9LMILE7JKPNM7I7NHGFRE2JVT9H4RD-01541?func=find-c&order=libros&ccl_term=%28+WRD+%3D+%28+alldocuments+%29+%29+and+%28+WFM+%3D+%28+BK+%29+%29+and+%28+WFT+%3D+%28+VIEW+%29+%29"
```
