earth=int(input('please enter your current earth weight:'))
planet=int(input('I have information for the following planet:\n\t1.venus\t2.mars\t3.jupiter\n\t4.saturn\t5.uranus\t6.neptune\nwhich planet are you visiting?'))


if(planet==1):
    print(f"Your weight would {earth*0.78}pound on that planet")
if(planet==2):
    print(f"Your weight would {earth*0.39}pound on that planet")
if(planet==3):
    print(f"Your weight would {earth*2.65}pound on that planet")
if(planet==4):
    print(f"Your weight would {earth*1.17}pound on that planet")
if(planet==5):
    print(f"Your weight would {earth*1.05}pound on that planet")
if(planet==6):
    print(f"Your weight would {earth*1.23}pound on that planet")

