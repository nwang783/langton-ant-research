from pathlib import Path
from collections import defaultdict,Counter
import ast,json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'K1_pipeline_detours_2026-10-23';p=D/'prepared_D158_connected_late_parent_control.json';sha=hashlib.sha256(p.read_bytes()).hexdigest();assert sha=='3badc0e3791c4a459b4651b6b922a8d73086915ed14e3ce12e40ff06bd18fd70';a=json.loads(p.read_text());word=a['word'];seed={complex(*p)for p in a['prepared_black']};B=set(seed);p=1;h=0;dirs=(1j,1,-1j,-1);H='NESW';events=defaultdict(list);edges=[];trace=[]
for t,ch in enumerate(word):
 assert ch==('L'if p in B else'R');events[p].append((t,H[h],ch));trace.append({'time':t,'cell':[int(p.real),int(p.imag)],'incoming':H[h],'turn':ch});B.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;q=p+dirs[h];edges.append((p,q));p=q
assert(len(word),len(seed),p,h,len(B))==(158,37,-2+3j,0,25)
assert trace==a['trace']and B=={complex(*q)for q in a['final_black']}
assert Counter(word)=={'R':73,'L':85}and Counter(len(v)for v in events.values())=={4:17,3:7,2:20,1:29}
for field,index in[('complete_finite_headings',1),('complete_finite_turns',2)]:assert{str((int(q.real),int(q.imag))):''.join(v[index]for v in e)for q,e in events.items()}==a[field]
known={complex(*ast.literal_eval(k)):v for k,v in a['known_headings'].items()};assert len(known)==16 and not seed&known.keys()
for q,want in known.items():assert ''.join(h for t,h,ch in events[q])==want and ''.join(ch for t,h,ch in events[q])=='RLRL'and q not in B
faces={'D':0,'J':-1-1j,'P0':-2,'I':-1+1j,'G':1+1j};births={};full={}
for name,sw in faces.items():
 directed=[(sw+1,sw),(sw,sw+1j),(sw+1j,sw+1+1j),(sw+1+1j,sw+1)];first=[edges.index(e)for e in directed];births[name]=min(first);full[name]=first
 assert first==[r['first']for r in a['boundary_first_departures'][name]]
assert births=={'D':4,'J':9,'P0':24,'I':39,'G':43}
# Verify each stated birth is the actual second read L and its departure
# switches from the earlier face to the named new directed boundary.
for name,cell in{'D':1,'J':0,'P0':-1,'I':-1+1j,'G':1+1j}.items():assert events[cell][1][0]==births[name]and events[cell][1][2]=='L'
note=D/'prepared_D158_connected_late_parent_control.md';nsha=hashlib.sha256(note.read_bytes()).hexdigest();assert nsha=='cd93b2f0071b958fa5f4636cade12f7382561e1a92cb97e113742731310bf737'
out={'status':'PASS literal158-read connected prepared late-parent control','note_sha256':nsha,'input_json_sha256':sha,'seed_mass':37,'final_mass':25,'end_pose':[-2,3,0],'read_spectrum':dict(Counter(len(v)for v in events.values())),'R_L':dict(Counter(word)),'named_directed_boundary_first_reads':births,'all_boundary_first_reads':full,'scope':'Finite complete prepared board only. Sixteen designated initially white cells have exactly the specified RLRL histories, entire factor cap4. Directed first-boundary chronology D→J→P0→I is an actual continuous cursor. Not a global WHITE translating front, canonical maximum p graph, renewable input, repetition or capture claim.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
