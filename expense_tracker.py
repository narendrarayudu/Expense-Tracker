from expense import Expense
from typing import List
from datetime import date, timedelta
import calendar

def main():
  print("Expense Tracker Running Succesfully")
  Income=1000

  expenses_filepath="expenses.csv"
 # expense= get_user_expense()
  
  #save_expense_to_file(expense,expenses_filepath)
  summarize_expense(expenses_filepath,Income)
  

def get_user_expense():
  print("Getting User Expense")
  expense_name=input("Expense Name: ")
  expense_amount=float(input("Expense Amount: "))
  print(f"You've entered {expense_name},{expense_amount}")

  expense_categories=[
    "Salary",
    "Business",
    "Food",
    "Rent",
    "Travel"
  ]
  
  while True:
      print("Select a Category: ")
      for i, category_name in enumerate(expense_categories):
        print(f"{i+1}. {category_name}")
      
      value_range=f"[1-{len(expense_categories)}]"
      selected_index=int(input(f"Enter a category name {value_range}: "))-1
      if selected_index in range(len(expense_categories)):
        selected_category=expense_categories[selected_index]
        new_expense=Expense(name=expense_name,category=selected_category,amount=expense_amount)
        return new_expense
      else:
        print("Invalid.Please Enter Valid Category")
  
def save_expense_to_file(expense:Expense,expenses_filepath):
  print(f"Saving Expense: {expense} to {expenses_filepath} ")
  with open(expenses_filepath,"a") as f:
    f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expense(expenses_filepath,Income):
  print("Sumarize User Expense")
  expenses: list[Expense] = []
  with open(expenses_filepath,"r") as f:
    lines=f.readlines()
    for line in lines:
      stripped_line=line.strip()
      expense_name,expense_amount,expense_category=line.strip().split(",")
      line_expense= Expense(name= expense_name,amount=float(expense_amount),category=expense_category) 
      expenses.append(line_expense)
  amount_by_category={}
  for expense in expenses:
    key = expense.category
    if key in amount_by_category:
      amount_by_category[key] += expense.amount
    else:
      amount_by_category[key] = expense.amount
  print("Expenses By Category")
  for key,amount in amount_by_category.items():
    print(f"{key}: ${amount: .2f}")

  total_spent= sum([x.amount for x in expenses])
  print(f"You've spent ${total_spent:.2f} this month!")
  print(f"Income per month: ${Income}")
  remaining_budget= Income - total_spent
  print(f"Budget Remaining ${remaining_budget: .2f} this month")

 
  today = date.today()
  year = today.year
  month = today.month
  day = today.day

  _, last_day = calendar.monthrange(year, month)

  remaining_days_count = last_day - day

  print("Remaining days in this month:", remaining_days_count)

  daily_budget= remaining_budget/ remaining_days_count
  print(f"Budget Per Day : ${daily_budget: .2f}")

if __name__=="__main__":
  main()