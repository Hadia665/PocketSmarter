import streamlit as st
from auth import signup , login
from budget import setBudget,getBudget,getExpenseList,addExpense,getexpense,calculateSaved,getSaved,updateSaved
from wallet import addtoWallet,getWallet
from wishlist import addwishlist,getWishList,updatePriority,checkandUpdate,removeItem
from expense import submitExpenses
from prediction import predictSpending,predictWishList,predictSpendingGraph
import matplotlib.pyplot as plt
from datetime import date,datetime
from database import supabase
st.set_page_config(page_title="Pocket Smarter", layout="wide")
st.markdown("""
<style>.stApp {background-color: #F8F9FA;}
h1, h2, h3 {color: #2C3E50;}
.stButton>button {
    background-color: #6C9BCF;
    color: white;
    border-radius: 12px;
    padding: 10px 18px;
    border: none;
    transition: 0.3s;
    font-weight:500;
}
.stButton>button:hover {
    transform: scale(1.05);
    background-color:#5B8ABE;
}
.card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    transition: 0.3s;
}
.card:hover {
    transform: translateY(-5px);
}
input, .stTextInput>div>div>input {
    border-radius: 10px !important;
}
[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 12px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
}
</style> """, unsafe_allow_html=True)
st.set_page_config(
    page_title="PocketSmarter",
    page_icon="logo.png",
    layout="wide"
)
if 'username' not in st.session_state:
    if st.session_state.get('show_auth')!=True:
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            subcol1, subcol2 = st.columns([1, 3])
            with subcol1:
                st.image("logo.png", width=70)
            with subcol2:
                st.markdown("""
                    <h1 style='color:#2C3E50; font-size:48px; margin:0; padding-top:5px;'>PocketSmarter</h1>
                """, unsafe_allow_html=True)
            st.markdown("""
                    <p style='color:#7F8C8D; font-size:20px; text-align:center;'>Smart Money Management for Students</p>
            """, unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.markdown("""
            <div style='background:white; padding:20px; border-radius:12px; 
            box-shadow:0 2px 8px rgba(0,0,0,0.08); text-align:center;'>
                <b>Track Expenses</b>
                <p style='color:gray; font-size:13px;'>Monitor every penny</p>
            </div>
            """, unsafe_allow_html=True)
        with col2:
            st.markdown("""
            <div style='background:white; padding:20px; border-radius:12px;
            box-shadow:0 2px 8px rgba(0,0,0,0.08); text-align:center;'>
                <b>Smart Savings</b>
                <p style='color:gray; font-size:13px;'>Auto savings wallet</p>
             </div>
            """, unsafe_allow_html=True)
        with col3:
            st.markdown("""
            <div style='background:white; padding:20px; border-radius:12px;
            box-shadow:0 2px 8px rgba(0,0,0,0.08); text-align:center;'>
                <b>Wish List</b>
                <p style='color:gray; font-size:13px;'>Save for your goals</p>
            </div>
            """, unsafe_allow_html=True)
        with col4:
            st.markdown("""
            <div style='background:white; padding:20px; border-radius:12px;
            box-shadow:0 2px 8px rgba(0,0,0,0.08); text-align:center;'>
                <b>AI Predictions</b>
                <p style='color:gray; font-size:13px;'>ML powered insights</p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
        col1,col2,col3=st.columns([1,2,1])
        with col2:
            if st.button(" Login", use_container_width=True):
                st.session_state['show_auth']=True
                st.session_state['auth_tab']='login'
                st.rerun()
            if st.button(" Sign Up", use_container_width=True):
                st.session_state['show_auth']=True
                st.session_state['auth_tab']='signup'
                st.rerun()
    else:
        auth_tab=st.session_state.get('auth_tab','login')
        if auth_tab=='signup':
            st.markdown("## Sign Up")
            firstName=st.text_input("FirstName")
            lastName=st.text_input("LastName")
            Susername=st.text_input("UserName")
            Spassword=st.text_input("Password",type="password")
            Cpassword=st.text_input("ConfirmPassword",type="password")
            if st.button("SignUp"):
                result=signup(firstName,lastName,Susername,Spassword,Cpassword)
                if result=="Signup Successful!":
                    st.success("Account Created!Please Login.")
                    st.session_state['auth_tab']='login'
                    st.rerun()
                else:
                    st.error(result)
            if st.button("Already have account? Login"):
                st.session_state['auth_tab']='login'
                st.rerun()
        else:
            st.markdown("## Login")
            Lusername=st.text_input("Login UserName")
            Lpassword=st.text_input("Login Password",type="password")
            if st.button("Login"):
                result=login(Lusername,Lpassword)
                if result=="Login Successful":
                    st.session_state['username']=Lusername
                    st.rerun()
                else:
                    st.write(result)
elif 'username' in st.session_state:
    if st.session_state.get('page')=='setup':
        U=st.session_state['username']
        budget=getBudget(U)
        if budget:
            days=int(budget[0])
            if budget[2]:
                startDate=datetime.strptime(budget[2],'%Y-%m-%d').date()
                today=date.today()
                daysPassed=(today-startDate).days
                if daysPassed>=days:
                    st.session_state['expense_list']=[]
                    st.session_state['page']='expenses'
                    st.rerun()
        if st.button("← Back"):
            st.session_state['page']=None
            st.rerun()
        st.markdown('## Setup Budget')
        st.markdown("---")
        col1,col2=st.columns(2)
        with col1:
            existing = getBudget(U)
            if existing:
                TotalDays = st.text_input("Days", value="")
                TotalAmount = st.text_input("Total Amount", value="")
            else:
                existing=getBudget(U)
                if existing:
                    TotalDays = st.text_input("Days",values=existing[0])
                    TotalAmount = st.text_input("Total Amount",value=existing[1])
                else:
                    TotalDays=st.text_input("Days")
                    TotalAmount=st.text_input("Total Amount")
        if st.button("Save Budget"):
            setBudget(U,TotalDays,TotalAmount)
            st.success("Budget Saved!")
            st.session_state['budget_saved']=True
            st.rerun()
        st.markdown("---")
        st.markdown("### Fixed Expenses")
        if 'expense_list' not in st.session_state:
            st.session_state['expense_list']=getExpenseList(U)
        col1,col2=st.columns(2)
        with col1:
            FixedExpense=st.text_input("Expense Name")
        with col2:
            Amount=st.text_input("Amount")
        if st.button("Add Expense"):
            st.session_state['expense_list'].append([FixedExpense,Amount])
            addExpense(U,FixedExpense,Amount)
            st.rerun()
        if len(st.session_state['expense_list'])>0:
            st.markdown("### Fixed Expenses")
            col1,col2,col3=st.columns(3)
            with col1:
                st.markdown("**Expenses**")
            with col2:
                st.markdown("**Amount**")
            with col3:
                st.markdown("---")
            for exp in st.session_state['expense_list']:
                col1,col2,col3=st.columns(3)
                with col1:
                    st.write(exp[0])
                with col2:
                    st.write(f"Rs. {exp[1]}")
                with col3:
                    if st.button("delete", key="del_"+exp[0]):
                        st.session_state['expense_list'].remove(exp)
                        supabase.table('expenses').delete().eq('username', U).eq('expense_name', exp[0]).execute()
                        st.rerun()
            st.markdown("---")
            saved=calculateSaved(U)
            st.metric("Saved Wallet",f"Rs. {saved}")
        if st.button("Period Complete!"):
            st.session_state['expense_list']=[]
            st.session_state['page']='expenses'
            st.rerun()
    elif st.session_state.get('page')=='wishlist':
        if st.button("← Back"):
            st.session_state['page']=None
            st.rerun()
        st.markdown("## Wish List")
        st.markdown("---")
        U=st.session_state['username']
        checkandUpdate(U)
        col1,col2,col3=st.columns(3)
        with col1:
            itemName=st.text_input("Item Name")
        with col2:
            itemPrice=st.text_input("Item Price")
        with col3:
            priority=st.selectbox("Priority",[1,2,3,4,5])
        if st.button("Add Item"):
            addwishlist(U,itemName,itemPrice,priority)
            st.success("Added!")
            st.rerun()
        st.markdown("---")
        wallet=getWallet(U)
        st.metric("Wallet", f"Rs. {wallet}")
        st.markdown("---")
        st.markdown("### My Wishes")
        wishlist=getWishList(U)
        if len(wishlist)==0:
            st.info("No items yet add your first wish!")
        else:
            wishlist.sort(key=lambda x:int(x[2]))
            col1,col2,col3,col4,col5=st.columns(5)
            with col1:
                st.markdown("**Item**")
            with col2:
                st.markdown("**Price**")
            with col3:
                st.markdown("**Priority**")
            with col4:
                st.markdown("**Difference**")
            with col5:
                st.markdown("**Actions**")
            st.markdown("---")
            for item in wishlist:
                col1,col2,col3,col4,col5=st.columns(5)
                walletAmount=float(wallet or 0)
                itemPriceVal=float(item[1])
                diff=walletAmount-itemPriceVal
                with col1:
                    st.write(f"{item[0]}")
                with col2:
                    st.write(f"Rs.{item[1]}")
                with col3:
                    newPriority=st.selectbox("P",[1,2,3,4,5],
                                             index=int(item[2])-1,
                                             key="p"+item[0]
                                             )
                    if newPriority!=int(item[2]):
                        updatePriority(U,item[0],item[1],newPriority)
                        st.rerun()
                with col4:
                    if diff>=0:
                        st.success(f"Can buy!")
                        if st.button("Bought it!", key="buy_"+item[0]):
                            walletVal = float(getWallet(U) or 0)
                            newWallet = walletVal - float(item[1])
                            supabase.table('wallet').update({
                                'total_saved': newWallet
                            }).eq('username', U).execute()
                            removeItem(U, item[0])
                            st.success(f"Congrats! {item[0]} purchased!")
                            st.rerun()
                    else:
                        st.write(f"Rs. {abs(diff):.0f} needed")
                with col5:
                    if st.button("Delete",key="del_"+item[0]):
                        removeItem(U,item[0])
                        st.rerun()
    elif st.session_state.get('page')=='expenses':
        if st.button("← Back"):
            st.session_state['page']=None
            st.rerun()
        st.markdown("### Daily Expenses")
        st.markdown("---")
        U=st.session_state['username']
        expenses=getExpenseList(U)
        if len(expenses)==0:
            st.warning("No Fixed Expense found.Please setup first!")
        else:
            extraadded=0
            extraminus=0
            for exp in expenses:
                st.markdown(f"**{exp[0]}**  Rs. {exp[1]}")
                choice=st.radio("Status",["Complete","Extra","Saved"],key=exp[0])
                if choice=="Extra":
                    amount=st.number_input("How Much?",key="e_"+exp[0])
                    extraminus+=amount
                elif choice=="Saved":
                    amount=st.number_input("How much Saved?",key="b_"+exp[0])
                    extraadded+=amount
                st.markdown("---")
            if st.button("Submit"):
                result=submitExpenses(U,extraadded,extraminus)
                st.success(f"Saved Updated: Rs. {result}")
                st.rerun()
            st.markdown("---")
            if st.button("Move to Wallet"):
                saved = getSaved(U)
                addtoWallet(U, saved)
                updateSaved(U, 0)
                supabase.table('expenses').delete().eq('username', U).execute()
                st.session_state['expense_list'] = []
                st.session_state['page'] = 'setup'
                st.rerun()
    elif st.session_state.get('page')=='predictions':
        if st.button("← Back"):
            st.session_state['page']=None
            st.rerun()
        st.markdown("##  Predictions")
        st.markdown("---")
        U=st.session_state['username']
        tab1,tab2,tab3=st.tabs([
            " Spending Forecast",
            " Wishlist Timeline", 
            " Savings Analysis"
        ])
        with tab1:
            predicted=predictSpending(U)
            budget=getBudget(U)
            if budget:
                totalAmount=float(budget[1])
                col1,col2=st.columns(2)
                with col1:
                    st.metric("Predicted Spending",f"Rs. {predicted}")
                with col2:
                    st.metric("Your Budget",f"Rs. {totalAmount}")
                if predicted > totalAmount:
                    st.error("You may overspend this month!")
                else:
                    st.success(" Looking good — within budget!")
            fig=predictSpendingGraph(U)
            if fig:
                st.pyplot(fig)
            else:
                st.info("Add more expenses to see trend!")
        with tab2:
            itemName,days=predictWishList(U)
            if itemName is None:
                st.info("Add items to wishlist first!")
            elif days==0:
                st.success(f" {itemName} — You can afford it now!")
            elif days==-1:
                st.warning(f" {itemName} — Improve your saving rate!")
            else:
                st.info(f" {itemName} — {days} days to go!")
                wallet=getWallet(U)
                wishlist=getWishList(U)
                if wishlist:
                    wishlist.sort(key=lambda x: int(x[2]))
                    price=float(wishlist[0][1])
                    progress=min(wallet/price,1.0)
                    st.progress(progress)
                    st.write(f"Saved: Rs. {wallet} / Rs. {price}")
        with tab3:
            wallet=float(getWallet(U) or 0)
            budget=getBudget(U)
            if budget:
                totalAmount=float(budget[1])
                savingRate=(wallet/totalAmount*100) if totalAmount>0 else 0
                col1,col2,col3=st.columns(3)
                with col1:
                    saved=getSaved(U)
                    st.metric(" Current Saved",f"Rs. {saved}")
                with col2:
                    st.metric(" Saving Rate",f"{savingRate:.1f}%")
                with col3:
                    st.metric(" Total Wallet",f"Rs. {wallet}")
                st.markdown("---")
                if savingRate>30:
                    st.success(" Excellent saving rate!")
                elif savingRate>10:
                    st.warning(" Good — but can improve!")
                else:
                    st.error(" Low saving rate!")
    else:
        U=st.session_state['username']
        col1,col2=st.columns([3,1])
        with col1:
            st.markdown(f"### Welcome back,{U}!")
        with col2:
            if st.button("Logout"):
                st.session_state.clear()
                st.rerun()
        st.markdown("---")
        col1,col2=st.columns(2)
        with col1:
            saved=getSaved(U)
            st.metric("Saved Wallet",f"Rs.{saved}")
        with col2:
            wallet=getWallet(U)
            st.metric("Total Wallet",f"Rs. {wallet}")
        st.markdown("---")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            if st.button("Setup",use_container_width=True):
                st.session_state['page'] = 'setup'
                st.rerun()
        with col2:
            if st.button("Expenses",use_container_width=True):
                st.session_state['page'] = 'expenses'
                st.rerun()
        with col3:
            if st.button("Wishlist",use_container_width=True):
                st.session_state['page'] = 'wishlist'
                st.rerun()
        with col4:
            if st.button("Predictions",use_container_width=True):
                st.session_state['page'] = 'predictions'
                st.rerun()



