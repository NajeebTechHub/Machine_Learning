
# Problem 1: Write a program that will give you in hand monthly salary after deduction on CTC - HRA(10%), DA(5%), PF(3%) and taxes deduction as below:
# Salary(Lakhs) : Tax(%)

# Below 5 : 0%
# 5-10 : 10%
# 10-20 : 20%
# aboove 20 : 30%

totalsalary = int(input('Enter your Salary in lakh : '))

deductsalary = totalsalary - (totalsalary*0.18)

if(totalsalary < 5):
  print('your salary is',deductsalary,'lakh')
elif(5 >= totalsalary < 10):
  print('your salary is',deductsalary - (totalsalary*0.10),'lakh')
elif(10 >= totalsalary < 20):
  print('your salary is',deductsalary - (totalsalary*0.20),'lakh')
elif(totalsalary >= 20):
  print('your salary is',deductsalary - (totalsalary*0.30),'lakh')