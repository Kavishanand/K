#dictionary to str
def calculate_electricity_bill():

    Electricity_bill={"consumer name":"kavish",
                    "eb reading":[1100,1200,1350,1650,2050]
                        }
    dic=[]
    tot=0
    

    reading=Electricity_bill["eb reading"]
    for i in range(1,len(reading)):
        unit=reading[i]-reading[i-1]
        month=i
    # print(f"month :{month}")

        if (unit<100):
            rate=0
            tot=tot+rate
        # print(f"units consumed :{unit}\nbill amount{rate}")
        elif (100 <=unit< 200):
            rate=unit*2
            tot=tot+rate
        # print(f"units consumed :{unit}\nbill amount{rate1}")
        elif (200 <=unit< 500):
            rate=unit*5
            tot=tot+rate
        # print(f"units consumed :{unit}\nbill amount{rate2}")
        elif (500 <=unit< 1000):
            rate=unit*10
            tot=tot+rate
        # print(f"units consumed :{unit}\nbill amount{rate3}")
        elif (unit>=1000):
            rate=unit*14
            tot=tot+rate
            #print(f"units consumed :{unit}\nbill amount{rate4}")
        appen={"month":month,"unit consumed":unit,"bill amount":rate}
        dic.append(appen)
    return dic       

a=calculate_electricity_bill()
file=open("/home/kavish/karka/karka.txt","w")
for k in a:
   # print(k)
        #print(k)
        
    #print(dic)
    #print(f"total amount:{tot}")

    file.write(f"month:{k['month']},\nunit consumed:{k['unit consumed']},\nbill amount{k['bill amount']}\n")

file.close
file=open("/home/kavish/karka/karka.txt","r")
print(file.read())

#dictionary to json








    







        