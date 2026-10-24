from pathlib import Path
from fractions import Fraction as F
import json,hashlib,math
S=Path(__file__).resolve();R=S.parents[1];P=R/'U_second_V_clock3_reflex_guard_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='25dd1d41e5f4516f02aae8864977e6a17471013fb1e87d802b43d7e9922f3546';m=json.loads(mf.read_text())
for f,h in m['files'].items():assert sha(P/f)==h
ref=json.loads((P/'clock3_reflex_guard.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
n={'__file__':str(S.with_name('check_second_ordinary_small_interface_independent.py'))};exec(Path(n['__file__']).read_text().split('triples=[]')[0],n);W,M,walk,center,xy,meet,pose,chord,pieces,tr=[n[k]for k in('W','M','walk','center','xy','meet','pose','chord','pieces','tr')]
start=(-1,-1);end=(-1,7);B=(-1,3);inc={}
for h in range(4):
 inc[h]={a:xy(tr[a]['p']*(-1j)**h)for a in'DVU'}
assert all(y>=0 for a,(x,y)in inc[0].items())and all(y>=0 for a,(x,y)in inc[3].items())
assert all(y<=0 for a,(x,y)in inc[2].items())and all(y<=0 for a,(x,y)in inc[1].items())
Cdata={h:{'delta':xy(tr['C']['p']*(-1j)**h),'chord':chord('C',0j,h)}for h in range(4)}
assert Cdata[0]['delta']==(0,1)and Cdata[3]['delta']==(-1,0)and Cdata[2]['delta']==(0,-1)
rows=[]
for a,p in(('Q',5+0j),('B',6+1j)):
 pcs,pp,pts=pieces(a,p,1);c1=chord('C',*pp);pp2=pose('C',*pp);c2=chord('V',*pp2);assert pp2==(4j,2) and c1==((3,7),(1,9))and c2==((1,9),B)
 hit=meet(start,end,*c2);assert hit==(F(1,2),F(1),B)
 for z in pcs+[c1]:assert meet(start,end,*z)is None
 assert pts==([(9,1),(7,7),(3,7)]if a=='Q'else[(11,3),(9,9),(3,7)])
 lo=min(q[1]for seg in pcs+[c1,c2]for q in seg);assert lo==(1 if a=='Q'else 3)
 # Interior CCW sector sweeps from outgoing N to reversed incoming V through the reflex side.
 outgoing=1j;reverseincoming=1+3j;oldreverse=-1j
 angle=lambda z:math.atan2(z.imag,z.real)%(2*math.pi)
 sector=(angle(reverseincoming)-angle(outgoing))%(2*math.pi);oldangle=(angle(oldreverse)-angle(outgoing))%(2*math.pi)
 beta=math.atan(F(1,3));assert math.pi<sector<2*math.pi and 0<oldangle<sector and abs(sector-(2*math.pi-beta))<1e-12
 open_turn=3*math.pi-beta;close=-math.pi+beta;assert abs(open_turn+close-2*math.pi)<1e-12
 rows.append({'foreign':a,'pieces':pcs+[c1,c2],'exact_contact':('1/2','1',B),'whole_loop_min_y2':lo,'U_start_y2':-1})
out={'status':'PASS two true-clock3 old-U FIRST second-contact reflex obstructions','manifest':sha(mf),'literal_zeroC_head_increments':inc,'literal_C_increments':Cdata,'cases':rows,'analytic_review':[
'The secondV terminal is the strict midpoint of the actual oldU chord, parameters1/2 and1. Prior simple proxy through b1 plus chronological FIRST b2 contact makes the forward B-to-B subarc a Jordan loop. True preforeign C count3 plus actual firstRAW C gives effective count4; actual preceding-C bit0 supplies the repaired-foreign lift. Open3pi-beta and closing-pi+beta give CCW2pi, not the oldU general arbitrary-tail reflex heuristic.',
'The bounded interior at B is the CCW reflex sector from outgoingN to reversed incomingV=(1,3), angle2pi-beta. The actual oldU reverse half pointsS strictly inside. It cannot leave or touch the rest of the boundary: old/old, old/foreign and old/b1 contacts violate prior simplicity, and old/b2 contact before B violates FIRSTcontact. Thus the genuine oldU start, not a hypothetical historical wire, is strictly in the bounded component.',
'Whole-loop support is reconstructed for unbounded zero-C runs. After sourceU, N0 heady>=4 and correctedY>=7; actual C1 raises heady1 and W1 correctedY>=9. W zero-C increments have nonnegativey; C2 has head dy0 and its two corrected endpoints are2y-1 and2y+1, so its minimum is>=9. This explicitly avoids mistaking its rising corrected chord for monotonic decrease. S2 heads are nonincreasing toward the final S head; C3 lowers heady1 before E3. E3 heads are nonincreasing toward foreign yA. Therefore all S2/C3/E3 endpoints have correctedY>=2yA+1. Source U remainder has Y>=3. Zero-length phases and source-own C tails obey the same atomic increments.',
'Exact repaired Q/B plus b1C/b2V pieces have minima1/3; hence the entire respective Jordan loop is contained in Y>=1/3, while oldU start hasY=-1. Its downward ray is disjoint from the boundary, placing it in the unbounded component, contradiction. No enclosure-only argument, exterior assumption, old identity or postforeign maturation is used.',
'Only Q5,0E,C,V0,4S and B6,1E,C,V0,4S at true preforeign age3 and chronological FIRST new contact are excluded. Other headings, clocks, later contacts and arbitrary-tail simplicity are not covered.'
]};S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
