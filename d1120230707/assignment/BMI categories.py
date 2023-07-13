import BMI_calculator
height=float(input('Your height in m: '))
weight=float(input('Your weight in kg: '))
cat=BMI_calculator.new(weight,height)
print(cat)

if(cat<18.5):
    print('BMI category:Under weight')
elif(cat>18.5) and (cat<24.9):
    print('BMI category:Normal weight')
elif(cat>25.0) and (cat<29.9):
    print('BMI category:Over weight')
elif(cat>30.0):
    print('BMI category:Obese')



