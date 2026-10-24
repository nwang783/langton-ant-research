"""All-count cylinder incidence relaxation for one prepared drift8 rail target.
SAT means a necessary integer flow only, not chronology or a front.
"""
import sys,pathlib,json,re,time
HERE=pathlib.Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'morphic_candidates'))
from smt_inflation_refinement import Z3
D=((0,1),(1,0),(0,-1),(-1,0))
def add(xs):return '(+ '+' '.join(xs)+')'if xs else'0'
def inp(x,y):return int(x%2==1 and y==1)
def outp(x,y):return int(y in(0,2) or(x%2==1 and y==3))
def solve(sector):
 lines=['(set-option :timeout 30000)'];edges=[];nodes=[(x,y,h)for x in range(8)for y in range(5)for h in range(4)if(x+y+h)%2==sector]
 for a in nodes:
  x,y,h=a
  for c in(1,-1):
   hh=(h+c)%4;dx,dy=D[hh];b=((x+dx)%8,y+dy,hh)
   if not 0<=b[1]<5:continue
   name=f'e{x}_{y}_{h}_{"R"if c==1 else"L"}'
   lines.extend([f'(declare-const {name} Int)',f'(assert (>= {name} 0))']);edges.append((name,a,b,c,dx))
 for a in nodes:lines.append(f'(assert (= {add([e[0]for e in edges if e[1]==a])} {add([e[0]for e in edges if e[2]==a])}))')
 for x in range(8):
  for y in range(5):
   lines.append(f'(assert (= {add([e[0]if e[3]==1 else f"(- {e[0]})"for e in edges if e[1][:2]==(x,y)])} {outp(x,y)-inp(x,y)}))')
 lines.append(f'(assert (= {add([e[0]if e[4]==1 else f"(- {e[0]})"for e in edges if e[4]])} 8))')
 z=Z3();z.run('\n'.join(lines));t=time.monotonic();ans=z.run('(check-sat)').strip();result=dict(sector=sector,status=ans,seconds=time.monotonic()-t)
 if ans=='sat':
  model=z.run('(get-value ('+' '.join(e[0]for e in edges)+'))');values={k:int(v)for k,v in re.findall(r'\((e\w+) (\d+)\)',model)};result['total_visits']=sum(values.values());result['positive_flow']={k:v for k,v in values.items()if v}
  lo=24;hi=result['total_visits'];queries=[];total=add([e[0]for e in edges])
  while lo<hi:
   mid=(lo+hi)//2;res=z.run(f'(push)\n(assert (<= {total} {mid}))\n(check-sat)').strip();queries.append([mid,res]);z.run('(pop)')
   if res=='sat':hi=mid
   elif res=='unsat':lo=mid+1
   else:break
  result['minimum_queries']=queries;result['minimum_bracket']=[lo,hi]
  if lo==hi:
   z.run(f'(assert (= {total} {lo}))');assert z.run('(check-sat)').strip()=='sat';model=z.run('(get-value ('+' '.join(e[0]for e in edges)+'))');values={k:int(v)for k,v in re.findall(r'\((e\w+) (\d+)\)',model)};result['minimum_flow']={k:v for k,v in values.items()if v}
 z.close();return result
if __name__=='__main__':
 out=dict(scope=__doc__,results=[solve(s)for s in(0,1)]);HERE.joinpath('mixed_rail_incidence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
