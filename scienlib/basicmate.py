def velocity(d,t):
       return d / t

def divider(n,c):
       residue = n % c
       if residue == 0:
             return True
       else:
             return False

def average(l):
       sum = 0
       for element in l:
             sum += element

       average = sum / len (l)
       return average
       
