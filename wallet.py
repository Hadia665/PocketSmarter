import csv
import os
def addtoWallet(username,amount):
    rows=[]
    updated=False
    if os.path.exists('Wallet.csv'):
        with open('Wallet.csv','r',newline='') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0]==username:
                    newTotal=float(row[1])+float(amount)
                    rows.append([username,newTotal])
                    updated=True
                else:
                    rows.append(row)
    if not updated:
        rows.append([username,amount])
    with open ('Wallet.csv','w',newline='') as file:
        writer=csv.writer(file)
        writer.writerows(rows) 
def getWallet(username):
    if not os.path.exists('Wallet.csv'):
        return 0
    with open ('Wallet.csv','r',newline='') as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0]==username:
                moneySaved=row[1]
                return moneySaved
