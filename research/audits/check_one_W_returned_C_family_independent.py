from pathlib import Path
from collections import Counter
from itertools import product
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1];p=SELF.parent/'check_one_foreign_return_U_star_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('ports={}')[0],ns)
W,M,walk,raw,xy,center,meet=[ns[k]for k in('W','M','walk','raw','xy','center','meet')];D=ROOT/'seven_word_spatial_return_2026-10-23';ref=json.loads((D/'one_W_returned_C_family.json').read_text())
def word(tokens):return''.join(W[c]for n in tokens for c in n)
def orders(t):
 if not sum(t):return[()]
 ans=[]
 for i,n in enumerate('DVU'):
  if t[i]:s=list(t);s[i]-=1;ans.extend((n,)+r for r in orders(tuple(s)))
 return ans
def ecounts(delta):
 x,y=xy(delta);out=[]
 if y>0:return out
 for v in range(-y+1):
  d=-y-v;rem=x-d-3*v
  if rem>=0 and rem%4==0:out.append((d,v,rem//4))
 return out
cases={};positives={}
def add(src,wp,S,E,f,kind):
 tokens=(src,wp)+S+(('C',)if kind=='single'else())+E+(f,'C');w=word(tokens);a=walk(w+M)
 assert tokens not in cases;cases[tokens]=(a['feasible'],kind)
 if a['feasible']:positives[tokens]=(w,a)
for src in('DC','VC','UC','VCC','UCC'):
 for f,target in zip('FQB',(2-5j,4-5j,5-4j)):
  last=('U',)if f=='B'else('V','U')
  for wp in('VCC','UCC'):
   st=1j+raw[wp]['p']*1j;assert(raw[wp]['h']+3)%4==1
   for t in ecounts(target-st):
    for E in orders(t):
     if E and E[-1]in last:add(src,wp,(),E,f,'double')
  for wp in('DC','VC','UC'):
   st=1j+raw[wp]['p']*1j;assert(raw[wp]['h']+3)%4==2
   budget=int(st.imag-1-target.imag);assert budget<=6
   for a in range(budget+1):
    for b in range((budget-a)//3+1):
     for c in range((budget-a-3*b)//4+1):
      if a+b+c==0:continue
      remain=budget-a-3*b-4*c
      for e in range(remain+1):
       d=remain-e;num=int(target.real-st.real+a+b-d-3*e)
       if num<0 or num%4:continue
       for S,E in product(orders((a,b,c)),orders((d,e,num//4))):
        if E and E[-1]in last:add(src,wp,S,E,f,'single')
assert len(cases)==1890 and len(positives)==10
assert Counter(cases.values())=={(False,'double'):60,(False,'single'):1820,(True,'single'):10}
assert{(tuple(a['literal_tokens']),a['feasible'])for a in ref['all_endpoint_driven_cases']}=={(t,v[0])for t,v in cases.items()}
controls=[];words={};physical=0
for rr in ref['positive_complete_board_controls']:
 tokens=tuple(rr['literal_tokens']);w,a=positives[tokens];cid=rr['control_id'];words[cid]=w;assert tokens[0]=='DC'and tokens[-2]=='F'
 seed={q for q,b in a['req'].items()if b};assert seed=={complex(*q)for q in rr['initial_black']}
 B=set(seed);p=0j;h=0;cuts={0:(p,h)}
 for i,ch in enumerate(w+M):
  assert(p in B)==(ch=='L');B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=1j*(-1j)**h;cuts[i+1]=(p,h);physical+=1
  if i+1==len(w):assert len(B)==rr['raw_exit_mass']
 assert len(B)==rr['complete_marker_exit_mass']
 atoms=''.join(tokens);t=0;segs=[]
 for n in atoms:
  p,h=cuts[t];u=center(p,h);t+=len(W[n]);p,h=cuts[t];segs.append((xy(u),xy(center(p,h))))
 for j in range(len(segs)-1):
  for i in range(j):
   hit=meet(*segs[i],*segs[j])
   if i+1<j:assert hit is None
   else:assert hit is not None and (hit[:2]==(1,0)if len(hit)==3 else hit==(segs[i][1],))
 hits=[]
 for i in range(len(segs)-2):
  z=meet(*segs[i],*segs[-1])
  if z is not None:assert len(z)==3 and z[1]==1 and z[2]==(1,1)and(i,z[0])in((0,1),(1,0));hits.append(i)
 assert hits==[0,1]and segs[-1][1]==segs[1][0]==(1,1)
 controls.append({'id':cid,'mass':len(seed),'raw_reads':len(w),'raw_mass':rr['raw_exit_mass']})
assert[c['mass']for c in controls]==[30,27,31,31,31,28,32,32,32,36]
# All-length persistent D-output law, from the complete RAW footprint only.
d=walk(W['D']);assert(d['p'],d['h'])==(1+1j,0)
assert[(i,ch)for i,(q,h,ch)in enumerate(d['reads'])if q==2][-1][1]=='R'
assert 1-1j not in d['req']and min(q.imag for q in d['req'])==-1
for cid,pre,port,threshold in[(0,('DC',),-2j,2),(3,('DC',),-2j,2),(5,(),-2-4j,4),(6,(),-3-5j,5)]:
 a=walk(word(pre)+words[cid]+M);assert a['feasible']and a['req'][port]is False and port.imag-port.real==-2 and -port.imag==threshold
 # For every n>=threshold, producer i=n+port.y lies in[0,n-1], and (i+2,i)=n(1,1)+port.
 assert port.imag<0 and port.real==port.imag+2
# Closed finite reverse relation: replay EVERY allowed predecessor, not a depth cut.
node_map={(r['control_id'],tuple(r['prefix'])):r for r in ref['complete_reverse_full_packet_gate_nodes']};assert len(node_map)==26
edges=[];bad=0
for(cid,pre),rr in node_map.items():
 suffix=word(pre)+words[cid]+M;assert walk(suffix)['feasible'];incoming=[]
 for n in raw:
  a=walk(word((n,))+suffix)
  if a['feasible']:
   assert(cid,(n,)+pre)in node_map and n not in('U','UC','UCC');incoming.append(n);edges.append((cid,pre,n))
  else:bad+=1
 assert sorted(incoming)==sorted(rr['exact_incoming_full_packets'])
assert len(edges)+bad==208
maxlens=[max(len(p)for c,p in node_map if c==i)for i in range(10)];assert maxlens==[2,0,1,2,1,3,4,0,1,1]
mp=D/'one_W_returned_C_family_manifest.json';sha=hashlib.sha256(mp.read_bytes()).hexdigest();assert sha=='21da1f5bec86654fdb8698cd408190070bb02dfb6fd664f09c8927b4a864c560'
for n,h in json.loads(mp.read_text())['files'].items():assert hashlib.sha256((D/n).read_bytes()).hexdigest()==h
out={'status':'PASS exact one-W returned-C family and all-ten causal left-lift exclusion','manifest_sha256':sha,'full_endpoint_words':1890,'double_tail_W_conflicts':60,'single_tail_W_conflicts':1820,'actual_positive_controls':controls,'physical_positive_reads':physical,'reverse_nodes':26,'predecessor_queries':208,'feasible_reverse_edges':len(edges),'immutable_reverse_conflicts':bad,'maximum_earlier_fullpacket_lengths':maxlens,'analytic':['Exactly one W base after the selected C can own both remaining Cs only as VCC/UCC, or own one as DC/VC/UC followed by a nonempty S-base run whose last base owns the other C. Both cases are present. Exact endpoint y budget<=6 bounds all nonnegative D/V/S-U counts, while x fixes E-U by divisibility; all multiset orders and actual last V/U adjacency are retained. This is an exhaustive algebraic subfamily, not an arbitrary depth scan.','Ten feasible full words have complete minimal finite boards, independently replayed. All have source DC C1 and foreign F. Their old-plus-foreign proxies are simple; returned C first meets the unique old vertex at its endpoint, owned by outgoing first C. This is a prepared positive loop, not physical state reset or a U-entry history.','Plain D freshly writes(i+2,i). Later D copy k=1 misses local(1,-1), and k>=2 lies below its RAW y minimum. At any fixed suffix first-R port q with qy-qx=-2,qy<0, every D-run length n>=-qy leaves that earlier D output unread and black at the suffix firstR. The thresholds2,2,4,5 therefore hold for ALL lengths.','The finite reverse relation is independently closed under all8 predecessors at every one of26 nodes; every other query has an immutable read conflict, not a discarded depth extension. No U-family edge enters any node. Hence no uninterrupted eight-prefix supplies a U-entry cut at or before the selected old C. A U later inside a positive word starts a new factor excluding that old source and is not a counterexample.'],'scope':'Only the exact one-W-base family and the previously signed double-tail source case. Arbitrary two-or-more W-base runs and mixed earlier foreign prefixes remain open. No global contact ban or capture theorem.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(physical)
