#csv is seperated by commas 
# import csv
# ### File handling on csv files:
# ### example CSV file: data.csv
# file_path = "data.csv"

# with open(file_path, mode = "r") as file: #as file chei paila ko f = deko jastai ho. with use garexi chei as file dinu parchha ani file close garirakhnu pardaina but f = dida chei opened file lai close garirakhna parcha and close ni garnu parcha.
#     csv_reader = csv.reader(file)
#     header = (csv_reader) #next nalekhda sab row list ko form ma aaucha
#     # header = next(csv_reader) #next lekhda 1st row skip bhyaera aru list sab aaucha.
#     # header = next(csv_reader) #arko next garda 2nd row ni hatera aru list sab aaucha.
#     for row in csv_reader:
#         print(row)
#         print(row[0]) #return every elements that lies in the index[0] of every list.


# import csv

# data = [
# ["Alice", 30, "London"],
# ["Bob", 25, "Paris"],
# ["Charlie", 35, "Berlin"]
# ]
# file_path = "data.csv"
# with open(file_path, mode = "a", newline = "") as file:
#     csv_writer = csv.writer(file)
#     for row in data:
#         csv_writer.writerow(row)

import csv
file_path = "data.csv"
with open(file_path, mode = "r", newline = "") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader: #read garda reader use garney ani write garda chei data liney maybe.
        print(row)