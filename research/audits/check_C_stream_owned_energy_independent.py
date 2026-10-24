from pathlib import Path
from collections import defaultdict,Counter
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();P=D/'C_STREAM_SIGNED_ENERGY_AND_OWNED_EXCURSION_FUEL.md';F=D/'C_stream_owned_fuel_energy_certificate.json';assert sha(P).startswith('360f1d9d')and sha(F).startswith('24dfad6c')and sha(D/'certify_C_stream_owned_fuel_energy.py').startswith('bffcb455');J=json.loads(F.read_text())
for f,h in J['dependencies'].items():assert sha(Path(f))==h
assert sha(S.with_name('check_active_C_entry_exit_independent.json')).startswith('317e4dce')and sha(S.with_name('check_C_cycle_excursion_independent.json')).startswith('99d6b773')
V=(1j,1,-1j,-1);off=(-1j,-1-1j,-1,0j);xy=lambda q:[int(q.real),int(q.imag)];key=lambda q:(q.real,q.imag)
def compute(w,h0,blocks=None,ref=None):
 p=0j;h=h0;E=[];n=len(w)
 for t,c in enumerate(w):E.append((p,h,c));h=(h+(1 if c=='R'else-1))%4;p+=V[h]
 d=p;assert d and h==h0 and int(d.real+d.imag)%2==0
 axis=0 if d.real else 1;dd=int(d.real if axis==0 else d.imag)
 def rep(p):
  a=int(p.real if axis==0 else p.imag);k=a//abs(dd)*(1 if dd>0 else-1);return p-k*d,k
 H=defaultdict(list)
 for t,(p,h,c)in enumerate(E):q,k=rep(p);H[q].append((t-k*n,t,h,c))
 for q,rs in H.items():rs.sort();assert all(a[3]!=b[3]for a,b in zip(rs,rs[1:]))
 adj=defaultdict(list);weights={};rows=[];lifetimes=[];inputs=[];outputs=[];birth=Counter();consume=Counter();opp=Counter();ic=Counter();oc=Counter();M=Counter()
 if blocks is None:blocks=[('period',n)]
 labels=[];ranges=[]
 for name,l in blocks:ranges.append((name,len(labels),len(labels)+l));labels +=[name]*l
 assert len(labels)==n and len({name for name,l in blocks})==len(blocks)
 for q,rs in sorted(H.items(),key=lambda z:key(z[0])):
  ax=rs[0][2]%2;sgn=lambda h:1 if h==ax else-1;a=sum(sgn(h)for tt,t,h,c in rs if c=='R')
  cp=rep(q+off[ax])[0];cm=rep(q+off[ax+2])[0];adj[cp].append((cm,-a));adj[cm].append((cp,a))
  row=dict(read_class=xy(q),axis_heading=ax,R_imbalance=a,C_plus=xy(cp),C_minus=xy(cm),complete_reads=[])
  for j,(ct,t,h,c)in enumerate(rs):
   ho=(h+(1 if c=='R'else-1))%4;row['complete_reads'].append(dict(canonical_time=ct,t=t,p=xy(E[t][0]),hi=h,ho=ho,c=c));charge=a*sgn(h);weights[t]=charge;b=labels[t]
   if c=='R':
    birth[b]+=charge
    if j==len(rs)-1:outputs.append(dict(phase=t,**{'class':xy(q)},charge=charge,block=b));oc[b]+=charge
   else:
    consume[b]+=charge
    if j==0:inputs.append(dict(phase=t,**{'class':xy(q)},charge=charge,block=b));ic[b]+=charge
    else:
     rc,rt,rh,rr=rs[j-1];assert rr=='R';age=ct-rc;ot=t-age;assert(ot-rt)%n==0;k=(ot-rt)//n;assert E[rt][0]+k*d==E[t][0]and age>=4 and age%4==0
     c0=a*sgn(rh);source=labels[rt];different=rh!=h;M[source,b,k]+=c0
     if different:opp[b]+=2*c0
     lifetimes.append(dict(R_phase=rt,L_phase=t,owner_period=k,owner_time=ot,age=age,**{'class':xy(q)},owner_heading=rh,consumer_heading=h,source_block=source,target_block=b,birth_charge=c0,opposite=different))
  rows.append(row)
 heights={next(iter(adj)):0};todo=list(heights)
 while todo:
  u=todo.pop()
  for v,k in adj[u]:
   if v in heights:assert heights[v]==heights[u]+k
   else:heights[v]=heights[u]+k;todo.append(v)
 assert len(heights)==len(adj);mn=min(heights.values());heights={p:z-mn for p,z in heights.items()}
 def face(t):
  k,j=divmod(t,n);p,h,c=E[j];return rep(p+k*d+off[h])[0]
 # Verify the local C change independently at EVERY physical event.
 for t,(p,h,c)in enumerate(E):
  delta=heights[face(t+1)]-heights[face(t)];assert delta==(0 if c=='R'else-weights[t])
 bro=[]
 for name,a,b in ranges:
  Q=heights[face(a)]-heights[face(b)];incoming=sum(z for(s,t,k),z in M.items()if t==name);outgoing=sum(z for(s,t,k),z in M.items()if s==name)
  assert consume[name]==Q==incoming-opp[name]+ic[name]and birth[name]==outgoing+oc[name]
  pa,ha,ca=E[a];kb,jb=divmod(b,n);pb,hb,cb=E[jb];closed=pa==pb+kb*d and ha==hb
  if closed:assert Q==0
  bro.append(dict(block=name,interval=[a,b],word=w[a:b],closed_head_pose=closed,C_start=xy(face(a)),C_end=xy(face(b)),C_height_drop=Q,birth_charge=birth[name],owned_incoming_charge=incoming,opposite_owner_charge=opp[name],input_charge=ic[name],permanent_output_charge=oc[name],owned_outgoing_charge=outgoing,signed_decorated_stock_flux=birth[name]-incoming-ic[name]))
 energy=sum(row['R_imbalance']**2 for row in rows);ds=sum(opp.values());os=sum(oc.values());iis=sum(ic.values());assert sum(consume.values())==0 and energy==sum(birth.values())==ds+os-iis
 result=dict(period=n,drift=xy(d),heading=h0,word=w,energy=energy,opposite_owner_charge=ds,output_charge=os,input_charge=iis,input_count=len(inputs),output_count=len(outputs),all_read_classes=rows,all_C_heights=[dict(**{'class':xy(q)},height=z)for q,z in sorted(heights.items(),key=lambda x:key(x[0]))],all_owned_lifetimes=lifetimes,input_roots=inputs,permanent_output_roots=outputs,block_rows=bro,full_owner_matrix=[dict(source=s,target=t,owner_period=k,charge=z)for(s,t,k),z in sorted(M.items())])
 if ref is not None:assert result==ref
 return result
summary={};derived={}
for name,z in J['base_controls'].items():
 r=compute(z['word'],z['heading'],ref=z);derived[name]=r;summary[name]=[r[k]for k in('energy','opposite_owner_charge','output_charge','input_charge','input_count','output_count')]
for name,z in J['excursion_partitions'].items():compute(z['word'],z['heading'],[(r['block'],r['interval'][1]-r['interval'][0])for r in z['block_rows']],z)
for r in J['all80_rotation_power_controls']:
 z=derived[r['name']];a=compute(z['word']*r['power'],r['rotation'])
 for k in('energy','opposite_owner_charge','output_charge','input_charge','input_count','output_count'):assert a[k]==r['power']*z[k]
 assert a['energy']==r['energy']and a['input_charge']==r['input_charge']
assert len(J['all80_rotation_power_controls'])==80
source=json.loads((D/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls']['S104'];hh={tuple(x['class']):x['height']for x in derived['S104']['all_C_heights']};cycle=[[hh[tuple(q)]for q in c['vertices']]for c in source['WHITE_first_entry_cycles']];assert cycle==[[3,3],[2,2]]and hh[1,-2]==4 and max(hh[tuple(x['class'])]for x in source['C_face_histories'])==4
assert any(x['R_phase']==43 and x['L_phase']==51 and x['birth_charge']==-1 and x['opposite']for x in derived['S104']['all_owned_lifetimes'])
assert any(x['R_phase']==62 and x['L_phase']==50 and x['owner_period']==-1 and x['birth_charge']==3 and x['age']==92 for x in derived['S104']['all_owned_lifetimes'])
assert summary['M10'][3:5]==[0,1]and summary['P1564'][3:5]==[0,197]
O=dict(status='PASS cap-free signed C-stream energy identity and complete owned excursion transfer only',proof=sha(P),certificate=sha(F),script=sha(S),summaries=summary,full_rotation_power_controls=80,complete_excursion_partitions=4,active_standard_maximum=4,standard_cycle_heights=cycle,analytic_review=[
'The unrestricted physical directed-port stream exists and is full-drift periodic on the plane because the balanced actual edgeflow lies in a finite-width strip. Its local Cplus-Cminus difference is exactly Rplus-Rminus, including BLACK-first histories. This imports only the signed stream construction, not a WHITE/capthree exclusion or a global maximum rule.',
'R leaves the activeCface unchanged. L with headingepsilon crosses to the opposite Cface, changingheight by-a epsilon. Actual wholeperiod returns to a translatedsameface, so sumL aepsilon=0. Collecting allR charges bycomplete physicalclasses gives sumR aepsilon=sum a^2. No arbitraryfieldstocksum is needed.',
'EveryR is oneactualR-to-nextL source or a lastR permanentroot; everyL is oneownedconsumer or a genuinefirstL inputroot. Actual source and consumer share a, with equal/oppositeepsilon. Subtraction gives E=D+O-I exactly; D,O,I andindividualcharges remain signed. FirstL+lastR inoneclass contribute both distinctroots. Zerocharge is not absence of input or physicalresource.',
'For any genuinecontiguous period partition, full ownerphase/periodoffset/sourceblock/targetblock are retained. Sourcebirthbalance and consumerchargebalance follow peractualownedpair. Eachclosedheadposeexcursion has identicalactiveCface and henceQ=0; connectors retain exactheightdrops. No geometric deletion, independentfuel, positivepayment or finitealphabet is inferred.',
'Fresh vector geometry reconstructs everyFULLd physicalhistory, samecellowner/seam, Cheight, each eventlocalheightchange, rootcharge and completeblockmatrix for allfivecontrols andfourpartitions. All80rotation/powercontrols scaleexactly. StandardE,D,O,I=(60,52,8,0); prepared80=(44,26,16,-2). StandardnegativeR43owner andpreviousperiodR62owner retained; prepared10/1564zeroI has1/197actualinputs.',
'The exactstandardactiveCmax4 at(1,-2) liesoffbothdiscoverycycles atlevels3/2. Thus choosingthehighestdiscoverycycle doesnot makeotheractivefaceslower. No outside-side inference, WHITE S1, noinputdetector, monotonicity or globalcapture follows. Infinitepreparedfieldstock is never summed/subtracted.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(summary);print(sha(S.with_suffix('.json')))
