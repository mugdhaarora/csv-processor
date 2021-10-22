import os.path
import unittest
import pandas as pd
dirname = os.path.dirname(__file__)

def findFile():
   file_name = os.path.join(dirname, 'data/Combined.csv')
   return os.path.exists(file_name)

def validateData():
   file_name = os.path.join(dirname, 'data/Combined.csv')
   df = pd.read_csv(file_name, sep=',')
   return len(df.columns)


class SimpleTest(unittest.TestCase):
   def testadd1(self):
      self.assertEquals(findFile(),1)
   
   def testadd2(self):
      self.assertEquals(validateData(),2)
      
if __name__ == '__main__':
   unittest.main()

