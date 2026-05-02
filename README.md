#  PocketSmart

> Smart money management for students — track, save, and predict your finances!

---

##  Features

- **Budget Setup** — Set your pocket money and fixed expenses for any period
- **Expense Tracking** — Daily tracking with Complete / Extra / Saved options
- **Smart Savings Wallet** — Automatically calculates and stores your savings
- **Wish List** — Add items with priority — get notified when you can afford them
- **AI Predictions** — ML-powered spending predictions and savings forecasts
- **Multi-user Support** — Secure login with hashed passwords

---

##  Tech Stack

| Layer | Technology |
|-------|-----------|
| Frontend | Streamlit |
| Backend | Python |
| ML Model | Scikit-learn (Linear Regression) |
| Database | CSV (local) / Supabase (cloud) |
| Auth | SHA-256 Password Hashing |

---

##  Project Structure

```
PocketSmart/
│
├── main.py          # Main app — UI & navigation
├── auth.py          # Login & Signup
├── budget.py        # Budget setup & calculations
├── expense.py       # Expense submission logic
├── wishlist.py      # Wishlist management
├── wallet.py        # Savings wallet
├── prediction.py    # ML predictions & graphs
│
└── data/
    ├── output.csv   # Users
    ├── budget.csv   # Budget data
    ├── expense.csv  # Fixed expenses
    ├── saved.csv    # Current saved amount
    ├── Wallet.csv   # Total wallet history
    └── Wishlist.csv # Wishlist items
```

---

##  How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/PocketSmart.git
cd PocketSmart
```

### 2. Install dependencies
```bash
pip install streamlit pandas scikit-learn matplotlib numpy
```

### 3. Run the app
```bash
streamlit run main.py
```

---

##  How It Works

```
1. Sign Up → Create your account
2. Setup   → Set budget, days & fixed expenses
3. Track   → Daily expense tracking
4. Save    → Period complete → savings go to wallet
5. Wish    → Add wishlist items — AI predicts when you can buy!
6. Predict → View spending trends & forecasts
```

---

##  AI Features

- **Spending Prediction** — Linear Regression predicts month-end spending
- **Wishlist Timeline** — Predicts how many days until you can afford each item
- **Saving Rate Analysis** — Tracks and evaluates your saving habits
- **Spending Trend Graph** — Visual representation of actual vs predicted spending

---

##  Developer

**Developed by:** Hadia Awan
**University:** FAST-NUCES  
**Semester:** 4th Semester  
**Department:** Computer Science  

---

## 🏆 Presented At

**Intra FAST Project Exhibition 2026**  
IEEE Student Branch — FAST-NUCES Chiniot-Faisalabad Campus  
Date: May 5, 2026

---

## 📸 Screenshots

*Coming soon*

---

## 📄 License

This project is for academic purposes.
