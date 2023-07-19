My_resume={
            "Name":"Kavish",
            "E_mail":"kavishanand20@gmail.com",
            "Mobile_no":7530066055,
            "Soft_skills":"confidence",
            "Hard_skills":"computer software knowledge",
            "Educational_qualification":[{"Qualification":"SSLC",
                                         "percentage":89,
                                         "passed out":2017},
                                         {"Qualification":"HSC",
                                          "percentage":78,
                                          "passed out":2019},
                                        {"Qualification":"Bsc.chemistry",
                                         "percentage":77,
                                         "passed out":2022}],
            "projects":"none",
            "Experiance":[{"company name":"cape start","role":"software devolper",
                          "duration":2.3},
                          {"company name":"zoho","role":"software devolper","duration":1},
                          {"company name":"TCS","role":"software devolper","duration":1}],
            "Hobbies":["playing games","movies","cooking"],
            "personal details":{
                    "Father_name":"Anand",
                    "Father_occupation":"driver",
                    "language_known":["Tamil","Engish"],
                    "DOB":22/2/2001,
                    "Gender":"male",
                    "Martial_status":"Single",
                    "Address":{ "door no":40/1,
                                "Street":"Raja pathai",
                                "city":"Nagercoil",
                                "pincode":629001}
            }
            }
    
print(My_resume["Hard_skills"])

for i in My_resume["Educational_qualification"]:
        Qualification=i["Qualification"]
        psd=i["passed out"]
        print(Qualification,psd)


print(My_resume["personal details"]["Address"]["city"])

print(My_resume["personal details"]["Address"]["city"])
        
        
        
    
        


