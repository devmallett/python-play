import csv
import re


# with open('contacts.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         if line_count == 0
#         print(row[16])

#%/-------------------------------------------------------------
# Pseodo Code 
    # find people by name (row #_____)
    # find what addresses they're at 
    # if that address = any address from the seller list, return that address

    # for each row in column number 15, 
    # return column number 

    # for each row in column $
    # return that column (2nd column being returned )

    # if column 1 = coumn 2
    # return that column 

#%/-------------------------------------------------------------
        

#Exports Street Dir Prefix, Street Name, Strreet Suffic, Street Dir Suffic, City
with open('properties.csv',  encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count += 1
        splitter = ' '
        rower = row[7:14]
        lsit_one = splitter.join(rower)
        # print(lsit_one)
        # return lsit_one
        print(lsit_one)

    

with open('contacts.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        line_count += 1 
        # print(row[5:10])
        seperator = ' '
        rower = row[5:15]
        list_two = seperator.join(row[5:10])
        # return list_two
        # return rower
        print(list_two)

#     def compare_strings(rower, seperator):
#         final_str = seperator.join(row[5:10])
#         return final_str
#         print(final_str)

        # locator = re.search("a-z", csv_file)
        # if locator == True:
        # owner_names = re.findall("[Ro..t]", csv_reader)
        # print(row[1] +  " " + row[15])
            # print(final_str)
        # print(rower)


        # python checker.py

    # print(f'Processed {line_count} lines.')



# with open('contacts.csv') as csv_file:
#     for row in csv_file:
#         print(row[1:10])
    # data = csv.reader(l)
    #         start_urls = [data]
    # # csv_reader = csv.QUOTE_ALL(csv_file)
    # # for row in csv_reader: 
    # #     print(csv_reader)

    # with open('contacts.csv') as csv_file:
    # for row in csv_file:
    #     print(row[1:10])

