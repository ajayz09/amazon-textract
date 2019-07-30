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
                frankedAmount = frankedAmount.replace("$","")
                print('Franked Amount - ',frankedAmount)
                return
    except:
        print("Franked Amount - ")  

def getUnfrankedAmount(df):
    DICTIONARY_UFA = "../dictionary/unfranked-amount"
    temp = open(DICTIONARY_UFA,'r').read().split('\n')
    try:
        for i in temp:
            unfrankedAmountRow = df[df['Key'].str.match(i)]
            if not unfrankedAmountRow.empty:
                unfrankedAmount = unfrankedAmountRow.Value.values[0]
                unfrankedAmount = unfrankedAmount.replace("$","")
                print('Unfranked Amount - ',unfrankedAmount)
                return
    except:
        print("Unfranked Amount - ") 

def getParticipatingShares(df):
    DICTIONARY_PS = "../dictionary/participating-shares"
    temp = open(DICTIONARY_PS,'r').read().split('\n')
    try:
        for i in temp:
            participatingSharesRow = df[df['Key'].str.match(i)]
            if not participatingSharesRow.empty:
                participatingShares = participatingSharesRow.Value.values[0]
                #participatingShares = participatingShares.replace("$","")
                print('Participating Shares - ',participatingShares)
                return
    except:
        print("Participating Shares - ")

def getTotalPayment(df):
    DICTIONARY_TP = "../dictionary/total-payment"
    temp = open(DICTIONARY_TP,'r').read().split('\n')
    try:
        for i in temp:
            totalPaymentRow = df[df['Key'].str.match(i)]
            if not totalPaymentRow.empty:
                totalPayment = totalPaymentRow.Value.values[0]
                totalPayment = totalPayment.replace("$","")
                print('Total Payment - ',totalPayment)
                return
    except:
        print("Total Payment - ")        

def getFrankingCredit(df):
    DICTIONARY_FC = "../dictionary/franking-credits"
    temp = open(DICTIONARY_FC,'r').read().split('\n')
    try:
        for i in temp:
            frankedCreditRow = df[df['Key'].str.match(i)]
            if not frankedCreditRow.empty:
                frankedCredit = frankedCreditRow.Value.values[0]
                frankedCredit = frankedCredit.replace("$","")
                print('Franking Credit - ',frankedCredit)
                return
    except:
        print("Franking Credit - ")        
       
DOCUMENTS_PATH = "../results"
dividendDF = pd.DataFrame(columns=['Number of Securities','Franked Amount','Unfranked Amount','Total Payment','Franking Credit'],index = None)
# df.to_csv(r'out.csv')
for documents in os.listdir(DOCUMENTS_PATH):
    print("\nContents of document - ", documents)
    print("----------------------------")
    FORM_DATA_PATH = DOCUMENTS_PATH + '/' + documents + '/Forms/'
    for forms in os.listdir(FORM_DATA_PATH):
        FORM_DATA = FORM_DATA_PATH + forms 
        data = pd.read_csv(FORM_DATA)
        getFrankedAmount(data)
        getUnfrankedAmount(data)
        getParticipatingShares(data)
        getTotalPayment(data)
        getFrankingCredit(data)
