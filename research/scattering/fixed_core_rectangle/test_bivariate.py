"""Finite controls for the arithmetic implementation, not theorem coverage."""
import itertools,random,json
from bivariate import has_nonnegative_zero,no_point_collision,A,ZERO

def main():
 tests=0
 for a,b in itertools.product(range(-5,6),repeat=2):
  for c in range(-20,21):
   brute=any(a*u+b*v+c==0 for u in range(41) for v in range(41))
   assert has_nonnegative_zero((a,b,c))==brute,(a,b,c,brute)
   tests+=1
 rng=random.Random(271828);point_tests=0
 for _ in range(10000):
  p=tuple(tuple(rng.randrange(-4,5) for _ in range(3)) for _ in range(2));q=(ZERO,ZERO)
  brute=any(all(a*u+b*v+c==0 for a,b,c in p) for u in range(101) for v in range(101))
  try:result=not no_point_collision(p,q)
  except AssertionError:result=True
  assert result==brute,(p,result,brute)
  point_tests+=1
 # Negative controls at unbounded, non-sampled coordinates.
 for t in (10**6,10**60):
  assert has_nonnegative_zero((1,0,-t))
  try:no_point_collision(((1,0,-t),(0,1,-t)),q)
  except AssertionError:pass
  else:raise AssertionError('distant isolated intersection accepted')
 print(json.dumps(dict(scalar_tests=tests,point_tests=point_tests,distant_negative_controls=2,status='arithmetic controls passed')))
if __name__=='__main__':main()
