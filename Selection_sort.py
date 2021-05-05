def selectionsor(l): 
  for start in range(0,len(l)): #scan_slices_from_l[0:len(l)]
    minpos=start #minimum_value_in_slice
    for i in range(start,len(l)):
      ifl[i]<l[minpos]:
        minpos=i
   (l[start],l[minpos])=(l[minpos],l[start])
