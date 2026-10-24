from pathlib import Path
import json,hashlib
P=Path(__file__).resolve();prefix=P.with_name('check_U1_young3_shadow_independent.py').read_text().split('rows=[];cases=[]')[0];exec(compile(prefix,str(P.with_name('check_U1_young3_shadow_independent.py')),'exec'))
B=ROOT/'core_periodicity_new/U_young3_boundary_frozen_20261023_1230';M=json.loads((B/'manifest.json').read_text())
for f in M['files']:assert hashlib.sha256((B/f['file']).read_bytes()).hexdigest()==f['sha256']
J=json.loads((B/'02_U_young3_boundary_shadow.json').read_text());cases=[];rows=[]
for p in ids:
 c=counts[p];h=(-G[p][1])%4;start=-rotation(G[p][0],h);assert h==c
 outs={start+rotation(o,h):o for o in G[p][4]};q=(-3j if p in(4,7) else 1-1j);assert q in outs and q not in K
 for target in(7,8,9):assert G[target][2][rotation(q-gp,-gh)] is False
 for s in(4,5):
  assert q not in G[s][3]|G[s][4] and G[s][2].get(q,True) is True
  for a in ids:
   for z in G[a][3]:
    for n in range(c+counts[s],c+4):
     if n<oldages[a,z] or counts[a]>c+3-n:continue
     ch=(h-n)%4;pos=q-rotation(z,ch);end=pos+rotation(G[base[a]][0],ch);remain=c+3-n
     if ch==1:
      assert remain==0 and counts[a]==0 and(end.real>0 or end.imag<-1)
      why='final east zero-C cone'
     elif ch==2:
      assert remain==1 and end.imag-1<-1;why='final south-to-east one-C cone'
     elif ch==3:
      se,sh=G[s][:2]
      if s==4:assert sh==0 and n-c-counts[s]==1 and pos.imag<se.imag+1;why='initial north-to-west one-C cone'
      else:assert sh==3 and n-c-counts[s]==0 and pos.real>se.real;why='initial west zero-C cone'
     else:
      assert ch==0 and c==2 and n==2 and s==4 and base[a]==4 and z==3j and pos==1-4j
      assert n-c-counts[s]==0 and pos.imag<G[s][0].imag;why='initial north zero-C cone'
     cases.append({'predecessor':p,'source':s,'consumer':a,'input':list(xy(z)),'age':n,'consumer_pose':[*xy(pos),ch],'remaining_C':remain,'base_endpoint':list(xy(end)),'shadow':list(xy(q)),'reason':why})
 rows.append({'predecessor':p,'pose':[*xy(start),h],'shadow':list(xy(q)),'slot':list(xy(outs[q]))})
key=lambda r:(r['predecessor'],r['source'],r['consumer'],tuple(r['input']),r['age'])
author={key(r):r for r in J['all_retirement_cases']};own={key(r):r for r in cases};assert author.keys()==own.keys() and len(own)==310
for k,r in own.items():
 for field in('consumer_pose','remaining_C','base_endpoint','shadow'):assert r[field]==author[k][field]
# Independently flatten all endpoint-compatible VCC forced-continuation cuts.
cuts=[]
for p in ids:
 h=(-G[p][1])%4;start=-rotation(G[p][0],h)
 for tail in(7,8,9):
  word=raws[p]+raws[6]+raws[5]+raws[0]+raws[tail]+mark;point=start;heading=h;last={};bad=None
  for t,turn in enumerate(word):
   if point in last and last[point][1]==turn:
    bad={'cell':list(xy(point)),'previous_read':last[point][0],'conflicting_read':t,'turn':turn};break
   last[point]=(t,turn);heading=(heading+(1 if turn=='R'else-1))%4;point+=(1j,1,-1j,-1)[heading]
  assert bad
  record={'predecessor':p,'tail':tail,'start_pose':[*xy(start),h],'conflict':bad,'suffix_conflict_phase':bad['conflicting_read']-len(raws[p])};cuts.append(record)
assert cuts==J['VCC_predecessor_literal_cuts'] and len(cuts)==24
# The universal age3 source classification fixes the same physical pair/target
# for all three V-family sources; one initial packet cannot supply it twice.
for source in(4,5,6):
 assert {1+0j,2+0j}<=G[source][4]
 assert {gp+rotation(z,gh)for z in(-1+1j,-1+2j)}=={1+0j,2+0j}
out={'status':'PASS independent all-eight predecessor/retirement and forced-VCC literal-cut reconstruction','manifest_sha256':hashlib.sha256((B/'manifest.json').read_bytes()).hexdigest(),'predecessors':rows,'retirement_count':len(cases),'new_c2_retirements':sum(r['predecessor']in(6,9)for r in cases),'retirement_cases':cases,'literal_VCC_cuts':cuts,'scope':'A produced q-age3 U/UC/UCC input in an actual complete recurrent-eight factor must be supplied by its FIRST packet. At most one such event per factor, with entry identities exempt. No record premise for this boundary law, no later age minimum without the exception, no funding closure or capture.'}
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print({k:v for k,v in out.items()if k not in('retirement_cases','literal_VCC_cuts')})
