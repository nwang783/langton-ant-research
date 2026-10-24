"""Exact complete-history clock synthesis for ONE supplied 128-read flow.
This tests its ordering, not all flows or all prepared fronts.
"""
from pathlib import Path
import sys,json,re,time
HERE=Path(__file__).parent
sys.path.insert(0,str(HERE.parent/'morphic_candidates'))
from smt_inflation_refinement import Z3
D=((0,1),(1,0),(0,-1),(-1,0));P=128;W=8;H=5
A=lambda xs:'(and '+' '.join(xs)+')'
S=lambda xs:'(+ '+' '.join(xs)+')'if xs else'0'
E=lambda a,b:f'(= {a} {b})'
NOT=lambda s:f'(not {s})'
flow=json.loads(HERE.joinpath('mixed_rail_flow_minimum.json').read_text())[0]['flow']
counts={tuple(a)+(c,):n for a,c,n in flow};N={};turns={};heads={}
for x in range(W):
 for y in range(H):
  n=sum(v for k,v in counts.items()if k[:2]==(x,y));N[x,y]=n
  turns[x,y]=[(-1 if (j+int(y==1 and x%2))%2 else 1) for j in range(n)]
  heads[x,y]=[(x+y)%2,(x+y)%2+2]
assert sum(N.values())==P
lines=['(set-option :timeout 120000)']
def add(s):lines.append('(assert '+s+')')
def hp(x,y,j,h):
 a=heads[x,y]
 if h==a[0]:return f'(not b{x}_{y}_{j})'
 if h==a[1]:return f'b{x}_{y}_{j}'
 return 'false'
def port(x,y,j,h,out):return hp(x,y,j,(h-turns[x,y][j])%4) if out else hp(x,y,j,h)
def pref(x,y,j,h,out):return f'{"o"if out else"i"}{x}_{y}_{j}_{h}'
for x in range(W):
 for y in range(H):
  for j in range(N[x,y]):
   lines.append(f'(declare-const b{x}_{y}_{j} Bool)');lines.append(f'(declare-const t{x}_{y}_{j} Real)')
   if j:add(f'(>= t{x}_{y}_{j} (+ t{x}_{y}_{j-1} 4))')
   for h in range(4):
    for out in(0,1):lines.append(f'(define-fun {pref(x,y,j,h,out)} () Int {S([f"(ite {port(x,y,k,h,out)} 1 0)"for k in range(j)])})')
  for h in heads[x,y]:
   for c in(1,-1):add(E(S([f'(ite {hp(x,y,j,h)} 1 0)'for j in range(N[x,y])if turns[x,y][j]==c]),str(counts.get((x,y,h,c),0))))
for x in range(W):
 for y in range(H):
  for j in range(N[x,y]):
   for h in range(4):
    dx,dy=D[h];X,Y=x+dx,y+dy;xx=X%W;z=X//W;source=port(x,y,j,h,1)
    if source=='false':continue
    if not 0<=Y<H:add(NOT(source));continue
    for k in range(N[xx,Y]):
     target=port(xx,Y,k,h,0)
     if target=='false':continue
     guard=A([source,target,E(pref(x,y,j,h,1),pref(xx,Y,k,h,0))])
     add(f'(=> {guard} (= (+ t{xx}_{Y}_{k} {z*P}) (+ t{x}_{y}_{j} 1)))')
add('(= t0_0_0 0)')
smt='\n'.join(lines);HERE.joinpath('mixed_rail_flow_clock.smt2').write_text(smt+'\n(check-sat)\n')
z=Z3();msg=z.run(smt);assert not msg.strip(),msg;st=time.monotonic();ans=z.run('(check-sat)').strip();out=dict(status=ans,seconds=time.monotonic()-st,period=P,flow_source='mixed_rail_flow_minimum.json sector0 exact128 primal',scope=__doc__)
if ans=='sat':
 names=[f'{a}{x}_{y}_{j}'for x in range(W)for y in range(H)for j in range(N[x,y])for a in('b','t')];model=z.run('(get-value ('+' '.join(names)+'))');HERE.joinpath('mixed_rail_flow_clock.model').write_text(model)
 out['model_path']='mixed_rail_flow_clock.model'
if ans=='unknown':out['reason']=z.run('(get-info :reason-unknown)')
z.close();HERE.joinpath('mixed_rail_flow_clock.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
