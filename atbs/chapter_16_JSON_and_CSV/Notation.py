########################
### CSV Module
########################
# import csv
# from pprint import pprint
# import os
#
# os.makedirs('headerRemoved', exist_ok=True)
#
# # Loop through every file in the current working directory.
# for csvFilename in os.listdir('.'):
#      if not csvFilename.endswith('.csv'):
#         continue    # skip non-csv files
#
#      print('Removing header from ' + csvFilename + '...')
# csvRows = []
# csvFileObj = open('example.csv')
# readerObj = csv.reader(csvFileObj)
# for row in readerObj:
#     if readerObj.line_num == 1:
#         continue# skip first row
#     csvRows.append(row)
# csvFileObj.close()
# csvFileObj = open(os.path.join('headerRemoved', 'example.csv'), 'w', newline='')
# csvWriter = csv.writer(csvFileObj)
# for row in csvRows:
#     csvWriter.writerow(row)
# csvFileObj.close()


# example_read = open('WordsForGames.txt')
# read = csv.reader(example_read)
# pprint([d for d in read])
# example_read.close()

# example_write = open('WordsForGames.txt','w',newline='')
# write_to_file = csv.writer(example_write)
# print(write_to_file.writerow(['spam', 'eggs', 'bacon', 'ham']))
# example_write.close()
#
# csvFile = open('example.csv', 'w', newline='')
# outputDictWriter = csv.DictWriter(csvFile, ['Name', 'Pet', 'Phone'])
# outputDictWriter.writeheader()
# outputDictWriter.writerow({'Name': 'Alice', 'Pet': 'cat', 'Phone': '555-1234'})
# outputDictWriter.writerow({'Name': 'Bob', 'Phone': '555-9999'})
# outputDictWriter.writerow({'Phone': '555-5555', 'Name': 'Carol', 'Pet':'dog'})
# csvFile.close()
#
# open_file = open('example.csv')
# example = csv.DictReader(open_file,)
# for row in example:
#     print(row['Name'].rjust(5),row['Pet'].rjust(5),row['Phone'].rjust(5))

###############################
#  JSON Module
###############################
## Reading
string_of_json_data = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
import json
import sys
json_data_as_python_value = json.loads(string_of_json_data)
#print(json_data_as_python_value)
## Writing
pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie',
'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
#print(stringOfJsonData)



print(sys.argv)


