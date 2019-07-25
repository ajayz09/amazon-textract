import csv
import pandas as pd
import os
import filetype

def checkMergeNeeded(path):

    with open(path, "r") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        # the below statement will skip the first row
        next(csv_reader)
        flag = 0
        count = 0
        for lines in csv_reader:
            count = count + 1
            if count == 2 :
                for entity in lines:
                    for a in entity:
                        if a.isdigit():
                            flag = 1
        if flag == 0 :
            return True
        else:
            return False                    

def mergeRows(path):
    table = pd.read_csv(path,skiprows=1,header=None)
    # print(table.loc[0,:])
    # print(table.loc[1,:])
    a = table.loc[0,:] + table.loc[1,:]
    print(a)

    table.loc[-1] = a
    table.index = table.index + 1  # shifting index
    table.sort_index(inplace=True) 
    table.drop(table.index[[1,2]], inplace=True)
    #table = table.append(a,ignore_index=True)
    print(table)
    table.to_csv(path,index=False)

# path = "../3/Tables/3-jpg-page-1-tables.csv"
# if checkMergeNeeded(path):
#     print("Needed")
#     mergeRows(path)
# else:
#     print("Not Needed")    

# documentsExtracted = ['../results/3', '../results/2', '../results/1']

# for documents in documentsExtracted:
#     tablePath = documents + '/Tables/'
#     for tableFile in os.listdir(tablePath):
#         filePath = tablePath + tableFile
#         print(filePath) 

path = "../documents"
for document in os.listdir(path):
    document = path + '/' + document
    kind = filetype.guess(document)
    if(kind.extension == 'pdf'):
        print(document)
