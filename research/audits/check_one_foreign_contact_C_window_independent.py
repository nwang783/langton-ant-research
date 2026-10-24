from pathlib import Path
from fractions import Fraction as F
from itertools import product
from collections import Counter
import hashlib,json
S=Path(__file__).resolve();R=S.parents[1];D=R/'one_foreign_first_contact_compression_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'manifest.json';assert sha(man)=='94bea2fc176865c14d0c45b7cd42b4f3e03638048a22b552006862c12bcae018';mf=json.loads(man.read_text())
for p,h in mf['files'].items():assert sha(D/p)==h
for p,h in mf['dependencies'].items():assert sha(R/p)==h
ref=json.loads((D/'first_contact_C_window.json').read_text());ns={'__file__':str(S.with_name('check_foreign_kinked_barrier_turn_independent.py'))};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns);W,M,walk,center,xy=[ns[k]for k in('W','M','walk','center','xy')];tr={a:walk(W[a])for a in'DCVUFQB'}
vec=lambda a,h=0:xy((center(tr[a]['p'],tr[a]['h'])-center(0j,0))*(-1j)**h)
alpha={'D':(1,0),'C':(1,0),'V':(0,1),'U':(0,0)}
def plus(a,b):return(a[0]+b[0],a[1]+b[1])
def minus(a,b):return(a[0]-b[0],a[1]-b[1])
def mul(z,w):return(z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])
def powr(z,k):
 if k<0:
  n=z[0]*z[0]+z[1]*z[1];z=(F(z[0],n),F(-z[1],n));k=-k
 q=(F(1),F(0))
 for _ in range(k):q=mul(q,z)
 return q
def principal(u,v,ang):
 rot=(u[0]*v[0]+u[1]*v[1],u[0]*v[1]-u[1]*v[0]);q=mul(powr((1,1),ang[0]),powr((3,1),ang[1]));assert rot[0]*q[1]==rot[1]*q[0]and rot[0]*q[0]+rot[1]*q[1]>0
 lo,hi=sorted((ang[0],sum(ang)));assert lo>=-4 and hi<=4 and not(ang[1]==0 and abs(ang[0])==4)
 return ang
ordinary=[]
for a,b in product('DCVU',repeat=2):ordinary.append([a,b,principal(vec(a),vec(b,3 if a=='C'else 0),plus((2*(a=='C'),0),minus(alpha[a],alpha[b])))])
foreign={}
for A in'FQB':
 pts=[center(0j,0),center(tr['F']['p'],tr['F']['h'])]
 if A!='F':pts.append(center(tr[A]['p'],tr[A]['h']))
 foreign[A]=[xy(v-u)for u,v in zip(pts,pts[1:])]
assert foreign=={'F':[(-6,-2)],'Q':[(-6,-2),(0,-4)],'B':[(-6,-2),(2,-6)]}
last={'F':(2,-1),'Q':(0,0),'B':(0,-1)};splices=[];wrap=[];ends=[]
for a,A,b in product('DVU','FQB','DCVU'):
 pcs=foreign[A];q=principal(vec(a),pcs[0],plus((2,1),alpha[a]));z=q
 if A!='F':z=plus(z,principal(pcs[0],pcs[1],(2,-1)if A=='Q'else(2,0)))
 z=plus(z,principal(pcs[-1],vec(b,2),minus(last[A],alpha[b])));assert z==plus((4,0),minus(alpha[a],alpha[b]));splices.append([a,A,b,z])
for A,b in product('FQB','DCVU'):
 pcs=[(-y,x)for x,y in foreign[A]];z=principal(vec('C'),pcs[0],(-3,1))
 if A!='F':z=plus(z,principal(pcs[0],pcs[1],(2,-1)if A=='Q'else(2,0)))
 z=plus(z,principal(pcs[-1],vec(b,1),minus(last[A],alpha[b])));assert minus(plus((6,0),minus(alpha['C'],alpha[b])),z)==(8,0);wrap.append([A,b,z])
for A in'FQB':assert walk(W['C']+W[A]+M)['feasible']
for kind,AA,off in(('Fprefix','FQB',(2,-1)),('Qtail','Q',(0,0)),('Btail','B',(0,-1))):
 for A,b in product(AA,'DCVU'):
  z=minus(last[A],alpha[b])
  if kind=='Fprefix'and A!='F':z=plus(z,(2,-1)if A=='Q'else(2,0))
  assert z==minus(off,alpha[b]);ends.append([kind,A,b,z])
def inside(q):
 lo,hi=sorted((q[0],sum(q)))
 if lo>=4 and hi<=12 and not(q[1]==0 and q[0]in(4,12)):return True
 assert hi<=4 or lo>=12
 return False
windows=[]
for kind in('preFOREIGN_ordinary','postFOREIGN_ordinary','Fprefix','Qtail','Btail'):
 for a in('DCVU'if'ordinary'in kind else'-'):
  for b in'DCVU':
   if'ordinary'in kind:off=plus((4 if kind.startswith('pre')else 0,0),minus(alpha[a],alpha[b]))
   else:off=minus({'Fprefix':(2,-1),'Qtail':(0,0),'Btail':(0,-1)}[kind],alpha[b])
   # No searched horizon: offsets lie strictly above -2 quarters; for K>=8
   # lower open turn exceeds12 quarters. All possible K are in0..7.
   assert min(off[0],sum(off))>=-2 and not(off[1]==0 and off[0]<=-2)
   allow=[k for k in range(8)if inside(plus((2*k,0),off))and not(a=='C'and k==0)]
   row=dict(source_class=kind,source_atom=a,contact_atom=b,allowed=allow,offset=off);windows.append(row)
   rr=next(z for z in ref['all44_exact_source_target_C_window_rows']if z['source_class']==kind and z['contact_atom']==b and z.get('source_atom','-')==a);assert rr['allowed_C_counts_before_contact_ENTRY']==allow and rr['open_turn_offset_pi_over4_beta']==list(off)
assert(len(ordinary),len(splices),len(wrap),len(ends),len(windows))==(16,36,12,20,44)
counts={kind:sum(len(z['allowed'])for z in windows if z['source_class']==kind)for kind in('preFOREIGN_ordinary','postFOREIGN_ordinary','Fprefix','Qtail','Btail')};assert counts=={'preFOREIGN_ordinary':56,'postFOREIGN_ordinary':58,'Fprefix':16,'Qtail':15,'Btail':16}
out={'status':'PASS source-relative bounded C window for a first contact after one foreign','manifest':sha(man),'ordinary16':ordinary,'nonC_foreign36':splices,'CF_wrap12':wrap,'foreign_source20':ends,'windows44':windows,'window_label_counts':counts,'analytic_review':[
'All principal turns were independently reconstructed from literal corrected-center endpoint vectors by Gaussian-rational ray equality and strict coefficient bounds for0<beta<pi/4. Ordinary joins telescope, including negative joins. True Q/B use two real pieces and no invented internal marker. Actual complete8 adjacency supplies non-C before firstforeign; formal raw C-to-foreign introduces a full -2pi wrap and is physically feasible on prepared boards, so no raw grammar ban is substituted.',
'At the first later nonadjacent positive contact, the preceding open proxy is simple by the first-contact definition. No adjacent principal join is pi, so a zero-time retracing overlap is excluded. Outgoing-old-piece ownership handles old vertices; the former terminal point is the current segment start and cannot be revisited at positive time by one straight nonzero chord. Earliest collinear onset is retained, not discarded by a zero determinant.',
'The old-source-to-current-head subarc plus the partial new chord is a Jordan curve. If closing tangents were opposite, the initial outgoing old arc and final incoming new arc would lie on the same ray near the contact, creating an earlier overlap. This holds even when the new contact is its endpoint. Thus closing principal turn is strictly between-pi andpi; same-direction collinear onset has zero closing turn. Each exact open-turn expression is >-pi/2, excluding clockwise total-2pi. Hence pi<Topen<3pi, with strict endpoint refinements.',
'Preforeign ordinary sources include the foreign+pi and all actual C intervals from sourceENTRY to contactENTRY; postforeign sources do NOT include that earlier half-turn. SourceC itself counts, terminal contactC does not. Foreign-piece sources have the separately checked endpoint corrections. These conventions give the44 exact source/target windows, with no beta-dependent ambiguity or finite-depth assumption.',
'At most seven ordinary heading epochs follow from the C windows; their D/V/U lengths, spatial diameters and field resources remain unbounded. After five postforeign Cs no preforeign ordinary source remains; after seven no foreign-piece source remains. Later contacts may be to a recent postforeign source, including convex loops, and no old-U reflex enclosure is imported.',
'For an old genuine U source the source-relative window bounds true preforeign age<=4, so the separately signed preforeign MISS and conditional arbitrary-tail LEFT lemma apply at first-contact ENTRY only. All-four physical survival from the special CUT2 transfer is NOT iterated. No arbitrary-tail simplicity, new lifetime law, secondforeign extension, compact field quotient or capture conclusion is obtained.'
]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'],counts)
