"""Fresh RAW V r first-loss clock with NO foreign between birth and loss.
Pure ordinary RAW support; no old-eight input-age law transported across a foreign.
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
r=(0,0);E=(-1,-1);L=(1,1);source=l.trace(W['V']);assert source['last'][r]==('R',4)and list(r)in l.literal_geometry(W['V'])['outputs'];old=chord('V',(0,0,0));assert contact(*old,L,E)==dict(old_s='0',new_t='1',point=['-1','-1'])
rows=[]
for atom in'DCVU':
 geo=l.literal_geometry(W[atom]);tr=l.trace(W[atom]+l.M)
 for slot in map(tuple,geo['inputs']):
  for hd in range(4):
   p=(*sub(r,l.rot(slot,hd)),hd);rec=dict(consumer=atom,input_slot=slot,pose=p,actual_input_first_read=o.describe(atom,tr['first'][slot][1]))
   if(sum(p[:2])+hd)%2:rec['classification']='unreachable_sector'
   else:
    h=contact(*old,*chord(atom,p));assert p!=(1,3,0)
    if h:rec.update(classification='nonadjacent_source_V_proxy_contact',contact=h)
    else:rec['classification']='noncontact_marker_r_loss_gate'
   rows.append(rec)
assert len(rows)==32 and Counter(q['classification']for q in rows)=={'unreachable_sector':16,'nonadjacent_source_V_proxy_contact':13,'noncontact_marker_r_loss_gate':3}
gates=[]
for atom,p in(('D',(1,0,3)),('V',(3,0,3)),('U',(4,1,3))):
 assert any(q['classification']=='noncontact_marker_r_loss_gate'and q['consumer']==atom and tuple(q['pose'])==p for q in rows);ep=after(W[atom],p);assert ep==(0,1,3)and z(ep)==L;h=contact(*chord(atom,p),L,E);assert h==dict(old_s='1',new_t='0',point=['1','1']);loc=l.rot(sub(r,p[:2]),-p[2]);tr=l.trace(W[atom]+l.M);assert loc not in l.trace(W[atom])['first']and tr['first'][loc]==('L',len(W[atom])+1)
 od={'D':(-1,1),'V':(0,0),'U':(0,1)}[atom];cl={'D':(-1,-1),'V':(-2,0),'U':(-2,-1)}[atom];assert tuple(od[k]+cl[k]for k in(0,1))==(-2,0)
 gates.append(dict(consumer=atom,pose=p,actual_RAW_EXIT=ep,corrected_EXIT=L,SAME_r_physical_L=o.describe(atom,len(W[atom])+1),r_current_loss_at_RAW_EXIT_CORE_not_physical_death=True,consumer_bridge_contact=h,open_delta_pi_over4_beta=od,closing_pi_over4_beta=cl,exact_total_turn='(K-1)*pi/2',Jordan_nonnegative_K=[5]))
# Rebind the independently signed plain RAW survivor-edge proof, not the
# restricted-language corollary of the older1822 note.
GP=R/'postforeign_V_rA_nonterminal_guardian_2026-10-24/rA_guardian.json';g=json.loads(GP.read_text());barriers=g['fresh_plain_RAW_current_edge_barrier'];assert len(barriers)==4
paths=[GP,R/'postforeign_V_rA_nonterminal_guardian_2026-10-24/manifest.json',R/'audits/check_postforeign_V_pair_guardian_independent.json',R/'one_foreign_first_contact_compression_2026-10-24/manifest.json',R/'audits/check_one_foreign_contact_C_window_independent.json',R/'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py'];assert all(p.exists()for p in paths)
out=dict(status='AUTHOR_FRESH_RAW_V_r_ZERO_FOREIGN_FIVE_C_GUARD_PENDING_REVIEW',scope='ANY genuine fresh RAW V R4 identity r, possibly born AFTER a foreign, followed only by actual ordinary D/C/V/U RAW atoms with actual markers. If the source-to-first-r-loss proxy is SIMPLE through that loss RAW, first CURRENT loss requires exactly K5 actual Cs from sourceV ENTRY to consumer ENTRY. No foreign occurs between source and loss. No U-entry or fullG8 producer assumption, no postforeign old age law.',genuine_source_R_birth=dict(cell=r,actual_SOURCE_RAW='V',birth_tick0=4,birth_read_number1=5,outside_actual_RAW_EXIT_CORE=True),all32_plain_first_CURRENT_loss_roles=rows,all3_marker_loss_Jordan_interfaces=gates,source_whole_chord_only_bridge_contact=contact(*old,L,E),fresh_plain_RAW_current_edge_barrier=barriers,analytic_Jordan='SAME r edge L1,1->E-1,-1 closes the source-V whole chord and future simple ordinary subarc through first loss. Source and final consumer touch bridge only at E/L, and it is current at every intervening cut. Every ordinary join has the signed principal lift. With beta=atan(1/3), open+closing=(K-1)pi/2, so Jordan and K>=0 forceK5. There is NO added foreign half-turn: a foreign before this newly born source is outside the closed subarc.',CURRENT_CORE_qualification='The three consumers meet r only at their common RAW EXIT0,1W. Original r is still physically alive in CORE there; the following actual word tick1/read2 deletes it. CORE absorption is already CURRENT loss. A recolored replacement is not the R4 identity.',corollary='At any actual simple ordinary source-prefix cut with source-relative C clock0..4, this SAME fresh r remains CURRENT, provided the stipulated actual marker contexts hold. Own source C tails are just subsequent actual C atoms in K, not a shifted full-producer clock.',attainment_not_asserted=True,no_old_G8_maturity_or_selected_parent_potential_or_arbitrary_foreign_extension=True,dependencies={str(p.relative_to(R)):hashlib.sha256(p.read_bytes()).hexdigest()for p in paths})
(H/'fresh_r.json').write_text(json.dumps(out,indent=2)+'\n');print('Fresh RAW V r:32 roles=16sector+13 true sourcecontacts+3 W marker gates; SAME-r edge Jordan gives zero-between-foreign K5. CURRENT through actual clocks0..4 under simple ordinary prefix; no oldG8 age import.')
