from database import supabase
from budget import getSaved, updateSaved, calculateSaved
def addwishlist(username,name,price,priority):
    supabase.table('wishlist').insert({'username': username,'item_name': name,'price': price,'priority': priority
    }).execute()
def getWishList(username):
    result=supabase.table('wishlist').select('*').eq('username', username).execute()
    wishlist=[]
    for row in result.data:
        wishlist.append([row['item_name'],row['price'],row['priority']])
    return wishlist
def updatePriority(username,name,price,priority):
    supabase.table('wishlist').update({'priority': priority
    }).eq('username',username).eq('item_name',name).execute()
def removeItem(username,name):
    supabase.table('wishlist').delete().eq('username',username).eq('item_name',name).execute()
def checkandUpdate(username):
    saved=getSaved(username)
    if saved==0:
        return
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