"""Independent literal controls supporting the explicit all-K staircase proof.
No author program is imported; general results use the accompanying inductions.
"""
from pathlib import Path
from collections import Counter
import json,random,hashlib
R=Path('/workspace/shared/langton');P=R/'cut_order_obstruction_2026-10-23/cut_order_minimal_transport_obstruction.md'
H=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word']
F={(H*2)[j:j+10]for j in range(104)};assert len(F)==84
union={'RRRLLRLLRLR','LLRLRLLRRLL','RRRRLRLLRLL','RRRLRRRRLRL','RRRLRRRRLRR','LRRLRRRRLRR'}
assert all(('RL'*6)[j:j+10]not in F and('RL'*6)[j:j+11]not in union for j in(0,1))
def eps(z):return 1 if(int(z.real+z.imag)%2)else-1
def margins(B):
 x=Counter();y=Counter()
 for z in B:x[int(z.real)]+=(-1)**int(z.imag);y[int(z.imag)]+=(-1)**int(z.real)
 assert all(v==0 for v in[*x.values(),*y.values()])
def mixed(A):
 d=Counter()
 for z in A:
  for v,s in((0,1),(1,-1),(1j,-1),(1+1j,1)):d[z+v]+=s
 return{z:v for z,v in d.items()if v}
for t in range(-20,21):
 f=lambda k:int(k<=1)
 assert 2*f(t)-f(t-1)-f(t+1)==(1 if t==1 else-1 if t==2 else 0)
steps=intervals=0;last=set()
for k in range(25):
 a=-2*k-1;b=2*k+1;c=-2*k-2
 height={complex(x,y)for y in range(a,b+1)for x in range(c,y+2)}
 assert last<=height;last=height
 delta=mixed(height);assert all(v==eps(z)for z,v in delta.items())
 board=set(delta);formula={complex(c,a),complex(a+2,a),complex(c,b+1),complex(b+2,b+1)}|{complex(n+d,n)for n in range(a+1,b+1)for d in(1,2)}
 assert board==formula and len(board)==8*k+8;margins(board)
 initial=board.copy();p=0j;h=1j;poses=[p-h/2];reads=[]
 for t in range(4*k+6):
  want=t%2==1;assert(p in board)==want and p==complex((t+1)//2,t//2)
  reads.append(p);board.symmetric_difference_update([p]);h*=1j if want else-1j;p+=h;poses.append(p-h/2);steps+=1
 assert len(set(reads))==len(reads)
 for s in range(len(reads)+1):
  for t in range(s+1,len(reads)+1):
   changed=reads[s:t];d=poses[t]-poses[s]
   assert len(changed)==2*max(abs(d.real),abs(d.imag))
   # Every signed occupation change is -1; at most two per axial line.
   rows=Counter();cols=Counter()
   for z in changed:
    sign=1 if z not in initial else-1
    assert sign*eps(z)==-1
    rows[int(z.imag)]+=1;cols[int(z.real)]+=1
   assert max([*rows.values(),*cols.values()])<=2
   assert all(n==min(n%4,4-n%4)for n in[*rows.values(),*cols.values()]);intervals+=1
rng=random.Random(231026);completions=[]
for case in range(32):
 initial={complex(x,y)for x in range(-4,5)for y in range(-4,5)if rng.randrange(3)==0};board=initial.copy();p=0j;h=1j;seen=set();Q=set();word=[]
 for t in range(200):
  black=p in board
  if p not in seen and black:Q.add(p)
  seen.add(p);word.append(black);board.symmetric_difference_update([p]);h*=1j if black else-1j;p+=h
 M=10+int(max(max(abs(z.real),abs(z.imag))for z in seen));complete=set()
 for i,z in enumerate(sorted(Q,key=lambda z:(z.real,z.imag))):
  x=M+4*i;y=M+4*i
  if (x-int(z.real))%2==0:x+=1
  if (y-int(z.imag))%2==0:y+=1
  rect={z,complex(x,z.imag),complex(z.real,y),complex(x,y)}
  assert not complete&rect and not(rect-{z})&seen;complete|=rect
 assert complete&seen==Q and len(complete)==4*len(Q);margins(complete)
 p=0j;h=1j
 for black in word:
  assert(p in complete)==black;complete.symmetric_difference_update([p]);h*=1j if black else-1j;p+=h
 completions.append(len(Q))
out={'status':'PASS literal controls plus separately reviewed all-parameter inductions','finite_K_cases':25,'literal_staircase_reads':steps,'all_subintervals':intervals,'general_word_completion_controls':len(completions),'required_black_counts':completions,'source_sha256':hashlib.sha256(P.read_bytes()).hexdigest(),'scope':'Infinite-support live staircase and arbitrarily long finite-fuel prefixes only; no infinite finite-seed counterexample, capture classification or mass-sensitive obstruction.'}
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
