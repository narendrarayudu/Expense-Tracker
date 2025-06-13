## 💸 Expense Tracker

A simple command-line based Python application to track your expenses, categorize them, and give you daily/monthly budget insights.

### 📂 Project Structure

expense_tracker/
│

├── expense_tracker.py    # Defines the Expense class

├── expence.py            # Main application logic (code you provided)

├── expenses.csv          # CSV file where expense data is stored

└── README.md             # Project documentation

### 🚀 Features
Prompt user to input:

Expense name
Amount
Category (e.g., Food, Rent, Travel, etc.)
Save expense data to a .csv file

Categorize expenses and summarize by:

Total amount spent per category

Total monthly expense

Remaining monthly budget (based on fixed income)

Remaining days in the month

Daily spending budget for the rest of the month

### 🧾 Categories Supported

Salary

Business

Food

Rent

Travel

# expense.py

class Expense:

  def __init__(self,name,category,amount)->None:
  
    self.name=name
    
    self.category=category
    
    self.amount=amount
  
  def __repr__(self):
  
    return f"<Expense: {self.name},{self.category}, ${self.amount:.2f}>""
        

Follow the prompts to input your expenses.

# 📊 Output Sample

Expense Tracker Running Succesfully

Getting User Expense

Expense Name: Tea

Expense Amount: 20

You’ve entered Tea, 20.0

Select a Category:

1. Salary

2. Business

3. Food

4. Rent

5. Travel

Enter a category name [1-5]: 3

Saving Expense: <Expense name=Tea, amount=20.0, category=Food> to expenses.csv

Summarize User Expense

Expenses By Category

Food: $ 20.00

You’ve spent $20.00 this month!

Income per month: $1000

Budget Remaining $ 980.00 this month

Remaining days in this month: 17

Budget Per Day: $ 57.65

# Notes

Expenses are appended to expenses.csv – so keep it clean or clear it if needed.

Income is currently hardcoded (e.g., $1000). You can modify it in the script or enhance by prompting the user for dynamic input.

# 📌 Future Improvements

Add date/time to each expense

Add expense deletion or editing

Visualizations using matplotlib or seaborn

GUI or Web version (Flask or Django)

### 🧑‍💻 Author
Narendra Rayudu
GitHub: narendrarayudu
