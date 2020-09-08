import json
import urllib.request as urllib2
import csv
url='http://dataeng.quero.com:5000/caged-data'
json_obj = urllib2.urlopen(url)

data = json.load(json_obj)

emp_data = data['caged']

# open a file for writing

employ_data = open('EmployData.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(employ_data)

count = 0

for emp in emp_data:

      if count == 0:

             header = emp.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(emp.values())

employ_data.close()