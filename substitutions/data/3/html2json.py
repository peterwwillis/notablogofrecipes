#!/usr/bin/env python3
from bs4 import BeautifulSoup
import json, sys
import unicodedata

def debugunicode(s):
    #r2e = row2.encode('utf-8')
    #r2en = unicodedata.normalize('NFKD', r2e.decode('utf-8', 'ignore'))
    #r2en = unicodedata.normalize('NFKD', row[2])
    #print("row2: %s -> %s -> %s" % ( row2, r2e, r2en ) )
    #print("  type: %s" % type(row2))
    for i, c in enumerate(s):
        print(i, '%04x' % ord(c), unicodedata.category(c), end=" ")
        try:
            if unicodedata.name(c): print(unicodedata.name(c))
        except: pass
        if unicodedata.category(c) == "No":
            print(unicodedata.numeric(c))

def unicodeit(s):
    return s
    #return unicodedata.normalize(u'NFKD', s).encode('ascii', 'replace').decode('ascii') 

#content = open(sys.argv[1]).read().encode('ascii', 'ignore')
#content = open(sys.argv[1]).read().encode('utf8')
content = open(sys.argv[1]).read().encode('utf-8')
#content = open(sys.argv[1]).read().decode('utf-8')
#content = open(sys.argv[1]).read()
#data = BeautifulSoup(content, "html.parser")
data = BeautifulSoup(content, "html.parser", from_encoding="utf-8")
table = {}

#table_data = [[cell.text for cell in row("td")]
#table_data = [[cell.stripped_strings for cell in row("td")]
#table_data = [[cell.get_text("\n", strip=True) for cell in row("td")]
table_data = [[cell.get_text(" ", strip=True) for cell in row("td")]
                                 for row in data("tr")]

table['items'] = []

for row in table_data:
    if len(row) < 3 or len(row[0]) < 1 or len(row[1]) < 1 or len(row[2]) < 1:
        continue
    if row == ['Ingredient', 'Amount', 'Substitutes']:
        continue

    row[2] = [ i for i in row[2].split("\n") ]
    #print("new row2: %s" % row[2] )
    table['items'].append( { 'Ingredient': row[0], 'Amount': row[1], 'Substitute': row[2] } )

#for row2 in data.body.find_all("div", attrs={"class": "az-term"}):
#    desc = row2.p.text.replace('\n',' ').strip()
#    table[row2.a.text] = desc[0].upper() + desc[1:]

print( json.dumps(dict(table), indent=2, sort_keys=True) )
