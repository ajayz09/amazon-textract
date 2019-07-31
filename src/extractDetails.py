import os
import time
import csv
import pandas as pd

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
    table.loc[-1] = a
    table.index = table.index + 1  # shifting index
    table.sort_index(inplace=True) 
    table.drop(table.index[[1,2]], inplace=True)
    #table = table.append(a,ignore_index=True)
    table.to_csv(path,index=False)

def preProcessDocuments():

    documents  = os.listdir("../documents")

    for document in documents:

        documentFormat = document.replace(".jpg","-jpg")
        documentName = document.replace(".jpg","")
        documentPath = "../results/" + documentName
        documentsExtracted.append(documentPath)
        if not os.path.exists(documentPath):
            os.makedirs(documentPath)
        for i in os.listdir(os.curdir):
            
            if os.path.isfile(os.path.join(os.curdir,i)) and documentFormat in i:   
                oldPath = os.curdir + '/' + i
                newPath = documentPath + '/' + i
                os.rename(oldPath, newPath) 
            
                isForms = "-forms.csv"
                isTable = "-tables.csv"

                if isForms in newPath:
                    formsPath = documentPath + '/Forms'
                    if not os.path.exists(formsPath):
                        os.makedirs(formsPath)
                    formsPath = formsPath + '/' + i    
                    os.rename(newPath,formsPath)

                if isTable in newPath:
                    tablePath = documentPath + '/Tables'
                    if not os.path.exists(tablePath):
                        os.makedirs(tablePath)
                    tablePath = tablePath + '/' + i    
                    os.rename(newPath,tablePath)    

    for documents in documentsExtracted:
        tablePath = documents + '/Tables/'
        for tableFile in os.listdir(tablePath):
            filePath = tablePath + tableFile
            time.sleep(2)
            if checkMergeNeeded(filePath):
                print("--------------Merging Rows------------")
                time.sleep(2)
                mergeRows(filePath) 
            else:
                print("Not Required")                 





documentsExtracted = []               

def main():
    
    preProcessDocuments()
    # getDividentStatementContents()

if __name__== "__main__":
    main()