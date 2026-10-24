from pathlib import Path
from itertools import product,combinations
from collections import Counter
import json,hashlib,ast,math
S=Path(__file__);R=S.parent.parent;P=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();bind={}
for line in(P/'SPLICE112_SHA256SUMS').read_text().splitlines():
 h,f=line.split();assert sha(P/f)==h;bind[f]=h
assert bind['SPLICE112_FIXED_INVENTORY_EXCLUSION.md']=='2de9060cb1e366e290f3df410e1f6bed8557d2ec741aa3f648758cbe716759ed'
z=json.loads((P/'probe_standard_upper_splice112.json').read_text());cert=json.loads((P/'splice112_inventory_clock_tree.json').read_text());std=json.loads((P/'check_single_used_first_circle.json').read_text())
V=(1j,1,-1j,-1);dr=2-2j;N=112;xy=lambda p:(int(p.real),int(p.imag));qt=lambda p:(p-(int(p.real)//2)*dr,int(p.real)//2);turn=lambda h,j:(h+(1 if j%2==0 else-1))%4
H={complex(*ast.literal_eval(p)):tuple('NESW'.index(c)for c in s)for p,s in z['complete_named_histories'].items()}
base={qt(complex(*q['point'])+1+1j)[0]:tuple('NESW'.index(c)for c in q['headings'])for q in std['all_standard_stable_histories']}
low=['W','','N','SS','WE','WWE','SNNS','SSNS','EEE','WWEEWW'];constructed={complex(i%2,i//2-1-i%2):tuple('NESW'.index(c)for c in w)for i,w in enumerate(low)}
constructed.update({p:h for p,h in base.items()if p.real+p.imag>=4});assert H==constructed and len(H)==26 and sum(bool(h)for h in H.values())==25 and sum(map(len,H.values()))==112 and sum(len(h)%2 for h in H.values())==12
assert max(p.real+p.imag for p,h in H.items()if h)-min(p.real+p.imag for p,h in H.items()if h)+1==13
extra=0
for p,h in H.items():
 new=Counter((j%2,x)for j,x in enumerate(h));old=Counter((j%2,x)for j,x in enumerate(base.get(p,())));assert all(new[k]>=v for k,v in old.items());extra+=sum((new-old).values())
assert extra==8 and all(p in H for p in base)
# Entire proposed physical successor permutation, including zero-use ports.
succ={}
for p,h in H.items():
 for d,v in enumerate(V):
  q,k=qt(p+v);src=[j for j,x in enumerate(h)if turn(x,j)==d];dst=[j for j,x in enumerate(H.get(q,()))if x==d];assert len(src)==len(dst)
  for a,b in zip(src,dst):succ[p,a]=((q,b),k)
assert len(succ)==112 and len({v for v,k in succ.values()})==112
seen=set();cyc=[]
for st in succ:
 if st in seen:continue
 u=st;k=0;seq=[]
 while u not in seen:seen.add(u);seq.append((u,k));u,dk=succ[u];k+=dk
 assert u==st;cyc.append((len(seq),k))
assert sorted(cyc)==[(8,0),(104,1)]
points=sorted((p for p,h in H.items()if h),key=lambda p:(p.real+p.imag,p.real));ix={p:i for i,p in enumerate(points)};opts=[]
for p in points:
 h=H[p];a=h[0]%2;n=len(h);counts=Counter((j%2,x)for j,x in enumerate(h));rr=range(0,n,2);ll=range(1,n,2);o=[]
 for r,l in product(combinations(rr,counts[0,a]),combinations(ll,counts[1,a])):
  plus=set(r)|set(l);o.append(tuple(a if j in plus else a+2 for j in range(n)))
 opts.append(o)
assert cert['points']==list(map(lambda p:list(xy(p)),points)) and cert['all_cell_heading_options']==[[''.join('NESW'[h]for h in w)for w in oo]for oo in opts]
sizes=list(map(len,opts));assert math.prod(sizes)==cert['raw_option_product']==3482851737600
var={};meta=[]
for i,p in enumerate(points):
 for d in range(4):
  counts=[sum(turn(x,j)==d for j,x in enumerate(w))for w in opts[i]];assert len(set(counts))==1
  for k in range(counts[0]):var[i,d,k]=len(meta);meta.append([i,d,k])
assert len(meta)==112 and meta==cert['variables'];ALL=[]
for i,p in enumerate(points):
 oo=[]
 for w in opts[i]:
  ni=Counter();no=Counter();ins=[];outs=[];cs=[];ee={}
  def add(u,v,c):ee[u,v]=max(ee.get((u,v),-10**9),c)
  for j,h in enumerate(w):
   q,k=qt(p-V[h]);ii=ix[q];iv=var[ii,h,ni[h]];ni[h]+=1;d=turn(h,j);ov=var[i,d,no[d]];no[d]+=1;ins.append(iv);outs.append(ov);cs.append(1+k*N)
  for iv,ov,c in zip(ins,outs,cs):add(iv,ov,c);add(ov,iv,-c)
  for j in range(1,len(w)):add(ins[j-1],ins[j],4+cs[j-1]-cs[j])
  oo.append(ee)
 ALL.append(oo)
def common(dom):
 ret={}
 for i,ds in enumerate(dom):
  keys=set(ALL[i][ds[0]])
  for o in ds[1:]:keys&=ALL[i][o].keys()
  for e in keys:ret[e]=max(ret.get(e,-10**9),min(ALL[i][o][e]for o in ds))
 return ret
assert cert['complete']and len(cert['nodes'])==1 and not cert['feasible_complete_options'];node=cert['nodes'][0];dom=[list(range(n))for n in sizes];assert node['input_domains']==dom
rounds=[]
for rnd in node['propagation']:
 available=common(dom);removed=set()
 for rr in rnd['removed']:
  i,o=rr['cell'],rr['option'];assert o in dom[i]and len(dom[i])>1 and(i,o)not in removed;removed.add((i,o));av=dict(available)
  for e,c in ALL[i][o].items():av[e]=max(av.get(e,-10**9),c)
  cy=rr['cycle'];assert cy and sum(c for u,v,c in cy)>0
  for j,(u,v,c)in enumerate(cy):assert v==cy[(j+1)%len(cy)][0]and av[u,v]>=c
 dom=[[o for o in ds if(i,o)not in removed]for i,ds in enumerate(dom)];rounds.append(len(removed))
assert rounds==[1,3,4,5,22,6]and sum(rounds)==41 and node['after_domains']==dom and node['leaf']=='infeasible'and node['reason']=='empty_domain';empty=[list(xy(points[i]))for i,d in enumerate(dom)if not d];assert empty==[[1,2]]
out={'status':'PASS one exact112-event full directed inventory impossible under all WHITE local reorderings','bindings':bind,'occupied_classes':25,'height':13,'events':112,'growth':12,'original_permutation_cycles':cyc,'standard_translated_plus_extra_occurrences':extra,'domain_sizes':sizes,'raw_product':math.prod(sizes),'positive_cycle_option_deletions_by_round':rounds,'empty_classes':empty,'analytic_review':['The entire target is independently reconstructed from signed normalized standard104 translated(1,1) and the ten explicitly supplied lower classes. All full physical port totals including zero-use and all112 permutation events match; the proposed literal order has104/+1 and8/0 components, so is NOT a controller.','Every complete WHITE local history with fixed (heading,turn) counts is independently generated by positive-heading rank subsets on R and L positions. Across25 occupied classes this is exactly3,482,851,737,600 choices, not a guessed cap. Count comparison gives exactly standard translated inventory plus eight events; this is deliberately narrow constructive scope.','For each outgoing physical-edge ordinal variable, target read clock equals physical predecessor representative clock plus1+a*112. Independent full-drift quotient reconstruction retains both equality directions and consecutive same-cell gap>=4. No temporal gauge, first-clock anchoring or solver model restricts the options.','Each common lower-bound edge is implied by EVERY remaining option at its cell, then combined across cells. Every41 deletion uses an explicitly closed positive integer cycle from common plus tested-option edges. Six simultaneous sound pruning rounds exhaust all nine options at(1,2); one proof node, no search/timeout premise.','Only this exact full inventory is impossible. Different inventory, added events, reordered standard backbone with different counts, other periods/drifts and universal attraction are not classified. The retained short-eight-detour theorem has distinct actual-backbone-order hypotheses; neither is silently substituted for the other.']};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S),sha(S.with_suffix('.json')))
