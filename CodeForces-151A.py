n,k,l,c,d,p,nl,np = map(int,input().split())
total_drink = k*l
each_makes = total_drink/nl
total_slices = c*d
each_salt = p/np
need = min(each_makes,total_slices,each_salt)/n
print(int(need))

