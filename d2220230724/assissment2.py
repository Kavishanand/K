monthly_gold_rate=[{"month":"jan",
                    "gold_rate":1500},
                    {"month":"feb",
                     "gold_rate":2000},
                     {"month":"mar",
                      "gold_rate":1000}]

a=0

for month in monthly_gold_rate:
    #print(month)
    mon=month["month"]
    rate=month["gold_rate"]
    # print(per_month)
    if rate>a:
        a=rate
    


print("max=",a,mon)
    #elif mini_month>mini:
        #mini=mini_months
    #print(mini)



     

