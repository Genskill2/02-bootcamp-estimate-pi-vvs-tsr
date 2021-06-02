import math
import unittest

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
    

    
    
    
    
    def wallis(m):
     pr=1
     for k in range(1,m+1):
          x=(4*k*k)/((4*k*k)-1)
          pr=pr*x
     return (2*x)
   
  
def monte_carlo(m):
     total_no_of_points=0
     points_inside_circle=0
     for i in range (0,m):
          x=random.random()
          y=random.random()
          total_no_of_points+=1
          if ((x*x)+(y*y))<=1:
               points_inside_circle+=1
     return (4*((points_inside_circle)/(total_no_of_points)))
     
     
     
if __name__ == "__main__":
    unittest.main()
 
