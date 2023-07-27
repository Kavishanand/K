


details=[
        {"name":"Kavish",
         "age":22,
        "place":"vadasery"
        },

        {"name":"Abino",
         "age":21,
         "place":"vadasery"
        },

        {"name":"Bharath",
         "age":22,
         "place":"vadasery"
        },

        {"name":"Pradesh",
         "age":20,
         "place":"vadasery"}
        ] 


for i in details:
        name=i["name"]
        age=i["age"]
        place=i["place"]
        print(f"i am {name},i am {age} years old,and im from {place}.")

for i in details:
        age=int(i["age"])
        if age>21:
                name=i["name"]
                place=i["place"]
                print(f"i am {name},and im from {place}.")
    





        

