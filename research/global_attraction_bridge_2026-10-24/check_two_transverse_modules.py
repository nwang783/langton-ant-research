"""Two literal causal moving returns, with all initially funded ports retained."""
from pathlib import Path
import json,hashlib
from check_return_permanent_output_debt import DXY,rot,future,case
P=Path(__file__).parent;G={(0,-1),(1,1),(1,3),(2,2)}
def points(n):
 poses=[((0,0),1),((7*n-1,7*n),0),((5*n,9*n-4),3),((n+5,5*n),2)]
 return [{(p[0]+rot(q,h-1)[0],p[1]+rot(q,h-1)[1]) for q in G} for p,h in poses]
def step(B,p,h,t):
 old=B.pop(p,None)
 if old is None:B[p]=t;h=(h+1)%4
 else:h=(h-1)%4
 return (p[0]+DXY[h][0],p[1]+DXY[h][1]),h,old
B={q:-i-1 for i,q in enumerate(sorted(G))};p=(0,0);h=1;A='';U='';gp=None
for t in range(286):
 if t==182:gp,gh=p,h
 p,h,old=step(B,p,h,t)
 if t<182:A+='R' if old is None else 'L'
 else:U+='R' if old is None else 'L'
src=json.loads((P/'TRANSVERSE_FAR_MODULE_SOURCE.json').read_text());F,Z=src['post_contact_word'],src['tail_word'];assert U==Z and (gp,gh)==((5,1),1)
def stages(n):
 r=[7*n//2-4,n-5,2*n-6,n-6];part=[61,71,61,56]
 return [A+U*r[i]+U[:part[i]] for i in range(4)]
base=set.union(*points(20));C0=set(map(tuple,src['protected_black']));b1=3061;c1=14393;records=[]
for n,J in [(40,100),(80,200)]:
 T=c1+8986+104*J;v=(76+2*J,55-2*J)
 tr=lambda q:(v[0]+q[1],v[1]-q[0])
 ports=[{tr(q) for q in b} for b in points(n)[1:]];extra=set.union(*ports);seed=base|extra;assert len(seed)==28 and len(extra)==12
 pre=''.join(stages(20));second=''.join(stages(n))[182:]
 expected=pre+F+U*J+second+F+U*2
 b2=T+156*n-241;c2=T+780*n-1389;tail_start=c2+8986
 q1=(60,63);q2=tr((3*n,3*n+3));assert len(pre)==c1 and len(pre+F+U*J)==T and T+len(second)==c2
 assert len(expected)==tail_start+208
 cuts={0,b1+1,c1,c1+8986,T,b2+1,c2,tail_start,len(expected)}
 B={q:-i-1 for i,q in enumerate(sorted(seed))};p=(0,0);h=1;first={};deaths={};births={};states={};turns=[];contact_id={};readset=set()
 for t,ch in enumerate(expected):
  if t in cuts:states[t]=(dict(B),p,h)
  if p in seed and p not in first:first[p]=t
  if t in (b1,b2):assert p in (q1,q2) and p not in B
  if t==c1:assert p==q1 and h==2 and B[p]==b1
  if t==c2:assert p==q2 and h==3 and B[p]==b2
  readset.add(p);pp=p;p,h,old=step(B,p,h,t);assert (old is None)==(ch=='R'),(n,t,p,ch,old)
  turns.append(ch)
  if old is None:births[t]=pp
  else:deaths[old]=t
 states[len(expected)]=(dict(B),p,h)
 word,dr,tail,tests=future(B,p,h);assert word==U and dr==(-2,-2)
 # Exact pruned-state closure bounds relevance for the ENTIRE infinite tail.
 tailC={q for q,i in B.items() if i in tail};CC=dict(B);pp=p;hh=h;extra_death={};events=[]
 for j in range(104):
  pp,hh,old=step(CC,pp,hh,len(expected)+j);events.append(old)
  if old is not None:extra_death[old]=j
 ww,dd,tt,_=future(CC,pp,hh);assert ww==U and dd==dr
 extra_death.update({i:104+j for i,j in tt.items()})
 nextC={q for q,i in CC.items() if i in tt};assert nextC=={(q[0]-2,q[1]-2) for q in tailC}
 LL=len(tailC);tail_profile=[LL]
 for j,old in enumerate(events):
  LL+=int(len(expected)+j in extra_death) if old is None else -1;tail_profile.append(LL)
 assert max(tail_profile)==22 and LL==len(tailC)
 deaths.update({i:len(expected)+t for i,t in tail.items()})
 # The added inputs are genuinely initial, untouched throughout the entire first return/recovery.
 assert len(first)==28 and min(first[q] for q in extra)>T
 # Every immutable local source fate at the first contact agrees with the old isolated source.
 original={tuple(z['cell']):z for z in json.loads((P/'TRANSVERSE_FAR_MODULE_CHECKED.json').read_text())['protected_reference']['initial_read_fates']}
 qfirst=states[c1][0];first_relevant={q for q,i in qfirst.items() if i in deaths}
 baseline_relevant={ (q1[0]+q[0],q1[1]+q[1]) for q,z in original.items() if z['death'] is not None }
 assert first_relevant==baseline_relevant|extra and len(first_relevant)==297
 actual_source={ (x-q1[0],y-q1[1]) for x,y in qfirst if -73<=x+y-sum(q1)<=17 and x-y-(q1[0]-q1[1])>=-20 }
 extras_inside={(x-q1[0],y-q1[1]) for x,y in extra if -73<=x+y-sum(q1)<=17 and x-y-(q1[0]-q1[1])>=-20}
 assert actual_source==C0|extras_inside and len(extras_inside)==4
 for q,z in original.items():
  i=qfirst[(q1[0]+q[0],q1[1]+q[1])];d=deaths.get(i)
  assert d==(None if z['death'] is None else c1+z['death'])
 qsecond=states[c2][0];relsecond={q for q,i in qsecond.items() if i in deaths}
 assert relsecond=={tr((3*n+q[0],3*n+3+q[1])) for q,z in original.items() if z['death'] is not None} and len(relsecond)==285
 # Complete first-contact field equality to the isolated construction plus all12 added bits.
 Bbase={q:-i-1 for i,q in enumerate(sorted(base))};pbase=(0,0);hbase=1
 for t,ch in enumerate(pre):pbase,hbase,old=step(Bbase,pbase,hbase,t);assert (old is None)==(ch=='R')
 assert set(qfirst)==set(Bbase)|extra
 # Record full fields with actual lifetime identities, not only their relevant pruning.
 snapshots=[]
 for t,(board,pp,hh) in sorted(states.items()):
  snapshots.append(dict(cut=t,pose=[pp,hh],full_black=[dict(cell=q,lifetime=i,death=deaths.get(i)) for q,i in sorted(board.items())],full_mass=len(board),relevant_mass=sum(i in deaths for i in board.values())))
 fullcase=case(f'two_modules_n20_n{n}',seed,1,len(expected),(b1,b2))
 assert fullcase['relevant_mass_max']==444
 L=len(seed);after_T_max=0
 for t,ch in enumerate(expected):
  if t>=T:after_T_max=max(after_T_max,L)
  L+=int(t in deaths) if ch=='R' else -1
 assert after_T_max==432
 # First exact infinite continuation begins here, not at the first finite canonical stretch.
 assert expected[tail_start-1]!=U[-1]
 records.append(dict(n1=20,n2=n,spacing_periods=J,initial_black=sorted(seed),added_initial_ports=[sorted(b) for b in ports],virtual_second_launch=v,second_U_entry=T,first_contact=c1,second_contact=c2,exact_final_canonical_start=tail_start,marked_lifetimes=[dict(cell=q1,birth=b1,death=c1,age=c1-b1),dict(cell=q2,birth=b2,death=c2,age=c2-b2)],all_initial_first_reads=[dict(cell=q,first_read=first[q],added=q in extra) for q in sorted(seed)],complete_snapshots=snapshots,first_protected_field_added_cells=sorted(extras_inside),first_relevant_exact_decomposition=dict(original_source=285,added_original_ports=12,total=297),second_relevant=285,relevant_all_future_max=444,full_case=fullcase,terminal_tail=word,terminal_drift=dr,terminal_ray_parity_tests=tests,infinite_tail_relevant_profile=tail_profile))
 print(json.dumps({k:v for k,v in records[-1].items() if k not in ['complete_snapshots','full_case','initial_black','all_initial_first_reads','added_initial_ports','terminal_tail']},indent=2),flush=True)
out=dict(status='AUTHOR exact finite two-module concatenations; independent audit pending',scope='Two literal28-cell finite seeds. Two genuine moving long returns, second longer, funded by12 additional initial bits. No autonomous regeneration, universal family or infinite concatenation.',source_hashes={q:hashlib.sha256((P/q).read_bytes()).hexdigest() for q in ['TRANSVERSE_FAR_MODULE_SOURCE.json','TRANSVERSE_FAR_MODULE_CHECKED.json','TRANSVERSE_FAR_MODULE_MANIFEST.json','check_return_permanent_output_debt.py']},controls=records)
(P/'TWO_TRANSVERSE_MODULES_CHECKED.json').write_text(json.dumps(out,indent=2)+'\n')
