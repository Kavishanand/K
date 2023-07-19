item_list=[{'name':'Apple','category':'fruit'},
           {'name':'banana','category':'fruit'},
           {'name':'carrot','category':'vegetable'},
           {'name':'broccoli','category':'vegetable'}]
fruits=[]
vegetables=[]

for item in item_list:
    if item['category']=='fruit':
        fruits.append(item['name'])
        print("name":fruits)
        
    elif item['category']=='vegetable':
        vegetables.append(item['name'])
        print("name":vegetables)

    
