def wallis(m):
     pr=1
     for k in range(1,m+1):
          x=(4*k*k)/((4*k*k)-1)
          pr=pr*x
     return 2*x
   
  
def monte_carlo(m):
     total_no_of_points=0
     points_inside_circle=0
     for i in range (0,m):
          x=random.random()
          y=random.random()
          total_no_of_points+=1
          if ((x*x)+(y*y))<=1:
               points_inside_circle+=1
     return 4*((points_inside_circle)/(total_no_of_points))
 
