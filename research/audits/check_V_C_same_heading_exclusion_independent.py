from pathlib import Path
from collections import Counter
from fractions import Fraction
import hashlib,json
SELF=Path(__file__).resolve();ns={'__file__':str(SELF.parent/'check_U_first_helper_ports_independent.py')};exec((SELF.parent/'check_U_first_helper_ports_independent.py').read_text().split('rows=[];gates=[];adjacent_rejects=[]')[0],ns)
globals().update({k:ns[k]for k in('ROOT','G','IDS','xy','rotation','chords','meet','pt','edge','walk','raws','mark','K')})
BUNDLE=ROOT/'core_periodicity_new/V_C_same_heading_exclusion_frozen_20261023_2043';man=json.loads((BUNDLE/'manifest.json').read_text())
for p,h in man['files'].items():assert hashlib.sha256((BUNDLE/p).read_bytes()).hexdigest()==h
A=1j;B=1;C=2+1j;rows=[];cases=[];adjs=[]
def bad(s,a,p,h):
 src=chords(s);dst=chords(a,p,h)
 for j,old in enumerate(src):
  for k,new in enumerate(dst):
   hit=meet(*old,*new)
   if hit:
    allow=j==len(src)-1 and k==0 and(p,h)==(G[s]['end'],G[s]['h'])and hit=={pt(old[1])}
    if allow:adjs.append([s,a,*xy(p),h])
    else:return True
 return False
for s in(4,5,6):
 for z in(A,B):
  for a in IDS:
   for h in range(4):
    for local in G[a]['I']:
     p=z-rotation(local,h);ctx={p+rotation(q,h)for q in G[a]['ctx']};row=dict(source=s,source_output=xy(z),consumer=a,head=[*xy(p),h])
     if(sum(xy(p))+h)%2:why='wrong_sector'
     elif 0j in ctx:why='causally_held_r_context'
     elif bad(s,a,p,h):why='past_source_chord_contact'
     else:
      why='exact_A_age2_or_B_age4'
      if z==A:
       assert(a,p,h,local)in((4,4j,2,3j),(5,4j,2,3j),(7,-1+5j,2,-1+4j),(8,-1+5j,2,-1+4j))
       path=[-1+3j,2j];start=2j;n=2
       sub='upper_min5_excludes'if a>=7 else'only_V_or_VC_lower_A_survives'
      else:
       assert(a,p,h)in[(v,1-1j,0)for v in(0,1)]+[(v,1-3j,0)for v in(4,5)]+[(v,2-2j,0)for v in(7,8,9)]+[(v,2-4j,0)for v in(7,8)]
       path=[3-1j,1+1j,-1-1j];start=-1-1j;n=4
       if a>=7 and local==-1+4j:sub='upper_min5_excludes'
       elif a>=7:
        sub='consumes_original_C_simultaneously';assert C in{p+rotation(q,h)for q in G[a]['I']}
       elif a in(0,1):sub='repeats_future_C_consumer_entry'
       else:sub='V_helper_leaves_A_child_in_future_core'
      end=path[0];cc=chords(a,p,h)[0];assert meet(*cc,end,end+1)=={pt(end)} # end on actual base
      for i,(u,v)in enumerate(zip(path,path[1:])):
       assert meet(cc[0],end,u,v)==({pt(end)}if i==0 else set())
       for j,(x,y)in enumerate(chords(s)):
        if j==0:x=start
        assert meet(x,y,u,v)==({pt(start)}if i==len(path)-2 and j==0 else set())
      row.update(forced_C_age=n,subreason=sub);cases.append(row)
     row['reason']=why;rows.append(row)
ref=json.loads((BUNDLE/'V_C_same_heading_exclusion.json').read_text());key=lambda r:(r['source'],tuple(r['source_output']),r['consumer'],tuple(r['head']))
refs={key(r):r for r in ref['rows']}
for r in rows:
 z=refs[key(r)];assert r['reason']==z['reason']
 if'forced_C_age'in r:assert r['forced_C_age']==z['forced_C_age']and r['subreason']==z['subreason']
cnt=Counter(r['reason']for r in rows);assert len(rows)==552 and len(cases)==37 and cnt==ref['counts']
# Exact symbolic principal turns, alphaV in(1,2) in pi/4 units.
def turns(ang):
 out=[]
 for (a,b),(c,d)in zip(ang,ang[1:]):
  co=c-a;off=d-b
  while co*Fraction(3,2)+off<=-4:off+=8
  while co*Fraction(3,2)+off>=4:off-=8
  assert all(-4<=co*x+off<=4 for x in(1,2))and -4<co*Fraction(3,2)+off<4;out.append((co,off))
 return out,(sum(x for x,y in out),sum(y for x,y in out))
At=[];Bt=[]
for ac in[(1,0),(0,2)]:
 tr,total=turns([(ac[0],ac[1]+4),(0,7),(1,0)]);assert total==(1-ac[0],4-ac[1]);At.append(tr)
for ac in[(0,1),(1,0),(0,2)]:
 tr,total=turns([ac,(0,3),(0,5),(1,0)]);assert total==(1-ac[0],-ac[1]);Bt.append(tr)
assert[n for n in range(20)if 2*n+4 in(-8,8)]==[2]and[n for n in range(20)if 2*n in(-8,8)]==[4]
# Held A halfedge is a subset of the true A edge. B bridge is two true edges.
assert meet(*edge(A),-1+3j,2j)=={pt(-1+3j),pt(2j)};assert set(edge(B))=={3-1j,1+1j};assert set(edge(0j))=={1+1j,-1-1j}
P=1-1j;H=1-3j;child=H+A
for typ in(4,5):
 req={P+rotation(q,0):b for q,b in walk(raws[typ]+mark)[2].items()};assert req[B]is False and B not in{P+q for q in G[typ]['I']}
 assert child in{H+q for q in G[typ]['O']};assert child in{P+q for q in K}and child not in{P+q for q in G[typ]['I']}
 target=chords(typ,P,0)[0]
 for clearer in(4,5):assert chords(clearer,H+4j,2)[0]==tuple(reversed(target))
for typ in(4,5):
 assert C-(1+2j)==1-1j and C-rotation(1+2j,2)==3+3j
assert 3+3j+rotation(3+3j,2)==0j
out=dict(status='PASS same-heading V-base C to V/VC exclusion and no two ordinary parallel child edges',manifest_sha256=hashlib.sha256((BUNDLE/'manifest.json').read_bytes()).hexdigest(),counts=dict(cnt),rows=rows,cases=cases,retained_adjacencies=adjs,A_closing_turns=At,B_closing_turns=Bt,analytic='Causal r lock is valid through original A/B retirement, excluding simultaneous r retirement. Held halfedge/two-edge bridges plus literal source tails and target prefixes yield exact full-source-entry ages2/4. Upper min5 removes U upper cases. A later C-selected same-heading V/VC requires B already white; D/DC repeats target entry, lower-q U consumes C, remaining V/VC helper creates A in target core. The only A clearer reverses the entire later V chord. Only opposite-heading(3,3) selected transfer remains, and two such edges return the original corrected center.',scope='Simple-center complete-eight factor. VCC distinguished lower-input transfers, C-tail outputs, perpendicular support and entry identities remain; no global bound is assumed.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(cnt)
