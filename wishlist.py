import csv
import os
from budget import getSaved,updateSaved,calculateSaved
def addwishlist(username,name,price,priority):
    with open('Wishlist.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([username,name,price,priority])
def getWishList(username):
    wishlist=[]
    if os.path.exists('Wishlist.csv'):
        with open('Wishlist.csv','r',newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    wishlist.append([row[1],row[2],row[3]])
    return wishlist         
def updatePriority(username,name,price,priority):
    rows=[]
    if os.path.exists('Wishlist.csv'):
        with open('Wishlist.csv','r',newline='') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0]==username and row[1]==name:
                    rows.append([username,name,price,priority])
                else:
                    rows.append(row)
    with open ('Wishlist.csv','w',newline='') as file:
        writer=csv.writer(file)
        writer.writerows(rows)
def checkandUpdate(username):
    saved=getSaved(username)
    if saved==0:
        saved=calculateSaved(username)
    wishlist=getWishList(username)
    if len(wishlist)==0:
        return
    wishlist.sort(key=lambda x:int(x[2]))
    firstitem=wishlist[0]
    firstprice=float(firstitem[1])
    if saved>=firstprice:
        saved=saved-firstprice
        removeItem(username,wishlist[0][0])
        updateSaved(username,saved)
def removeItem(username,name):
    rows=[]
    if os.path.exists('Wishlist.csv'):
        with open('Wishlist.csv','r',newline='') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0]==username and row[1]==name:
                    pass
                else:
                    rows.append(row)
    with open('Wishlist.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)