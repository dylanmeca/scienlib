import math

class basic:

      def __init__(self):
         #print ("Hello World")
         return

      def velocity(self,d,t):
         self.d = d
         self.t = t
         return d / t

      def divider(self,n,c):
         self.n = n
         self.c = c
         residue = n % c
         if residue == 0:
             return True
         else:
             return False

      def average(self,l):
         self.l = l
         sum = 0
         for element in l:
             sum += element

         average = sum / len (l)
         return average


class fisic:

      def __init__(self):
             return
   
      def sigmoid(self,x):
          self.x = x
          return 1/(1 + math.exp(-x))


      

       
