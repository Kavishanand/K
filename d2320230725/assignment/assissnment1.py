gold_rate=[{"month":"jan",
            "rate":1500,
            "jewel list":[{"name":"chain",
                           "making cost":12
                           },
                           {"name":"ring",
                            "making cost":14
                            }]
            },
            {"month":"feb",
             "rate":2000,
             "jewel list":[{"name":"chain",
                           "making cost":10
                           },
                           {"name":"ring",
                           "making cost":11
                           }]
            },
            {"month":"mar",
            "rate":1000,
            "jewel list":[{"name":"chain",
                           "making cost":11
                           },
                           {"name":"ring",
                            "making cost":14
                            }]
            }]

for flower in gold_rate:
    #print(flower)
    month=flower["month"]
    rate=flower["rate"]
    list=flower["jewel list"]
    #print(rate)
    
    for l in list:
        name=l["name"]
        cost=l["making cost"]
        gold_maker=rate*cost/100
        print(gold_maker)

