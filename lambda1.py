l={1,2,3,4,5,6,7,8,9}
od=list(map(lambda x:x*3,l))
print(od)
odl=list(filter(lambda x:(x%3==0),l))
print(odl)