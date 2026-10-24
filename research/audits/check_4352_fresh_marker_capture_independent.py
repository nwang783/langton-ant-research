"""Complete original395-cell M1 replay and full-board future-tail certification."""
from pathlib import Path
from collections import defaultdict
import hashlib,json
SELF=Path(__file__).resolve();R=SELF.parents[1];P=R/'causal_reduction/unit_scale';V=((0,1),(1,0),(0,-1),(-1,0))
J=json.loads((P/'prepared4352_two_phase_manifest.json').read_text());E=json.loads((P/'prepared4352_fresh_marker_M1_entry.json').read_text());A=json.loads((P/'prepared4352_fresh_marker_M1_capture.json').read_text());H=json.loads((R/'deliverables/constant_184_capturing_family/family_data.json').read_text())['standard_word']
marker=(108,105);seed={(sum(x),sum(y))for x,y in J['seed_families']}|{marker};assert len(seed)==395 and seed==set(map(tuple,E['original_seed']))
p=(295,270);h=3;B=set(seed);history=[];first={};snap={};times={E['time'],A['capture_time'],*[e['time']for e in A['events']]}
for t in range(A['capture_time']+1):
 if t in times:snap[t]=set(B),p,h
 if t==A['capture_time']:break
 c='L'if p in B else'R';first.setdefault(p,c);history.append(c);B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=tuple(p[j]+V[h][j]for j in (0,1))
word=''.join(history);prefix=''.join(s['word']*sum(s['count_N_constant'])for s in J['stages']);assert len(prefix)==584941 and word[:len(prefix)]==prefix
returnword=J['stages'][-1]['word'];assert word[584941:585030]==returnword[:89]and word[585030]=='L'and returnword[89]=='R'
b,q,g=snap[E['time']];assert(q,g)==(marker,1)and len(b)==50081 and b==set(map(tuple,E['field_before_marker']))
assert word[E['time']:]==A['continuation_word']and len(word)==707402 and (p,h)==((18,105),1)and len(B)==54177
assert B==set(map(tuple,A['final_field']))and {q for q,c in first.items()if c=='L'}==seed
hashfield=lambda b:hashlib.sha256(json.dumps(sorted(b),separators=(',',':')).encode()).hexdigest();assert hashfield(B)==A['final_field_sha256']
s=SELF.with_name('check_prepared1564_connected_capture_independent.py').read_text();exec(compile(s[s.index('def periodic('):s.index('reports=[]')],str(SELF),'exec'))
reports=[]
for e in A['events']:
 b,q,g=snap[e['time']];w=e['word'];assert w in{H[i:]+H[:i]for i in range(104)}and e['pose']==[list(q),g]and e['mass']==len(b)
 failure,d,G,n=periodic(b,q,g,w);assert failure==e['next_mismatch']
 if failure is not None:assert word[e['time']:e['time']+failure]==(w*((failure+103)//104))[:failure]and word[e['time']+failure]!=w[failure%104]
 reports.append(dict(time=e['time'],failure=failure,pose=e['pose'],drift=d,critical_tests=n))
w=A['capture_word'];failure,d,G,n=periodic(B,p,h,w);assert failure is None and d==(-2,2)
for a in G:assert periodic(B^{(a[0]+1000000*d[0],a[1]+1000000*d[1])},p,h,w)[0]is not None
# The distant new marker cannot affect the true ten-step reverse history.
assert abs(295-marker[0])+abs(270-marker[1])>10
allowed={(H*2)[i:i+10]for i in range(104)};stream='LRLRRRRLLL'+word+w[:10];K=sum(stream[i:i+10]not in allowed and stream[i+1:i+11]not in allowed for i in range(len(word)+10));assert K==A['total_K']==157079
out=dict(status='PASS complete original395-cell M1 fresh-marker capture',source_sha256=hashlib.sha256((P/'prepared4352_fresh_marker_M1_capture.json').read_bytes()).hexdigest(),literal_reads=len(word),first_L_equals_seed=True,initial_mass=395,marker_read_time=585030,marker_pose=(marker,1),capture_pose=(p,h),capture_mass=len(B),final_field_sha256=hashfield(B),total_K=K,events=reports,tail_orbits=len(G),tail_critical_tests=n,all_orbit_far_flip_rejections=len(G),scope='Only the specified original M1 board plus one preloaded marker. ALL-M marker ownership is separately signed; no ALL-M modified future or new prepared phase is inferred.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
