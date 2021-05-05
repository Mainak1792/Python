def insertionsort(seq):
  for slice in range(len(seq)): #iterate_the_positions
    pos=slice
    while pos>0 and seq[pos]<seq[pos-1]: #to_Check_whether_the_position_is_lower_than_its_left_element
      (seq[pos],seq[pos-1])=(seq[pos-1],seq[pos]) #swap_and_send_the_element_to_left
      pos=pos-1
#complexity=O(n^2)
