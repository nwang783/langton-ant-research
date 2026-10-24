from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'global_attraction_bridge_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'MIRROR_PRISTINE_RECORD_MANIFEST.json';assert sha(MF)=='4463ffef766240fd0a2cfb42605018e2756c9b57f77e21974c2b72d44579b7e7';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
assert sha(D/mf['requires'])==mf['requires_sha256'];ref=json.loads((D/'MIRROR_PRISTINE_RECORD_CHECKED.json').read_text())
for f,h in ref['dependencies'].items():assert sha(D/f)==h
lib=S.with_name('check_mirror_winding_independent.py');ns={'__file__':str(lib)};exec(lib.read_text().split('small=Counter()')[0],ns);cycle,wind,surgery,step,V,xy=[ns[k]for k in['cycle','wind','surgery','step','V','xy']];parent=json.loads((D/'MIRROR_WINDING_RENEWAL_CHECKED.json').read_text());tot=0;results=[]
for c in parent['controls']:
 seed={complex(*q)for q in c['initial_black']};B={q:-i-1 for i,q in enumerate(sorted(seed,key=lambda p:(p.real,p.imag)))};p=0j;h=1;dot=lambda a,q:int(q.imag)if a==0 else int(q.real)if a==1 else-int(q.imag)if a==2 else-int(q.real);hull=[max([0]+[dot(a,q)for q in seed])for a in range(4)];records=[]
 for t in range(len(c['whole_word'])+1):
  for axis in range(4):
   if dot(axis,p)<=hull[axis]:continue
   assert h==axis and p not in B and all(dot(axis,q)<dot(axis,p)for q in B)
   a=cycle((p,h),B);b=cycle((p,(h+2)%4),B);aw,aa=wind(a);bw,ba=wind(b)
   assert ba==-1 and len(b)==4 and all(dot(axis,q)>=dot(axis,p)for q,hh in b);assert aa<0 and all(dot(axis,q)<=dot(axis,p)for q,hh in a);assert set(a).isdisjoint(b)and set(aw).isdisjoint(bw)
   z=surgery(B,(p,h));assert z['kind']=='merge'and z['same_orientation']and z['positive_area_change']==0 and z['new_lengths']==[len(a)+4]and z['new_areas']==[aa-1]
   oldnext=step((p,h),B);bb=set(B)|{p};newloop=cycle((p,h),bb);assert oldnext in newloop
   field=sorted([(xy(q),i)for q,i in B.items()]);digest=hashlib.sha256(json.dumps(field,separators=(',',':')).encode()).hexdigest()
   records.append(dict(tick=t,axis=axis,pose=[xy(p),h],active_before_length=len(a),active_before_area=aa,active_after_length=len(a)+4,active_after_area=aa-1,other_loop=[[xy(q),hh]for q,hh in b],complete_field_sha256=digest));hull[axis]=dot(axis,p)
  if t==len(c['whole_word']):break
  turn='L'if p in B else'R';assert turn==c['whole_word'][t]
  if turn=='L':del B[p]
  else:B[p]=t
  h=(h+(1 if turn=='R'else-1))%4;p+=V[h]
 rr=next(z for z in ref['controls']if z['name']==c['name']);assert records==rr['records'];assert [[z['tick'],z['axis']]for z in records]==c['union_records'];tot+=len(records);results.append(dict(name=c['name'],reads=len(c['whole_word']),records=len(records),max_active_before=max(z['active_before_length']for z in records)))
assert tot==ref['records']==122
out=dict(status='PASS universal finite-board axial pristine-record fresh clockwise loop merger, no return budget',manifest=sha(MF),script=sha(S),records=tot,controls=results,analytic_review=[
'A strict coordinate record beyond the augmented original-support/head-history hull has incoming outward normal, current WHITE head and the entire current BLACK field strictly behind the record line. The opposite incoming state follows one untouched clockwise four-state square in the fresh closed half-plane.',
'Every modified empty-board circuit through a BLACK site strictly behind the line stays in the old closed half-plane, and their union is closed under the changed pairing. Hence the active frozen circuit at the record is also behind the line, whether altered or baseline. This uses the whole field, not a local crop or a current relevant hull.',
'The active and opposite-state circuits are distinct and their plaquette domains disjoint. Signed winding surgery then forces equal clockwise orientation. The R update merges them with length+4 and negative area minus1, while total positive winding P is unchanged. The actual old successor belongs to the new merged loop, so the static update is correctly tied to the real move.',
'Other normals and checkerboard sectors follow proper rotation/translation with the baseline carried along. No reflection, physical time reversal or invariant-sector substitution is required. All122 exact records independently reconstruct from the original two seeds, including complete current-field identity digests and terminal record supported by the signed full future.',
'This is a fresh-boundary interface only. It does not prevent later interior positive-area creation, detached-loop reuse, cancellation or remote reattachment, and gives no return-time, record-density, global budget or attraction conclusion.'
],dependencies=ref['dependencies']|{'independent_winding_report':sha(S.with_name('check_mirror_winding_independent.json'))})
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(sha(S.with_suffix('.json')));print(results)
