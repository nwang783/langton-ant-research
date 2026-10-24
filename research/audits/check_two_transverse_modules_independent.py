from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'TWO_TRANSVERSE_MODULES_MANIFEST.json';assert sha(MF)=='3af037c60bc8a1bf4c8a7329e3de56cff6cce09622856a6467147f6cd9ad0b69';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
J=json.loads((D/'TWO_TRANSVERSE_MODULES_CHECKED.json').read_text())
for f,h in J['source_hashes'].items():assert sha(D/f)==h
ns={'__file__':str(S.with_name('check_transverse_far_module_independent.py'))};exec(Path(ns['__file__']).read_text().split('controls=[]')[0],ns)
verify,vec,xy,G,A,U,F,Z,protected,omega=[ns[k]for k in('verify','vec','xy','G','A','U','F','Z','protected','omega')];assert U==Z
fates={q:ns['death'].get(-i-1)for i,q in enumerate(sorted(protected,key=lambda q:(q.real,q.imag)))};relevant285={q for q,t in fates.items()if t is not None};assert len(relevant285)==285
ports=lambda n:[{p+r*q for q in G}for p,r in[(0j,1),(7*n-1+7*n*1j,1j),(5*n+(9*n-4)*1j,-1),(n+5+5*n*1j,-1j)]]
moduleword=lambda n:''.join(A+U*rr+U[:m]for rr,m in zip((7*n//2-4,n-5,2*n-6,n-6),(61,71,61,56)))
base=set.union(*ports(20));pre=moduleword(20);assert len(pre)==14393
controls=[]
for row in J['controls']:
 n,jj=row['n2'],row['spacing_periods'];assert(n,jj)in[(40,100),(80,200)];v=76+2*jj+(55-2*jj)*1j;transform=lambda q:v-1j*q;extra=set.union(*[{transform(q)for q in po}for po in ports(n)[1:]]);seed=base|extra;assert len(extra)==12 and len(seed)==28 and sorted(map(xy,seed))==row['initial_black']
 T=23379+104*jj;b1=3061;c1=14393;b2=T+156*n-241;c2=T+780*n-1389;onset=c2+8986;expected=pre+F+U*jj+moduleword(n)[182:]+F+U*2;N=len(expected);assert N==onset+208
 q1=60+63j;q2=transform(3*n+(3*n+3)*1j);snaptimes={0,b1+1,c1,23379,T,b2+1,c2,onset,N};B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda q:(q.real,q.imag)))};p=0j;h=1;deaths={};births={};first={};snaps={}
 for t,ch in enumerate(expected):
  if t in snaptimes:snaps[t]=(dict(B),p,h)
  if p in seed and p not in first:first[p]=t
  assert(ch=='L')==(p in B);old=B.get(p)
  if t in(b1,b2):assert p==(q1 if t==b1 else q2)and old is None
  if t in(c1,c2):assert(p,h,old)==((q1,2,b1)if t==c1 else(q2,3,b2))
  if ch=='L':deaths[B.pop(p)]=t;h=(h-1)%4
  else:B[p]=t;births[t]=p;h=(h+1)%4
  p+=vec[h]
 snaps[N]=(dict(B),p,h);word,d,ff,tests=verify(B,p,h);assert word==U and d==-2-2j;deaths.update({tag:N+t for tag,t in ff.items()})
 assert expected[onset-1]!=U[-1]and len({U[i:]+U[:i]for i in range(104)})==104
 assert(snaps[T][1],snaps[T][2])==(transform(5+1j),2)
 assert len(first)==28 and min(first[q]for q in extra)>T and max(first[q]for q in extra)<c2
 assert{tuple(r['cell']):r['first_read']for r in row['all_initial_first_reads']}=={tuple(xy(q)):t for q,t in first.items()}
 for r in row['all_initial_first_reads']:assert r['added']==(complex(*r['cell'])in extra)
 fields={t:{q for q,tag in bb.items()if tag in deaths}for t,(bb,pp,hh)in snaps.items()};assert fields[c1]=={q1+q for q in relevant285}|extra and len(fields[c1])==297
 inside={q-q1 for q in snaps[c1][0]if omega(q-q1)};added_inside={q-q1 for q in extra if omega(q-q1)};assert len(inside)==334 and inside==protected|added_inside and len(added_inside)==4 and sorted(map(xy,added_inside))==row['first_protected_field_added_cells']
 for q,dt in fates.items():assert deaths.get(snaps[c1][0][q1+q])==(None if dt is None else c1+dt)
 assert fields[c2]=={q2-1j*q for q in relevant285}and len(fields[c2])==285
 bb=set(base);pp=0j;hh=1
 for ch in pre:assert(ch=='L')==(pp in bb);bb.symmetric_difference_update({pp});hh=(hh+(1 if ch=='R'else-1))%4;pp+=vec[hh]
 assert set(snaps[c1][0])==bb|extra and len(snaps[c1][0])==1745
 for snap in row['complete_snapshots']:
  t=snap['cut'];bb,pp,hh=snaps[t];assert snap['pose']==[xy(pp),hh]and snap['full_mass']==len(bb)and snap['relevant_mass']==len(fields[t])
  actual={(tuple(xy(q)),tag,deaths.get(tag))for q,tag in bb.items()};assert actual=={(tuple(r['cell']),r['lifetime'],r['death'])for r in snap['full_black']}
 L=sum(tag in deaths for tag in range(-28,0));assert L==28;prof=[L]
 for t,ch in enumerate(expected):L+=int(t in deaths)if ch=='R'else-1;prof.append(L)
 assert max(prof)==444 and max(prof[T:])==432 and len(fields[b2+1])==222
 permanent=[sum(expected[t]=='R'and t not in deaths for t in range(b+1,c))for b,c in[(b1,c1),(b2,c2)]];assert permanent==[1286,72*n-154]
 CC=dict(B);pp=p;hh=h;later={};events=[]
 for k in range(104):
  old=CC.pop(pp,None);events.append(old)
  if old is None:CC[pp]=N+k;hh=(hh+1)%4
  else:later[old]=k;hh=(hh-1)%4
  pp+=vec[hh]
 w2,d2,f2,tests2=verify(CC,pp,hh);assert(w2,d2)==(word,d);later.update({tag:104+t for tag,t in f2.items()});C0={q for q,tag in B.items()if tag in ff};C1={q for q,tag in CC.items()if tag in f2};assert C1=={q+d for q in C0}
 L=len(C0);tp=[L]
 for k,old in enumerate(events):L+=int(N+k in later)if old is None else-1;tp.append(L)
 assert tp==row['infinite_tail_relevant_profile']and max(tp)==22
 controls.append(dict(second_n=n,spacing=jj,actual_updates=N,second_launch=T,first_contact=c1,second_contact=c2,exact_final_onset=onset,full_contact_masses=[len(snaps[c1][0]),len(snaps[c2][0])],relevant_contact_masses=[297,285],whole_future_relevant_max=444,first_added_input=min(first[q]for q in extra),marked_ages=[c1-b1,c2-b2],actual_permanent_births=permanent,terminal_parity_tests=tests,tail_relevance_max=22))
out=dict(status='PASS two literal28-cell full-board causal moving-return concatenations, with all12 extra initial inputs charged',manifest_sha256=sha(MF),script_sha256=sha(S),source_audit=sha(S.with_name('check_transverse_far_module_independent.json')),controls=controls,analytic_review=[
'Both exact28-cell seeds were rebuilt from independent rotatedG ports. Every72784/114384 physical update, actual cursor, full snapshot and current lifetime death was independently replayed, followed by full all-period ray parity. The second launch starts at the actual rotated reference cut182, not an invented G reset.',
'All12 extra bits are original and first read strictly after the actual second U-phase entry; all are consumed before the second marked death. First whole field is isolatedS20 plus12, while its infinite protected strip has334 rather than330 black cells. Thus the old infinite capture premise fails genuinely; the shared finite8986 recovery cannot be called a first capture.',
'Every original protected330 lifetime keeps its exact eventual fate. First ENTIRE relevance is285+12=297, not285. Second entire relevant field is the rotated285 pattern and really captures. Identical local field is therefore distinguished from identical full future-relevant state.',
'First/second genuinely R-born consumed lifetimes have ages11332 then23812/48772, with all intermediate old archive retained. Actual permanent birth counts1286 and2726/5606 use the whole future, never template predictions. Finite profilemax444 plus explicit translated-pruned tail closure(max22) proves the all-future444 bound.',
'Only these two literal seeds are certified. The supplied longer second return spends12 added initial inputs; no fresh reproduction, infinite autonomous regeneration, all-parameter concatenation or failure of eventual per-orbit bounded age/capture follows.'
]);S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')))
