import math

class basic:

      def __init__(self):
         #print ("Hello World")
         return

      def velocity(self,d,t):
         return d / t

      def divider(self,n,c):
         residue = n % c
         if residue == 0:
             return True
         else:
             return False

      def average(self,n):
          sum = 0
          for element in n:
              sum += element

          average = sum / len(n)
          return average
          
class fisic:

      def __init__(self):
             return
   
      def sigmoid(self,x):
          self.x = x
          return 1/(1 + math.exp(-x))


      

       
