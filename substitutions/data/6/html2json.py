#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json, sys

content = open(sys.argv[1]).read().encode('ascii', 'ignore')
data = BeautifulSoup(content, "html.parser")
table = {}

#table_data = [[cell.text for cell in row("td")]
#table_data = [[cell.stripped_strings for cell in row("td")]
table_data = [[cell.get_text("\n", strip=True) for cell in row("td")]
                                 for row in data("tr")]

table['items'] = []

if len(table_data) < 1:
    print("Tables: %s" % data("table"))
else:
    #print("table data: %s" % table_data)
    for row in table_data:
        if len(row) != 2 or len(row[0]) < 1 or len(row[1]) < 1:
            continue
        if row == [] or row == ['If your recipe calls for this ingredient:', 'Try substituting this ingredient:']:
            continue
        #print("row: %s" % row)
        row[1] = [ i for i in row[1].split("\n") ]
        table['items'].append( { 'Ingredient': row[0], 'Substitute': row[1] } )

#for row2 in data.body.find_all("div", attrs={"class": "az-term"}):
#    desc = row2.p.text.replace('\n',' ').strip()
#    table[row2.a.text] = desc[0].upper() + desc[1:]

print( json.dumps(dict(table), indent=2, sort_keys=True) )
