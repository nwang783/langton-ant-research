from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import json,hashlib,math
S=Path(__file__);R=S.parents[1];D=R/'old_V_all_tail_foreign_age3_pair_horizon_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='e78c5521d09401c1d33323c26fa62565b3ac28b3db81b5757e4c05110f2022ab'
for f,h in json.loads(MF.read_text())['files'].items():assert sha(D/f)==h
ref=json.loads((D/'V_n3.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,center,xy,cross,meet,pieces=[ns[x]for x in['W','M','K','tr','rot','center','xy','cross','meet','pieces']]
G={a:tr(W[a])for a in W};C={a:tr(W[a]+M)for a in W};I={a:{p for p,b in C[a]['req'].items()if b and p not in K}for a in W};r=0j;B=1+0j;CC=2+1j;bud=2+2j
ex=lambda a,p,h:(p+rot(h)*G[a]['p'],(h+G[a]['h'])%4)
def cut(a,p,h,t):q=(t-p)/rot(h);return q in K or C[a]['req'].get(q)is False
angles=json.loads((R/'one_foreign_first_contact_compression_2026-10-24/first_contact_C_window.json').read_text())['all44_exact_source_target_C_window_rows'];va=[x for x in angles if x['source_class']=='preFOREIGN_ordinary'and x['source_atom']=='V'];a=center(0j,0);u=center(G['V']['p'],G['V']['h'])-a;geo=[];counts=Counter()
for row in va:
 A=row['contact_atom'];assert 3 in row['allowed_C_counts_before_contact_ENTRY'];c=center(0j,3);ep,eh=ex(A,0j,3);v=center(ep,eh)-c;den=cross(u,v);assert den
 corners=[(a+s*u-c-t*v)/2 for s in[0,1]for t in[0,1]]
 for x in range(math.floor(min(z.real for z in corners)),math.ceil(max(z.real for z in corners))+1):
  for y in range(math.floor(min(z.imag for z in corners)),math.ceil(max(z.imag for z in corners))+1):
   if(x+y+3)%2:continue
   p=complex(x,y);q=c+2*p-a;s=F(cross(q,v),den);t=F(cross(q,u),den)
   if not(0<=s<1 and 0<t<=1):continue
   assert x>=0
   if cut(A,p,3,r)or cut(A,p,3,B):typ='pair'
   elif cut(A,p,3,CC):typ='C'
   else:assert(A,p)==('U',3+2j)and cut(A,p,3,bud);typ='bud'
   geo.append((A,x,y,3,str(s),str(t),typ));counts[typ]+=1
assert len(geo)==15 and counts==dict(pair=9,C=5,bud=1)
re={(z['actor'],*z['ENTRY']):z for z in ref['all15_outgoing_owned_W3_geometries_and_guard_routes']}
for A,x,y,h,s,t,typ in geo:z=re[(A,x,y,h)];assert(z['old_outgoing_s'],z['new_positive_t'])==(s,t)
normal=[]
for A in'FQB':
 for q in I[A]:
  p=-rot(1)*q;e,eh=ex(A,p,1);assert eh==3 and e.real<=0;normal.append((A,xy(q),[*xy(p),1],[*xy(e),eh]))
assert len(normal)==47
rr={(z['FOREIGN'],tuple(z['true_input'])):z for z in ref['all47_actual_FOREIGN_input_to_W_EXIT_normal_bounds']}
for A,q,p,e in normal:z=rr[(A,tuple(q))];assert z['actual_FOREIGN_ENTRY']==p and z['actual_W_RAW_EXIT']==e
# Derived endpoint count domain, not a prior word-index restriction.
horizons=[]
for A,x,y,h,s,t,typ in geo:
 tags=[r,B]+([CC]if typ=='C'else[bud]if typ=='bud'else[])
 for tag in tags:
  drop=int(tag.real)-x
  assert drop<=1
  layouts=[]
  for d in range(max(0,drop+1)):
   for v in range(max(0,drop//3+1)):
    for u in range(max(0,drop//4+1)):
     if d+3*v+4*u<=drop:layouts.append((d,v,u))
  assert all(v==u==0 and d<=1 for d,v,u in layouts);horizons.append((A,x,y,xy(tag),drop,layouts))
assert len(horizons)==36
for src in['V','VC','VCC']:
 z=tr(''.join(W[a]for a in src));ek={z['p']+rot(z['h'])*k for k in K}
 for tag in[r,B,CC,bud]:assert z['last'][tag]==G['V']['last'][tag]and z['last'][tag][0]=='R'and tag not in ek
cports=[];bports=[]
for A in'DVU':
 for q in I[A]:
  p=CC-rot(3)*q;e,eh=ex(A,p,3)
  if(int(p.real+p.imag)+3)%2:typ='sector'
  elif(A,p)==('U',3+2j):
   op=pieces('V')[0];ap=(center(p,3),center(e,eh));assert meet(*op,*ap)is not None;typ='earlier_contact'
  else:assert(A,p)==('U',4+1j)and cut(A,p,3,B);typ='held_B'
  cports.append((A,xy(q),[*xy(p),3],[*xy(e),eh],typ));pb=bud-rot(3)*q;eb,hb=ex(A,pb,3);assert eb.real<=2;bports.append((A,xy(q),[*xy(pb),3],[*xy(eb),hb]))
assert Counter(z[-1]for z in cports)==dict(sector=6,earlier_contact=1,held_B=1)and len(bports)==8
# Bind the actual ONE and TWO interfaces separately; neither needs an invented later atom.
one=json.loads((R/'seven_word_spatial_return_2026-10-23/first_foreign_first_returned_atom_simplicity_manifest.json').read_text());two=json.loads((R/'first_foreign_two_ordinary_simplicity_2026-10-24/manifest.json').read_text());assert 'Exactly'in one['scope']['next_atom']and 'TWO'in two['theorem']
out=dict(status='PASS old-V true foreign age3 and TOTAL ordinary contact3 pair-horizon slice',manifest=sha(MF),geometries=geo,classification=dict(counts),all47_foreign_input_exit_bounds=normal,all36_derived_horizons=horizons,C_rail=cports,bud_rail=bports,analytic_review=[
'True preforeign age n3 equals TOTAL target clock K3, so the postforeign prefix before actor is exclusively a zero-C W base rail. Actor itself may be C and is not parsed as a further completed packet.',
'All47 actual foreign heading-E inputs, including marker capture, have W exit x<=physical tag x. Every preceding zero-W D/V/U decreases x by1/3/4. The36 target-specific arithmetic bounds derive at most zero/one preceding D, or impossibility; no fixed actor index is assumed.',
'Use the actual ONE-RAW theorem for an immediate target and TWO-RAW theorem only if one real preceding RAW exists. The same real finalM supplies their required context, including a target C. No ungiven next RAW or completed G7 is inferred.',
'This proves COMPLETE r/B foreign MISS on candidate-compatible histories before invoking portable358+b84. Preforeign r5/B4 and C/bud552 ages remain strictly beforeFOREIGN; own V/VC/VCC tails preserve SAME births and internalRAW uses signed8d68. Nine simultaneous pair-input rows are excluded by earlier actual contacts, not color.',
'The pair earliest-loss totalK2 is earlier than actual foreign3. Its currentness cuts9 targets. C COMPLETE MISS is separately proved only for needed targets; its8 W loss roles give6sector,1 earlier oldV contact,1 held-B WHITE, cutting5. Last U3,2 target needs budWHITE, but every FORE and earlier W bud loss exitsx<=2 and cannot reachx3.',
'Only ENTRY currentness is claimed; target true-input consumption is retained until another independent contradiction. C has3 external first-WHITE capture sites and2 alreadyENTRYCORE sites, not5 first-WHITE. Other foreign ages, total clocks, old-source classes and arbitrary-tail simplicity remain open.'
],dependencies=ref['dependencies'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
