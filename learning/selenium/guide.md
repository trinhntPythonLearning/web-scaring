Before using selenium, need to install selenium module and webdriver (chromedriver)  
### Fetching page
```
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path=driver_path)
driver = webdriver.Chrome(service=service)
driver.get(url)
```

### Select elememt
```
item = driver.find_element(by=By.XPATH, value='')

# Example for button click
item.click()

# Example for select dropdown menu, using Select()
item = Select(item)
item.select_by_visible_text('value')
```

### Configure webdriver
Work in silence mode, do not open web browser

```
option = Options()
options.headless = True  # hide GUI
options.add_argument("--window-size=1920,1080")  # set window size to native GUI size
options.add_argument("start-maximized")  # ensure window is full-screen
...
driver = webdriver.Chrome(options=options)
```

### Web driver wait until event
Events:
- Item is loaded -> to be valid item
- Button is clicked
- ...

Example:

```
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver=driver, timeout=5).until(
    EC.presence_of_element_located((by, value))
)

-> wait up to 5s for item load
```