from bs4 import BeautifulSoup
import time
import pandas as pd

# Website Link
WEBSITE_URL = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Initialize The Webdriver
browser = webdriver.Chrome("chromedriver_win32")
browser.get(WEBSITE_URL)

time.sleep(10)

scraped_data = []

# Define Data Scrapping Method
def scrape():
    print(f'Scrapping page {i+1} ...' )

soup = BeautifulSoup(browser.page_source, "html.parser")

# Find <table>
bright_star_table = soup.find("table", attrs = {"class", "wikitable"})

# Find <tbody>
table_body = bright_star_table.find('tbody')

# Find <tr>
table_rows = table_body.find_all('tr')

# Get Data From <td>
for row in table_rows:
    table_cols = row.find_all('td')
    print(table_cols)

    temp_list = []

    for col_data in table_cols:
        #print(col_data.text)

        data = col_data.text.strip()
        #print(data)

        temp_list.append(data)

        scraped_data.append(temp_list)

stars_data =[]

for i in range(0, len(scraped_data)):

    Star_names = scraped_data[i][1]
    Distance = scraped_data[i][3]
    Mass = scraped_data[i][5]
    Radius = scraped_data[i][6]
    Lum = scraped_data[i][7]

    required_data = [Star_names, Distance, Mass, Radius, Lum]
    stars_data.append(required_data)

# Define headers
headers = ['Star_names', 'Distance', 'Mass', 'Radius', 'Luminosity']

# Define pandas dataframe
star_df_1 = pd.Data_frame(stars_data, columns = headers)

# Convert to CSV
star_df_1.to_csv('scraped_data.csv', index = True, index_label = "id")