import csv
import os
from datetime import date
def setBudget(username,days,totalAmount):
    rows=[]
    updated=False
    if os.path.exists('budget.csv'):
        with open('budget.csv','r',newline='') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0]==username:
                    startDate=str(date.today())
                    rows.append([username,days,totalAmount,startDate])
                    updated=True
                else:
                    rows.append(row)
    if not updated:
        startDate=str(date.today())
        rows.append([username,days,totalAmount,startDate])
    with open ('budget.csv','w',newline='') as file:
        writer=csv.writer(file)
        writer.writerows(rows)
def getBudget(username):
    if not os.path.exists('budget.csv'):
        return None
    with open ('budget.csv','r',newline='') as file:
        reader=csv.reader(file)
        for row in reader:
            if row[0]==username:
                return row[1],row[2],row[3] if len(row)>3 else None
def addExpense(username,expenseName,expenseamount):
    with open('expense.csv','a',newline='') as file:
        writer=csv.writer(file)
        writer.writerow([username,expenseName,expenseamount])
def getexpense(username):
    totalexpense=0
    if os.path.exists('expense.csv'):
        with open('expense.csv','r',newline='') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0]==username:
                    totalexpense+=float(row[2])
    return totalexpense
def calculateSaved(username):
    budget = getBudget(username)
    if budget is None:
        return 0
    days, totalAmount,startDate = budget
    totalExpense = getexpense(username)
    saved = float(totalAmount) - totalExpense
    return saved
def getExpenseList(username):
    expenses=[]
    if os.path.exists('expense.csv'):
        with open('expense.csv','r',newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[0] == username:
                    expenses.append([row[1],row[2]])
    return expenses    
def updateSaved(username,amount):
    rows=[]
    updated=False
    if os.path.exists('saved.csv'):
        with open('saved.csv','r',newline='') as file:
            reader=csv.reader(file)
            for row in reader:
                if row[0]==username:
                    rows.append([username,amount])
                    updated=True
                else:
                    rows.append(row)
    if not updated:
        rows.append([username,amount])
    with open ('saved.csv','w',newline='') as file:
        writer=csv.writer(file)
        writer.writerows(rows)
def getSaved(username):
    if not os.path.exists('saved.csv'):
        return 0
    with open('saved.csv', 'r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == username:
                return float(row[1])
    return 0