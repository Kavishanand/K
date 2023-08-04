from pprint import pp
details=[{"Name":"Siva",
          "Email":"siva@gmail.com",
          "password":"siva",
          "Hobbies":["games","utube","gardening"],
          "Friend list":["Ram","subhash","robin"]
          },
          {"Name":"Krishna",
           "Email":"krishna@gmail.com",
           "password":"krishna",
           "Hobbies":["pubg","mobile","eating"],
           "Friend list":["abino","kavish","suresh"],
           },
           {"Name":"ben",
            "Email":"ben@gmail.com",
            "password":"ben",
            "Hobbies":["playing","mobile","eating"],
            "Friend list":["suresh","kavish","pradesh"],
            }]


email=input("Enter a Email: ")
pwrd=input("Enter a password: ")


for d in details:
    pas=d["password"]
    em=d["Email"]
    hob=d["Hobbies"]
    frd=d["Friend list"]
    # print(d)
    if email==em and pwrd==pas:
        d["loggedIn"]=True
        print(hob,frd)
    else:
        d["loggedIn"]=False
print(details)
pp(details)
        
