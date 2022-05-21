from optparse import Values


key=[]
value=[]
for i in range(97,123):
    keys=chr(i)
    Values=i
    key.append(keys)
    value.append(Values)
dictionary=dict(zip(key,value))
print(dictionary)  