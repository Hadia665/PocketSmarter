import hashlib
from database import supabase
from datetime import date
def setBudget(username,days,totalAmount):
    existing=supabase.table('budget').select('*').eq('username',username).execute()
    startDate=str(date.today())
    if existing.data:
        supabase.table('budget').update({
            'days':days,
            'total_amount':totalAmount,
            'start_date':startDate}).eq('username',username).execute()
    else:
        supabase.table('budget').insert({
            'username':username,
            'days':days,
            'total_amount':totalAmount,
            'start_date':startDate}).execute()
def getBudget(username):
    result=supabase.table('budget').select('*').eq('username',username).execute()
    if result.data:
        row=result.data[0]
        return row['days'],row['total_amount'],row['start_date']
    return None
def addExpense(username,expenseName,expenseamount):
    supabase.table('expenses').insert({
        'username':username,
        'expense_name':expenseName,
        'expense_amount':expenseamount
    }).execute()
def getexpense(username):
    result=supabase.table('expenses').select('expense_amount').eq('username',username).execute()
    total=0
    for row in result.data:
        total+=float(row['expense_amount'])
    return total
def calculateSaved(username):
    budget = getBudget(username)
    if budget is None:
        return 0
    days, totalAmount,startDate = budget
    totalExpense = getexpense(username)
    saved = float(totalAmount) - totalExpense
    return saved
def getExpenseList(username):
    result=supabase.table('expenses').select('*').eq('username',username).execute()
    expenses=[]
    for row in result.data:
        expenses.append([row['expense_name'],row['expense_amount']])
    return expenses    
def updateSaved(username,amount):
    existing=supabase.table('saved').select('*').eq('username',username).execute()
    if existing.data:
        supabase.table('saved').update({'amount': amount}).eq('username', username).execute()
    else:
        supabase.table('saved').insert({'username': username, 'amount': amount}).execute()
def getSaved(username):
    result = supabase.table('saved').select('amount').eq('username',username).execute()
    if result.data:
        return float(result.data[0]['amount'])
    return 0
