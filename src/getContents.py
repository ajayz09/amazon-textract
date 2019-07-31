import os
import time
import csv
import pandas as pd

def getFrankedAmount(df):
    DICTIONARY_FA = "../dictionary/franked-amount"
    temp = open(DICTIONARY_FA,'r').read().split('\n')
    try:
        for i in temp:
            frankedAmountRow = df[df['Key'].str.match(i)]
            if not frankedAmountRow.empty:
                frankedAmount = frankedAmountRow.Value.values[0]
                frankedAmount = frankedAmount.replace("A$","")
                frankedAmount = frankedAmount.replace("$","")
                print('Franked Amount - ',frankedAmount)
                return True
    except:
        return False  

def getUnfrankedAmount(df):
    DICTIONARY_UFA = "../dictionary/unfranked-amount"
    temp = open(DICTIONARY_UFA,'r').read().split('\n')
    try:
        for i in temp:
            unfrankedAmountRow = df[df['Key'].str.match(i)]
            if not unfrankedAmountRow.empty:
                unfrankedAmount = unfrankedAmountRow.Value.values[0]
                unfrankedAmount = unfrankedAmount.replace("A$","")
                unfrankedAmount = unfrankedAmount.replace("$","")
                print('Unfranked Amount - ',unfrankedAmount)
                return True 
    except:
        return False 

def getParticipatingShares(df):
    DICTIONARY_PS = "../dictionary/participating-shares"
    temp = open(DICTIONARY_PS,'r').read().split('\n')
    try:
        for i in temp:
            participatingSharesRow = df[df['Key'].str.match(i)]
            if not participatingSharesRow.empty:
                participatingShares = participatingSharesRow.Value.values[0]
                participatingShares = participatingShares.replace(",","")
                print('Participating Shares - ',participatingShares)
                return True 
    except:
        return False 
        # print("Participating Shares - ")

def getTotalPayment(df):
    DICTIONARY_TP = "../dictionary/total-payment"
    temp = open(DICTIONARY_TP,'r').read().split('\n')
    try:
        for i in temp:
            totalPaymentRow = df[df['Key'].str.match(i)]
            if not totalPaymentRow.empty:
                totalPayment = totalPaymentRow.Value.values[0]
                totalPayment = totalPayment.replace("A$","")
                totalPayment = totalPayment.replace("$","")
                print('Total Payment - ',totalPayment)
                return True
    except:
        return False 
        # print("Total Payment - ")        

def getFrankingCredit(df):
    DICTIONARY_FC = "../dictionary/franking-credits"
    temp = open(DICTIONARY_FC,'r').read().split('\n')
    try:
        for i in temp:
            frankedCreditRow = df[df['Key'].str.match(i)]
            if not frankedCreditRow.empty:
                frankedCredit = frankedCreditRow.Value.values[0]
                frankedCredit = frankedCredit.replace("A$","")
                frankedCredit = frankedCredit.replace("$","")
                print('Franking Credit - ',frankedCredit)
                return True
    except:
        return False 
        # print("Franking Credit - ")       

def getFrankingCreditsFromTable(df):
    DICTIONARY_FC = "../dictionary/franking-credits"
    temp = open(DICTIONARY_FC,'r').read().split('\n')
    try:
        for i in temp:
            if i in df.columns:
                frankedCredit = df[i].iloc[0]    
                frankedCredit = frankedCredit.replace("A$","")
                frankedCredit = frankedCredit.replace("$","")
                print('Franking Credit - ',frankedCredit)
                return True
    except:
        return False           
       
DOCUMENTS_PATH = "../results"
dividendDF = pd.DataFrame(columns=['Number of Securities','Franked Amount','Unfranked Amount','Total Payment','Franking Credit'],index = None)
gotFrankedAmount = False
gotUnfrankedAmount = False
gotParticipatingShares = False
gotTotalPayment = False
gotFrankingCredits = False

for documents in os.listdir(DOCUMENTS_PATH):
    print("\nContents of document - ", documents)
    print("----------------------------")
    FORM_DATA_PATH = DOCUMENTS_PATH + '/' + documents + '/Forms/'
    for forms in os.listdir(FORM_DATA_PATH):
        FORM_DATA = FORM_DATA_PATH + forms 
        data = pd.read_csv(FORM_DATA)
        gotFrankedAmount = getFrankedAmount(data)
        gotUnfrankedAmount = getUnfrankedAmount(data)
        gotParticipatingShares = getParticipatingShares(data)
        gotTotalPayment = getTotalPayment(data)
        gotFrankingCredits = getFrankingCredit(data)

    if not gotFrankingCredits:
        TABLE_DATA_PATH = DOCUMENTS_PATH + '/' + documents + '/Tables/'
        for tables in os.listdir(TABLE_DATA_PATH):
            TABLE_DATA = TABLE_DATA_PATH + tables 
            dataTable = pd.read_csv(TABLE_DATA,skiprows=1,index_col=False)
            getFrankingCreditsFromTable(dataTable)