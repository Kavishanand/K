days=["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
totaldays=30
mon=[]
tues=[]
wed=[]
thurs=[]
fri=[]
sat=[]
sun=[]
j=7
for i in range(1,30,+1):
    if (i%7==0):
        sun.append(i)
        # print(i)
    if (i%j==6):
        sat.append(i)
        # print(i)
    if (i%j==5):
        fri.append(i)
        # print(i)
    if (i%j==4):
        thurs.append(i)
        # print(i)
    if (i%j==3):
        wed.append(i)
        # print(i)
    if (i%j==2):
        tues.append(i)
        # print(i)
    if (i%j==1):
        mon.append(i)
        # print(i)
    

    
print("monday",mon)
print("tuesday",tues)
print("wednesday",wed)
print("thursday",thurs)
print("fridya",fri)
print("saturday",sat)
print("sunday",sun)