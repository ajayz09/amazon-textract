import os
import time
import csv
import pandas as pd

def formatdate(paymentDate):
    months = dict(january='01', february='02', march='03', april='04', may='05', june='06', july='07', august='08', september='09', october='10', november='11', december='12')
    paymentDateList = paymentDate.split()
    if (len(paymentDateList) != 1):
        day = paymentDateList[0]
        month = paymentDateList [1].lower()
        year = paymentDateList[2]
        month = months[month]
        date = year+'-'+month+'-'+day
        return date
    elif (len(paymentDateList) == 1):
        paymentDateList = paymentDate.split('/')
        day = paymentDateList[0]
        month = paymentDateList [1]
        year = paymentDateList[2]
        date = year+'-'+month+'-'+day
        return date
            

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
                if unfrankedAmount == 'Nil':
                    unfrankedAmount = 0.00
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

def getPaymentDate(df):
    DICTIONARY_PD = "../dictionary/payment-date"
    temp = open(DICTIONARY_PD,'r').read().split('\n')
    try:
        for i in temp:
            paymentDateRow = df[df['Key'].str.match(i)]
            if not paymentDateRow.empty:
                paymentDate = paymentDateRow.Value.values[0]
                if not paymentDate:
                    return False
                date = formatdate(paymentDate)    
                print('Payment Date - ',date)
                return True
    except:
        return False             

def getFrankingCreditsFromTable(df):
    DICTIONARY_FC = "../dictionary/franking-credits"
    temp = open(DICTIONARY_FC,'r').read().split('\n')
    try:
        for i in temp:
            # print("df.columns ",df.columns)
            if i in df.columns:
                frankedCredit = df[i].iloc[0]    
                frankedCredit = frankedCredit.replace("A$","")
                frankedCredit = frankedCredit.replace("$","")
                print('Franking Credit - ',frankedCredit)
                return True
    except:
        return False    

def getFrankedAmountFromTable(df):
    DICTIONARY_FA = "../dictionary/franked-amount"
    temp = open(DICTIONARY_FA,'r').read().split('\n')
    try:
        for i in temp:
            if i in df.columns:
                frankedAmount = df[i].iloc[0]    
                frankedAmount = frankedAmount.replace("A$","")
                frankedAmount = frankedAmount.replace("$","")
                print('Franked Amount - ',frankedAmount)
                return True
    except:
        return False        

def getUnfrankedAmountFromTable(df):
    DICTIONARY_UFA = "../dictionary/unfranked-amount"
    temp = open(DICTIONARY_UFA,'r').read().split('\n')
    try:
        for i in temp:
            if i in df.columns:
                unfrankedAmount = df[i].iloc[0]    
                unfrankedAmount = unfrankedAmount.replace("A$","")
                unfrankedAmount = unfrankedAmount.replace("$","")
                if unfrankedAmount == 'Nil':
                    unfrankedAmount = 0.00
                print('Unfranked Amount - ',unfrankedAmount)
                return True
    except:
        return False

def getTotalPaymentFromTable(df):
    DICTIONARY_TP = "../dictionary/total-payment"
    temp = open(DICTIONARY_TP,'r').read().split('\n')
    try:
        for i in temp:
            if i in df.columns:
                totalPayment = df[i].iloc[0]    
                totalPayment = totalPayment.replace("A$","")
                totalPayment = totalPayment.replace("$","")
                print('Total Payment - ',totalPayment)
                return True
    except:
        return False                       
       
def getParticipatingSharesFromTable(df):
    DICTIONARY_PS = "../dictionary/participating-shares"
    temp = open(DICTIONARY_PS,'r').read().split('\n')
    try:
        for i in temp:
            if i in df.columns:
                participatingShares = df[i].iloc[0]    
                participatingShares = participatingShares.replace("A$","")
                participatingShares = participatingShares.replace("$","")
                print('Participating Shares - ',participatingShares)
                return True
    except:
        return False

# def getPaymentDate(textDocument):
#     for line in open(textDocument):
#         # for k in keywords:
#         if 'Payment Date' in line:
#             print(line)

def getPaymentDateFromText(textDocument):
    DICTIONARY_PD = "../dictionary/payment-date"
    temp = open(DICTIONARY_PD,'r').read().split('\n')
    flag = False
    for line in open(textDocument):
        if flag == True:
            date = formatdate(line)
            if date:
                print ('Payment Date - ',date)
                return True
        for k in temp:
            if k in line:
                flag = True
    return False            
                


DOCUMENTS_PATH = "../results"
dividendDF = pd.DataFrame(columns=['Number of Securities','Franked Amount','Unfranked Amount','Total Payment','Franking Credit'],index = None)
gotFrankedAmount = False
gotUnfrankedAmount = False
gotParticipatingShares = False
gotTotalPayment = False
gotFrankingCredits = False
gotPaymentDate = False

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
        gotPaymentDate = getPaymentDate(data)

    TABLE_DATA_PATH = DOCUMENTS_PATH + '/' + documents + '/Tables/'
    for tables in os.listdir(TABLE_DATA_PATH):
        TABLE_DATA = TABLE_DATA_PATH + tables 
        dataTable = pd.read_csv(TABLE_DATA,skiprows=1,index_col=False)
        if not gotFrankingCredits:
            getFrankingCreditsFromTable(dataTable)
        if not gotFrankedAmount:
            getFrankedAmountFromTable(dataTable) 
        if not gotUnfrankedAmount:
            getUnfrankedAmountFromTable(dataTable)
        if not gotTotalPayment:
            getTotalPaymentFromTable(dataTable)   
        if not gotParticipatingShares:
            getParticipatingSharesFromTable(dataTable) 

    TEXT_DATA_PATH = DOCUMENTS_PATH + '/' + documents + '/Text/'  
    for text in os.listdir(TEXT_DATA_PATH):
        TEXT_DATA = TEXT_DATA_PATH + text   
        if not gotPaymentDate:
            gotPaymentDate = getPaymentDateFromText(TEXT_DATA)             