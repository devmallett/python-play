import csv



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


# one = []
# two = []
# #Exports Street Dir Prefix, Street Name, Strreet Suffic, Street Dir Suffic, City
# with open('properties.csv',  encoding="utf8") as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         line_count += 1
#         one = row[9]
#         return one

# with open('contacts.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     for row in csv_reader:
#         line_count += 1
#         two = row[15]
#         return two 

# if one = two
#     print(one)

f1 = open('properties.csv', 'encoding="utf8"')
f2 = open('contacts.csv', 'encoding="utf8"')
f3 = open('results.csv', 'encoding="utf8"')

c1 = csv.reader(f1)
c2 = csv.reader(f2)
c3 = csv.writer(f3)

masterlist = list(c2)

for hosts_row in c1:
    row = 1
    found = False
    for master_row in masterlist:
        results_row = hosts_row
        if hosts_row[9] == master_row[15]:
            results_row.append('FOUND in master list (row ' + str(row) + ')')
            found = True
            break
        row = row + 1
    if not found:
        results_row.append('NOT FOUND in master list')
    c3.writerow(results_row)
    print(c3)

f1.close()
f2.close()
f3.close()




        

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

