from pathlib import Path
from fractions import Fraction
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];ns={'__file__':str(SELF.parent/'check_one_foreign_return_U_star_independent.py')};exec(Path(ns['__file__']).read_text().split('ports={}')[0],ns);W,M,walk,raw,xy,center,meet=[ns[k]for k in('W','M','walk','raw','xy','center','meet')]
D=R/'seven_word_spatial_return_2026-10-23';a=json.loads((D/'returned_C_prepared_loop_control.json').read_text());atoms='DCDCDVCVVFC';word=''.join(W[b]for b in atoms);assert len(word)==200;z=walk(word+M);assert z['feasible'];seed={q for q,b in z['req'].items()if b};assert len(seed)==27 and seed=={complex(*q)for q in a['initial_black']}
B=set(seed);p=0j;h=0;dirs=[1j,1,-1j,-1];cuts={0:(p,h)}
for i,ch in enumerate(word+M):
 assert(p in B)==(ch=='L');B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h];cuts[i+1]=(p,h)
 if i+1==200:assert(p,h,len(B))==(0j,2,53)and B=={complex(*q)for q in a['RAW_exit']['black']}
assert len(B)==52 and B=={complex(*q)for q in a['after_actual_marker_black']}
segs=[];t=0
for b in atoms:
 p,h=cuts[t];u=center(p,h);t+=len(W[b]);p,h=cuts[t];v=center(p,h);segs.append((xy(u),xy(v)))
assert cuts[10]==(1+1j,0)and cuts[129]==(3-4j,1)and cuts[185]==(1+0j,3)
queries=[]
for i in range(10):
 for j in range(i+1,10):
  c=meet(*segs[i],*segs[j]);queries.append((i,j,str(c)))
  if j>i+1:assert c is None
  else:
   assert c is not None and segs[i][1]==segs[j][0]
   if len(c)==3:assert c[:2]==(1,0)
   else:assert c==(segs[i][1],)
hits=[]
for i in range(10):
 c=meet(*segs[i],*segs[10])
 if i==9:assert c[:2]==(1,0)
 elif c is not None:assert c[1]==1 and c[2]==(1,1)and(i,c[0])in[(0,1),(1,0)];hits.append(i)
assert hits==[0,1]
pre=[]
for n in raw:
 z=walk(''.join(W[b]for b in n)+word+M);assert not z['feasible'];pre.append((n,z['i'],xy(z['q']),z['first']))
assert len(pre)==8
man=D/'returned_C_prepared_loop_control_manifest.json';sha=hashlib.sha256(man.read_bytes()).hexdigest();assert sha=='407d65053476a0d29ad76c0a1df2685bf1ebe2e25586ac2f68874b33b86bf8cb'
for f,h in json.loads(man.read_text())['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS prepared27-black returned-C loop, complete physical replay and exact eight-predecessor isolation','manifest_sha256':sha,'physical_reads':211,'initial_mass':27,'raw_exit_mass':53,'after_marker_mass':52,'old_foreign_segment_queries':queries,'returned_old_contact_descriptions':hits,'eight_predecessor_conflicts':pre,'analytic':['Whole-board literal211-read replay reconstructs the minimal27-black seed; all unlisted cells remain initially white, and exact complete final boards agree. RAW exit is(0,0,S), not the initial heading, with mass53 rather than27.','The old nine atomic chords plus actual F chord are simple including every adjacent collinear endpoint. Returned raw C touches no nonadjacent old interior before its END at doubled(1,1). That old vertex is incoming first-D END and outgoing first-C START; the unique outgoing-source assignment is C. Its old-C chart is exactly F(2,-5,E),returned C(0,-1,W),age3.','Prepending each of the eight genuine full packets to this fixed fullpacket-cut history yields an immutable repeated-cell turn conflict. Thus no longer uninterrupted full-eight prefix can lift THIS fixed control to U-entry. This does not exclude a different containing-source history at the same residual interface or an earlier foreign excursion.'],'scope':'Positive prepared finite-board control, not U-entry, not a physical pose/field cycle, and not a universal returned-C counterexample.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
