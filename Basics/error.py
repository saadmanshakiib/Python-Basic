def calculate(revenue,expense):
   try:
       if expense > revenue:
           return (expense - revenue) * 100 / revenue

       elif revenue > expense:
           return (revenue - expense) * 100 / revenue

   except ZeroDivisionError:
       return None

revenue = int(input("Enter Revenue : "))
expense = int(input("Enter Expense : "))

safe_margin = calculate(revenue,expense)
print(safe_margin)