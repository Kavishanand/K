k=['apple','banana','orange','pineapple']
 
for j,type in enumerate(k):
    if (j<=1):
        print(type)
    else:
        break


Alpha=['a','b','c','d','e','f','g','h','i','j','k','l']
for ind,alph in enumerate(Alpha):
    if(ind+1)%4==0:
      print(alph)
    else:    
      continue
