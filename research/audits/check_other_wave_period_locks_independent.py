from pathlib import Path
from collections import Counter,deque
import hashlib,json
ROOT=Path('/workspace/shared/langton');P=ROOT/'causal_reduction/unit_scale';D=ROOT/'new_constructive_2026-10-23';SELF=Path(__file__).resolve();m=json.loads((P/'prepared1564_uniform_support_manifest.json').read_text());assert hashlib.sha256((P/'prepared1564_uniform_support_manifest.json').read_bytes()).hexdigest()=='90fcf1a66046418c38d07f7e935ea80cf873751aefae69a4b07af89ba3bd8399'
dirs=(1j,1,-1j,-1)
def odd(word,p,h,n):
 counts=Counter()
 for c in word:
  counts[int(p.real-p.imag),int(p.real)%n]+=1;h=(h+(1 if c=='R'else-1))%4;p+=dirs[h]
 return {q for q,k in counts.items()if k%2}
# Rebuild ALL seven actual writer lanes from the signed affine stages.
initial=set();lanes=[]
for stage in m['stages']:
 if stage['kind']!='H':continue
 x=stage['start_x_N_constant'];y=stage['start_y_N_constant'];assert x[0]%2==y[0]%2==0 and x[0]==y[0]
 lane=odd(stage['word'],complex(x[1],y[1]),stage['heading'],2);assert len(lane)==12
 lift={(t,a+2*k)for t,a in lane for k in range(7)};assert not initial&lift;initial|=lift;lanes.append(lane)
assert len(lanes)==7 and len(initial)==588
wave=m['stages'][-1];S=initial^odd(wave['word'],-6-6j,0,14);assert len(S)==692
endpoint=json.loads((P/'prepared1564_source_endpoint_family.json').read_text());tail=odd(endpoint['capture_word'],-104-24j,0,2);assert len(tail)==12
lift={(t,a+2*k)for t,a in tail for k in range(7)};assert not S&lift;E=S|lift;assert len(E)==776
refsource=json.loads((P/'prepared1564_actual_output_consumers.json').read_text());assert S=={tuple(q)for q in refsource['backgrounds']['seven_writer_output']['black_mod14']}and E=={tuple(q)for q in refsource['backgrounds']['seven_writer_output_plus_endpoint_lane']['black_mod14']}
F={tuple(q)for q in json.loads((P/'prepared15324_return_normal_form.json').read_text())['bulk_mod26']};assert len(F)==964
sources=[(14,S,(-40,8)),(14,E,(-40,8)),(26,F,(15,20))];ref=json.loads((D/'other_wave_core_period_locking.json').read_text());reports=[]
for(n,field,band),rr in zip(sources,ref['results']):
 lower=min(t for t,a in field)-2;upper=max(t for t,a in field)+2;parts=[]
 for g in range(1,n):
  if n%g:continue
  allowed=lambda v:len({(v[0],a)in field for a in range(v[1],n,g)})==1
  seeds={(t,a)for t in range(band[0],band[1]+1)for a in range(g)if allowed((t,a))};seen=set();comps=[]
  for root in sorted(seeds):
   if root in seen:continue
   pot={root:0};todo=deque([root]);seen.add(root)
   while todo:
    v=todo.popleft();assert lower<v[0]<upper
    t,a=v;point=complex(a,a-t)
    for direction in dirs:
     p=point+direction;x,y=int(p.real),int(p.imag);w=(x-y,x%g);lift=x//g
     if not allowed(w):continue
     if w in pot:assert pot[w]==pot[v]+lift
     else:pot[w]=pot[v]+lift;seen.add(w);todo.append(w)
   comps.append(pot)
  r=next(x for x in rr['divisors']if x['g']==g);assert len(seeds)==r['central_vertices']and len(comps)==len(r['central_components'])
  for c in comps:
   match=[x for x in r['central_components']if{tuple(v[:2])for v in x['potential']}==set(c)];assert len(match)==1;other={(t,a):z for t,a,z in match[0]['potential']};assert len({c[v]-other[v]for v in c})==1
  mixed={(t,a)for t in range(lower,upper+1)for a in range(g)if not allowed((t,a))};assert mixed=={(t,a)for t,a,b,w in r['mixed_witnesses']}
  for t,a,b,w in r['mixed_witnesses']:assert b%g==w%g==a and(t,b)in field and(t,w)not in field
  parts.append(dict(g=g,central=len(seeds),components=len(comps),full_potentials=[[[t,a,z]for(t,a),z in sorted(c.items())]for c in comps]))
 reports.append(dict(period=n,black_classes=len(field),ribbon=band,divisors=parts))
sha=hashlib.sha256((D/'other_wave_core_period_locking.md').read_bytes()).hexdigest();assert sha=='106d67ae82bec263b9418c63e70476541705d9cfe3394738213205a211d21bfa'
out=dict(status='PASS complete source profiles and infinite-quotient arithmetic locks',note_sha256=sha,seven_actual_lanes=[sorted(x)for x in lanes],endpoint_lane=sorted(tail),reports=reports,scope='14-divisible full parallel stride for either complete1564 output touching[-40,8];26-divisible stride for complete4352 output touching[15,20]. Arbitrary finite caps/transients allowed, exact infinite-profile necessity only.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print([(r['black_classes'],[(x['g'],x['central'],x['components'])for x in r['divisors']])for r in reports])
