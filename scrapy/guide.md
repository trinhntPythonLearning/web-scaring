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




