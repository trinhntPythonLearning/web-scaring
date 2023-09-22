### Basic step for BS4

1. Fetch the page
   ```
   page_result = requests.get(url)
   content = page_result.text
   ```

2. Create soup
   ```
   soup = BeautifulSoup(content, 'html.parser')
   ```

3. Find item
   ```
   soup.find(id=’specific_id’)

   soup.find(’tag’, class_=’class_name’)

   soup.find_all(’tag’)

   soup.select('selecter')
   ```