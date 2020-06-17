
'''
df_list = pd.read_html(page.text) # this parses all the tables in webpages to a list
df = df_list[0]
df.head()
'''
"""
import pandas as pd
from bs4 import BeautifulSoup

html_string = '''
      <table>
            <tr>
                <td> Hello! </td>
                <td> Table </td>
            </tr>
        </table>
    '''

soup = BeautifulSoup(html_string, 'lxml')  # Parse the HTML as a string

table = soup.find_all('table')[0]  # Grab the first table

new_table = pd.DataFrame(columns=range(0, 2), index=[0])  # I know the size

row_marker = 0
for row in table.find_all('tr'):
    column_marker = 0
    columns = row.find_all('td')
    for column in columns:
        new_table.iat[row_marker, column_marker] = column.get_text()
        column_marker += 1

new_table
"""