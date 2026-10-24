from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
R=Path(__file__).resolve().parents[1];U=R/'causal_reduction/unit_scale';H=json.loads((R/'recovered_bundle/ant_global/root/standard.json').read_text())['word'];P=json.loads((U/'reverse108_prepared_control.json').read_text())['word'];A=json.loads((U/'reverse108_parallel_rail_bundle.json').read_text());F=json.loads((U/'reverse108_prepared_family.json').read_text())
def orbit(w,start,h,d):
 p=complex(*start);groups=defaultdict(list);dirs=(1j,1,-1j,-1)
 for t,c in enumerate(w):
  x,y=int(p.real),int(p.imag);key=(x-y,x%2);rep=complex(key[1],key[1]-key[0]);k=int((p.real-rep.real)//d[0]);assert p==rep+k*complex(*d)
  groups[key].append((t-len(w)*k,k,t,c));h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
 for g in groups.values():g.sort()
 return groups,p,h
hs,end,h=orbit(H,(0,0),1,(2,2));ps,endp,hp=orbit(P,(0,6),3,(-2,-2));assert end==2+2j and h==1 and endp==-2+4j and hp==3
# Whole finite P^n fields, using independently sorted literal temporal histories.
def field_bits(events):
 assert events and all(a[3]!=b[3]for a,b in zip(events,events[1:]))
 return (int(events[0][3]=='L'),int(events[-1][3]=='R'),1,len(events)%2)
coef=[0]*4;inter=[0]*4;maxwidth=0;orbits=[]
for key,events in sorted(ps.items()):
 lo=min(k for t,k,i,c in events);hi=max(k for t,k,i,c in events);width=hi-lo;maxwidth=max(maxwidth,width);stable=field_bits(events)
 # At n>=width+1, only k<hi and k>=n+lo are boundary; central length n-width.
 n=width+1;left=[];right=[]
 for k in range(lo,hi):left.append(field_bits([e for e in events if 0<=k-e[1]<n]))
 for j in range(lo,hi):right.append(field_bits([e for e in events if 0<=n+j-e[1]<n]))
 for a in range(4):coef[a]+=stable[a];inter[a]+=sum(b[a]for b in left+right)-width*stable[a]
 orbits.append({'class':key,'width':width})
assert (coef,inter,maxwidth)==([11,3,23,12],[13,13,19,20],2)
for n in range(1,maxwidth+2):
 total=[0]*4
 for events in ps.values():
  for k in range(min(e[1]for e in events),n+max(e[1]for e in events)):
   hit=[e for e in events if 0<=k-e[1]<n]
   if hit:
    z=field_bits(hit);total=[a+b for a,b in zip(total,z)]
 assert total==[a*n+b for a,b in zip(coef,inter)]
assert F['counts_affine']=={'slope':coef,'intercept':inter}
NEread=set(hs);NEblack={k for k,e in hs.items()if field_bits(e)[1]};assert all(e[0][3]=='R'for e in hs.values())
turn=lambda S:{(-t,p)for t,p in S}
writers={'NE':(NEread,NEblack),'SW':(turn(NEread),turn(NEblack))}
Pread=set(ps);Pblack={k for k,e in ps.items()if e[0][3]=='L'}
for read,black in writers.values():
 lo=min(t for t,p in read);hi=max(t for t,p in read);assert hi-lo==10
 assert read=={(t,p)for t in range(lo,hi+1)for p in (0,1)}
 assert {(lo,p)for p in(0,1)}|{(hi,p)for p in(0,1)}<=black
assert max(t for t,p in Pblack)-min(t for t,p in Pblack)==10
shift=lambda S,t,p:{(u+t,(v+p)%2)for u,v in S}
records=[];single=[]
for orient,read,black in [('SW',Pread,Pblack),('NE',turn(Pread),turn(Pblack))]:
 for wn,(wr,wb)in writers.items():
  options={(x-u,(y-v)%2)for x,y in wb for u,v in black if (x-u)%2==0}
  assert not[(t,p)for t,p in options if shift(black,t,p)==wb&shift(read,t,p)]
  single.append((wn,orient,len(options)))
 # Anchored first rail is NE after a genuine half-turn if needed.
 options={(x-u,(y-v)%2)for x,y in NEblack for u,v in black if (x-u)%2==0}
 for ct,cp in sorted(options):
  req=shift(black,ct,cp);white=shift(read-black,ct,cp);missing=req-NEblack
  if not missing:assert white&NEblack;continue
  anchor=min(missing)
  for wn,(wr,wb)in writers.items():
   placements={(anchor[0]-u,(anchor[1]-v)%2)for u,v in wb if (anchor[0]-u)%2==0}
   for wt,wp in sorted(placements):
    secondread=shift(wr,wt,wp)
    if secondread&NEblack:continue
    # Reconstruct the interval-disjointness conclusion, not merely assume it.
    assert not(secondread&NEread)
    field=NEblack|shift(wb,wt,wp);badB=sorted(req-field);badW=sorted(white&field);assert badB or badW
    records.append(dict(second_writer=wn,consumer=orient,consumer_offset=[ct,cp],writer_offset=[wt,wp],missing_black=list(map(list,badB)),polluted_white=list(map(list,badW))))
assert records==A['records']and len(records)==59
counts=Counter((r['second_writer'],r['consumer'])for r in records);assert counts=={('NE','SW'):18,('NE','NE'):15,('SW','SW'):14,('SW','NE'):12}
out={'status':'PASS','note_sha256':hashlib.sha256((U/'reverse108_standard_rail_bundle_obstruction.md').read_bytes()).hexdigest(),'source_hashes':{p.name:hashlib.sha256(p.read_bytes()).hexdigest()for p in (U/'reverse108_parallel_rail_bundle.json',U/'reverse108_prepared_family.json')},'all_n_P_fields':{'slope':coef,'intercept':inter,'maximum_phase_offset_span':maxwidth},'single_rail_cases':single,'two_rail_cases':len(records),'two_rail_case_counts':{str(k):v for k,v in counts.items()},'scope':'One supplied P108 word, any finite parallel bundle of mature white-written standard rails. Finite-flight/cap lifting is separate; no other rewriter or universal-capture claim.'}
(R/'audits/check_reverse108_rail_bundle_independent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
