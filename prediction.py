import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from database import supabase
from budget import getSaved,getBudget,getexpense
from wishlist import getWishList
def predictSpending(username):
    result=supabase.table('expenses').select('expense_amount').eq('username', username).execute()
    amounts=[float(row['expense_amount']) for row in result.data]
    if len(amounts)<2:
        return sum(amounts)
    cumulative=[]
    total=0
    for amt in amounts:
        total+=amt
        cumulative.append(total)
    X=np.array(range(1,len(cumulative)+1)).reshape(-1,1)
    Y=np.array(cumulative)
    model=LinearRegression()
    model.fit(X,Y)
    prediction=model.predict([[30]])
    return round(prediction[0],2)
def predictWishList(username):
    wishlist=getWishList(username)
    if len(wishlist)==0:
        return None,0
    wishlist.sort(key=lambda x:int(x[2]))
    firstitem=wishlist[0]
    itemName=firstitem[0]
    itemPrice=float(firstitem[1])
    saved=getSaved(username)
    remaining=itemPrice-saved
    if remaining<=0:
        return itemName,0
    budget=getBudget(username)
    if budget is None:
        return itemName,0
    days=int(budget[0])
    totalAmount=float(budget[1])
    totalExpense=getexpense(username)
    dailySaving=(totalAmount-totalExpense)/days
    if dailySaving<=0:
        return itemName,-1
    daysNeeded=round(remaining/dailySaving)
    return itemName,daysNeeded
def predictSpendingGraph(username):
    result=supabase.table('expenses').select('expense_amount').eq('username', username).execute()
    amounts=[float(row['expense_amount']) for row in result.data]
    if len(amounts)<2:
        return None
    cumulative=[]
    total=0
    for amt in amounts:
        total+=amt
        cumulative.append(total)
    X=np.array(range(1,len(cumulative)+1)).reshape(-1,1)
    Y=np.array(cumulative)
    model=LinearRegression()
    model.fit(X,Y)
    futureDays=list(range(1,31))
    predictions=model.predict(np.array(futureDays).reshape(-1,1))
    fig,ax=plt.subplots(figsize=(10,4))
    ax.plot(range(1,len(cumulative)+1),cumulative,'b-o',label='Actual Spending',linewidth=2)
    ax.plot(futureDays,predictions,'r--',label='Predicted',linewidth=2)
    ax.set_xlabel('Days')
    ax.set_ylabel('Amount')
    ax.set_title('Spending Trend & Prediction')
    ax.legend()
    ax.grid(True, alpha=0.3)
    return fig
