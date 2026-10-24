"""Weak fresh RAW U SAME LEFT guard through source-relative C clock3.
No unnecessary K4 claim and no old-eight maturity transported across a foreign.
"""
from pathlib import Path
from fractions import Fraction as Q
from collections import Counter
import importlib.util,json,hashlib
R=Path('/workspace/shared/langton');H=Path(__file__).resolve().parent

def load(name,path):
 s=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(s);s.loader.exec_module(m);return m
l=load('literal',R/'word_stabilization/check_foreign_return_interfaces.py');o=load('owner',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py');W=o.WORDS

def add(p,q):return p[0]+q[0],p[1]+q[1]
def sub(p,q):return p[0]-q[0],p[1]-q[1]
def det(p,q):return p[0]*q[1]-p[1]*q[0]
def after(w,p=(0,0,0)):
 q,h=p[:2],p[2]
 for c in w:h=(h+(1 if c=='R'else-1))%4;q=add(q,l.DIRS[h])
 return*q,h

def z(p):return add((2*p[0],2*p[1]),l.rot((-1,-1),p[2]))
def chord(a,p):return z(p),z(after(W[a],p))
def contact(a,b,c,d):
 u,v,q=sub(b,a),sub(d,c),sub(c,a);de=det(u,v)
 if de:
  s,t=Q(det(q,v),de),Q(det(q,u),de)
  return dict(old_s=str(s),new_t=str(t),point=[str(Q(a[k])+s*u[k])for k in(0,1)])if 0<=s<=1 and 0<=t<=1 else None
 if det(q,u):return None
 k=0 if u[0]else 1;lo,hi=sorted((Q(c[k]-a[k],u[k]),Q(d[k]-a[k],u[k])))
 return dict(collinear_old_interval=[str(max(Q(0),lo)),str(min(Q(1),hi))])if max(0,lo)<=min(1,hi)else None
LEFT={(0,0),(0,1)};src=l.trace(W['U']);geo=l.literal_geometry(W['U']);assert LEFT<=set(map(tuple,geo['outputs']))and src['last'][(0,0)]==('R',4)and src['last'][(0,1)]==('R',19);old=chord('U',(0,0,0));rows=[]
for tag in sorted(LEFT):
 for atom in'DCVU':
  cg=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
  for slot in map(tuple,cg['inputs']):
   for hd in range(4):
    p=(*sub(tag,l.rot(slot,hd)),hd);q=dict(SAME_original_U_LEFT_cell=tag,consumer=atom,input_slot=slot,pose=p,physical_first_L_owner=o.describe(atom,tr['first'][slot][1]))
    if(sum(p[:2])+hd)%2:q['classification']='sector'
    else:
     bad=[]
     for held in sorted(LEFT):
      loc=l.rot(sub(held,p[:2]),-hd);f=tr['first'].get(loc)
      if loc in l.K or f and f[0]=='R':bad.append(dict(SAME_LEFT=held,local=loc,role='ENTRY_CORE'if loc in l.K else'first_WHITE',first=f))
     if bad:q.update(classification='SAME_LEFT_initial_CORE_or_WHITE',conflicts=bad)
     else:
      h=contact(*old,*chord(atom,p));assert p!=(0,4,0)
      if h:q.update(classification='nonadjacent_source_U_proxy_contact',contact=h)
      else:q['classification']='sole_noncontact_N_U_gate'
    rows.append(q)
assert len(rows)==64 and Counter(q['classification']for q in rows)=={'sector':32,'SAME_LEFT_initial_CORE_or_WHITE':18,'nonadjacent_source_U_proxy_contact':12,'sole_noncontact_N_U_gate':2}
keep=[q for q in rows if q['classification']=='sole_noncontact_N_U_gate'];assert all(q['consumer']=='U'and tuple(q['pose'])==(1,-1,0)for q in keep)
assert after(W['U'])==(0,4,0);zero=[]
for atom in'DVU':
 ep=after(W[atom]);assert ep[2]==0 and ep[0]>=0 and ep[1]>=1;zero.append(dict(atom=atom,N_zero_C_EXIT_increment=ep))
# Literal full source tail spelling is NOT needed: each own C is an actual
# next ordinary atom and counted in K. C has empty residual I.
assert l.literal_geometry(W['C'])['inputs']==[]
GP=R/'postforeign_V_rA_nonterminal_guardian_2026-10-24/rA_guardian.json';g=json.loads(GP.read_text());assert len(g['fresh_plain_RAW_current_edge_barrier'])==4
# Useful donor-reader interface, retained as a local current/core fact only.
reader=(1,0,1);core={add(reader[:2],l.rot(q,reader[2]))for q in l.K};assert LEFT<=core
paths=[GP,R/'postforeign_V_rA_nonterminal_guardian_2026-10-24/manifest.json',R/'audits/check_postforeign_V_pair_guardian_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FRESH_RAW_U_LEFT_EARLY_MINIMUM4_PENDING_REVIEW',scope='ANY genuinely fresh RAW U original LEFT pairR4/R19, possibly born AFTER a foreign; following ordinary RAW source-prefix is SIMPLE and has actual marker contexts. At actual source-relative C clocks0..3 both SAME tags remain CURRENT outsideCORE. No foreign between source and protected cut. No K4/all-age U persistence claim, old8 input-age law or fullG8 producer reset.',all64_plain_FIRST_CURRENT_loss_roles=rows,unique_noncontact_consumer_pose=dict(atom='U',pose=(1,-1,0),both_LEFT_TRUE_inputs_retained=True),deadline_proof='If a first loss completes by clock3 under the simple-prefix hypothesis, all other roles contradict initial held field/sector or cause an earlier source contact. Sole U gate headsN; actual ordinary K<=3 and headingN implyK0. Creating U RAW exits(0,4,N), and every later N zero-C base D/V/U raises y, so gateheady-1 is unreachable. Thus no first CURRENT loss completes by3.',all3_N_zero_C_generators=zero,CORE_qualification='Every actual first CURRENT loss is covered by a plain I slot, including marker-only RAWEXIT CORE absorption and recycled physical cells. True simultaneous LEFT inputs in the sole U gate are preserved. Replacements are not the SAME R4/R19 identities.',fresh_plain_RAW_current_edge_barrier=g['fresh_plain_RAW_current_edge_barrier'],source_births=[dict(cell=(0,0),R_tick0=4,birth_read_number1=5),dict(cell=(0,1),R_tick0=19,birth_read_number1=20)],donor_reader_local_corollary=dict(actual_reader_RAW='D',entry_relative_fresh_U=reader,both_CURRENT_LEFT_inside_entry_CORE=sorted(LEFT),statement='An actual reader at relative(1,0,E) by sourceage3 is impossible under the stipulated simple ordinary source-prefix, because its entry CORE contains genuine CURRENT LEFT tags. This is a current/core contradiction, not a BLACK-versus-L color contradiction.'),dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'fresh_U_LEFT.json').write_text(json.dumps(out,indent=2)+'\n');print('Fresh RAW U LEFT throughC3:64 roles=32sector+18 heldfield+12 sourcecontacts+2 simultaneous U1,-1N roles; N clock<=3 forces0, sourceEXITy4 blocks. No K4/all-age claim or old8 import.')
