Scrapy is a fast, open-source web crawling framework written in Python

### Install scrapy:
```
pip install scrapy
```

### Start a scrapy project
```
scrapy startproject <project_name>
cd <project_name>
scrapy genspider <spider_name> <url> (generate spider)
```

Example:
```
scrapy startproject spider_example
cd spider_example
scrapy genspider worldometers https://www.worldometers.info/world-population/population-by-country
```

### Run project
```
scrapy crawl <spider_name>
scrapy crawl <spider_name> -o <file>.json(.csv) -> save output to file
```

### Scrapy template
List all template that spider can generate
```
scrapy genspider -l:

-> Output:
Available templates:
  basic
  crawl
  csvfeed
  xmlfeed
```

Create crawl template
```
scrapy genspider -t crawl <spider_name> <url>
```


### Pipeline
Pipeline file: pipelines.py  
There are 3 related functions:
- open_spider: called when spider opened
- close_spider: call when spider closed
- process_item: call when each item is process

Config edit: **ITEM_PIPELINES** in **"setting.py"** file
