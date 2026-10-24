from pathlib import Path
from collections import Counter
from fractions import Fraction as F
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'seven_word_spatial_return_2026-10-23'
ns={'__file__':str(R/'audits/check_foreign_kinked_barrier_turn_independent.py')};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns)
W,M,walk,center,xy,meet=(ns[k]for k in('W','M','walk','center','xy','meet'))
K={-1-1j,-1,-1j,0,1};L={0,1j,1,1+1j};author=json.loads((D/'foreign_tail_first_contact.json').read_text());allrows={};filtered={};angles=[]
for name in'QB':
 full=walk(W[name]+M);raw=walk(W[name]);mid=-7-3j;end=center(raw['p'],raw['h']);assert W[name][:56]==W['F'];rows=[]
 for a in'DCVU':
  atom=walk(W[a]);A=-1-1j;B=center(atom['p'],atom['h']);u=B-A
  for h in range(4):
   turn=(-1j)**h;c=mid*turn;d=end*turn;v=d-c
   points=[A+s*u-c-t*v for s in(0,1)for t in(0,1)]
   lo=[-((-int(min(getattr(q,z)for q in points)))//2)for z in('real','imag')];hi=[int(max(getattr(q,z)for q in points))//2 for z in('real','imag')]
   for x in range(lo[0],hi[0]+1):
    for y in range(lo[1],hi[1]+1):
     if(x+y+h)%2:continue
     p=complex(x,y);s0=center(p,h);s1=2*p+c;s2=2*p+d
     earlier=meet(xy(A),xy(B),xy(s0),xy(s1));adj=False
     if earlier is not None:
      if not(len(earlier)==3 and isinstance(earlier[0],F) and earlier[:2]==(1,0)):continue
      if(p,h)!=(atom['p'],atom['h']):continue
      adj=True
     hit=meet(xy(A),xy(B),xy(s1),xy(s2))
     if hit is None:continue
     collinear=not(len(hit)==3 and isinstance(hit[0],F))
     if not collinear:
      s,t,_=hit
     else:
      # Earliest tail parameter touching the closed old segment; assign an
      # old endpoint to its outgoing atom, never an arbitrary overlap point.
      z='real'if v.real else'imag';ts=[F(int(getattr(q-s1,z)),int(getattr(v,z)))for q in(A,B)];t=min(ts)
      pp=(A,B)[ts.index(t)];zz='real'if u.real else'imag';s=F(int(getattr(pp-A,zz)),int(getattr(u,zz)))
     if not(0<=s<1 and 0<t<=1):continue
     ages=[n for n in((-h)%4,(-h)%4+4)if n or a!='C']
     rows.append((a,x,y,h,s,t,tuple(ages),collinear,adj))
 expected={(r['source_atom'],*r['foreign_pose'],F(r['contact']['s']),F(r['contact']['t']),tuple(r['permitted_C_ages']),r['contact']['kind']=='collinear_first_onset',r['legal_F_entry_adjacent_source_endpoint'])for r in author['rows'][name]}
 assert set(rows)==expected;allrows[name]=rows
 survivors=[];counts=Counter()
 for a,x,y,h,s,t,ages,col,adj in rows:
  if a!='U':continue
  p=complex(x,y);turn=(-1j)**h;core={p+q*turn for q in K};white={p+q*turn for q,b in full['req'].items()if not b};inputs={p+q*turn for q,b in full['req'].items()if b}-core
  why='core'if core&L else'white'if white&L else'open';counts[why]+=1
  if why!='open':continue
  remain=[]
  for n in ages:
   if n<=1 and inputs&L:continue
   if name=='B'and(x,y,h,n)==(-3,6,3,1):
    q=(-1+2j-p)/turn;assert q==-4-2j and full['req'][q]is False
    assert next((i,c)for i,(qq,hh,c)in enumerate(full['reads'])if qq==q)==(52,'R');continue
   remain.append((n,int(n>=4)))
  if remain:survivors.append([x,y,h,remain])
 filtered[name]={'contexts':dict(counts),'survivors':survivors}
 assert len(rows)=={'Q':24,'B':39}[name]and sum(len(r[6])for r in rows)=={'Q':47,'B':76}[name]
# Symbolic principal closing turns: beta/(pi/4) is strictly in(0,1).
# Total lifted tangent is2(n+2)+delta-8b. For delta>0 choose
# close=8*(floor(n/4)+1)-2*(n+2)-delta, always strictly principal.
for name in'QB':
 for a in'DCVU':
  dc,db=({'D':(1,0),'C':(1,0),'V':(0,1),'U':(0,0)}if name=='Q'else{'D':(1,1),'C':(1,1),'V':(0,2),'U':(0,1)})[a]
  if(dc,db)==(0,0):continue
  for n in range(4):
   cc=8-2*(n+2)-dc;cd=-db
   assert min(cc,cc+cd)>=-4 and max(cc,cc+cd)<=4 and not(cd==0 and abs(cc)==4)
   angles.append((name,a,n,cc,cd))
for b in(0,1):
 valid=[n for n in range(16)if abs(8*(n//4+1-b))==8]
 assert valid==list(range(4*b,4*b+4))
qcol=[r for r in allrows['Q']if r[7]];assert len(qcol)==1 and qcol[0][0]=='U'and qcol[0][3]==2 and qcol[0][6]==(2,6)
assert not any(r[7]for r in allrows['B'])
manifest=D/'foreign_tail_first_contact_manifest.json';sha=hashlib.sha256(manifest.read_bytes()).hexdigest();assert sha=='364870f37fdab340789d094421ad986b55848bcf137f73ec957f9839cb9be010'
for name,expected in json.loads(manifest.read_text())['files'].items():assert hashlib.sha256((D/name).read_bytes()).hexdigest()==expected
out={'status':'PASS genuine Q/B-tail chronological first-contact catalogue and scoped U-source history cuts','manifest_sha256':sha,'counts':{n:{'geometries':len(rr),'clock_labels':sum(len(x[6])for x in rr)}for n,rr in allrows.items()},'U_filters':filtered,'symbolic_angles':angles,'collinear_Q_case':str(qcol),'analytic':['Before the first tail contact, the F-prefix must miss the old path. The source-chord filter allows only its legal F-entry adjacency, verified at the full physical endpoint pose. Both appended pieces are simple and only adjacent to one another. Thus chronological first contact gives the Jordan closure, not an arbitrary reset closure.','The actual C-to-F negative wrap is retained. Positive delta gives ages0..3 or4..7 according to preceding-C bit. A C source cannot have age0.','For parallel Q-tail/U geometry, opposite travel begins contact at the old endpoint s=1, assigned to the outgoing atom; same travel begins at s=0 and closes with zero turn. Only ages2/6 survive, with no ambiguous pi-join ages0/4/8.','Actual complete Q/B contexts, not an F marker, give U-source filters. Age0/1 old-star effects use the signed early-star theorem; B(-3,6,W) at1 instead contradicts the same original recycled-q identity surviving until age2.'],'scope':'Necessary tail obligations only. The separate all-age B(3,0,E) exclusion is not silently folded into this immutable catalogue. No D/C/V tail closure, attained ancestry, global proxy simplicity or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(filtered)
