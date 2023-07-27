height=float(input('Your height in m:'))
weight=float(input('Your weight in kg:'))

def new(weight,height):
    BMI=(weight/height**2)
    print(BMI)
    return BMI

new(weight,height)