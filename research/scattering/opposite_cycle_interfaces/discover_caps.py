"""Discovery only: central blank caps for the four unprotected cycle outputs."""
import sys,json,gzip
from pathlib import Path
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1]
sys.path.insert(0,str(ROOT/'continuation_2026-10-22/ant_continuation'))
from ant_exact import W,P,D,step,plan,PHASES
sys.path.insert(0,str(HERE.parent/'transverse'));from crossing import Field,tail,rotate,plus
B=set();pos=(0,0);h=0
for _ in range(9977):pos,h,_=step(B,pos,h)
assert pos==(-15,10) and h==3
O=pos;E=B^{plus(O,rotate(q,1)) for q in P}
rows=[];dis=json.loads((HERE/'discovery.json').read_text())
for r in [29,32,56,71]:
 row=next(x for x in dis if x['r']==r and x['n']==x['p']==100);p,h=row['pose'];phase=row['tail']['phase'];tw=W[phase:]+W[:phase];p0,h0=plan(tw[:(104-phase)%104],tuple(p),h)[2:];assert h0==0
 constant=plus(O,rotate(p0,1));L=(-121-sum(constant))//4;cap=plus(constant,(2*L,2*L));assert -124<=sum(cap)<=-121
 rays=[(plus(O,rotate(q,1)),(-2,-2),0,None) for q in D]+[(plus(cap,plus(rotate(q,3),(-2,-2))),(-2,-2),0,None) for q in D]
 field=Field(rays,E^{plus(cap,rotate(q,3)) for q in P});p=cap;h=1;w=[];zmin=zmax=sum(p)
 for t in range(500000):
  zmin=min(zmin,sum(p));zmax=max(zmax,sum(p));p,h,ch=field.step(p,h);w.append(ch)
  if t>=312 and (t+1)%104==0:
   tw=''.join(w[-104:])
   if tw in PHASES and ''.join(w[-312:])==tw*3:
    cert=tail(field,p,h,tw)
    if cert:
     filename=f'cap_r{r}.txt.gz'
     with gzip.open(HERE/filename,'wt') as f:f.write(''.join(w))
     out=dict(status='infinite-model witness only; no actual transfer yet',r=r,start=[cap,1],incoming_phase_zero_source=p0,NE_entry_count_m_constant=[1,L],capture=t+1,pose=[p,h],tail=cert,prefix_z_bounds=[zmin,zmax],word_file=filename);break
 else:out=dict(r=r,status='limit',pose=[p,h])
 rows.append(out);print(json.dumps(out),flush=True);(HERE/'cap_discovery.json').write_text(json.dumps(rows,indent=2)+'\n')
