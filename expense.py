from database import supabase
from budget import calculateSaved,getBudget,getSaved,updateSaved
from wallet import addtoWallet,getWallet
def submitExpenses(username,extraadded,extraminus):
    saved=getSaved(username)
    if saved==0:
        saved=calculateSaved(username)
    saved=saved+extraadded
    saved=saved-extraminus
    if saved<0:
        walletVal=float(getWallet(username) or 0)
        newWallet=walletVal+saved
        supabase.table('wallet').update({'total_saved': newWallet}).eq('username',username).execute()
        saved=0
    updateSaved(username,saved)
    return saved
