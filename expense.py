import os
import csv
from budget import getExpenseList,calculateSaved,getBudget,getSaved
from wallet import addtoWallet,getWallet
from budget import updateSaved
def submitExpenses(username,extraadded,extraminus):
    saved=getSaved(username)
    if saved==0:
        saved=calculateSaved(username)
    saved=saved+extraadded
    saved=saved-extraminus
    if saved<0:
        walletVal=float(getWallet(username)or 0)
        wallet=walletVal+saved
        addtoWallet(username,wallet)
        saved=0
    updateSaved(username,saved)
    return saved

