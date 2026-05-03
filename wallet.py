from database import supabase
def addtoWallet(username,amount):
    existing=supabase.table('wallet').select('*').eq('username', username).execute()
    if existing.data:
        currentTotal=float(existing.data[0]['total_saved'])
        newTotal=currentTotal+float(amount)
        supabase.table('wallet').update({'total_saved':newTotal}).eq('username',username).execute()
    else:
        supabase.table('wallet').insert({
            'username':username,
            'total_saved':amount
        }).execute()
def getWallet(username):
    result=supabase.table('wallet').select('total_saved').eq('username', username).execute()
    if result.data:
        return float(result.data[0]['total_saved'])
    return 0