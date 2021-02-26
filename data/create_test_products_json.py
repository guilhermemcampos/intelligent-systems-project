import pandas as pd
import os
#import json

csv_file_path = os.getcwd() + r'\data\test_products.csv'
df = pd.read_csv (filepath_or_buffer=csv_file_path, sep=',', header=0)
df.head()

df_title = df[['title']].copy()
df_title.head()

json_file_path = os.getcwd() + r'\data\test_products.json'
#df_title.to_json (json_file_path, orient='records', indent=4)

json1 = df_title.to_json (orient='records')
test_products = '{"products": ' + json1 + '}'
#json_load = json.loads(test_products)
#json_dump = json.dumps(json1, indent=4)
#print(json_dump)

test_products_json_file = open(json_file_path, 'wt')
#test_products_json_file.write(json_dump)
test_products_json_file.write(format(test_products))
test_products_json_file.close()

