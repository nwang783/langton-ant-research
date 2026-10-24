from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();ROOT=SELF.parents[1]
p=SELF.parent/'check_returned_V_source_reduction_independent.py';ns={'__file__':str(p)};exec(p.read_text().split('mins=')[0],ns)
walk,W,M,xy,raw,ctx,outputs,K=[ns[x]for x in('walk','W','M','xy','raw','ctx','outputs','K')]
AR={n:walk(W[n])for n in'DCVU'};AC={n:walk(W[n]+M)for n in'DCVU'}
AO={n:({q for q,b in AC[n]['req'].items()if b}^AR[n]['odd'])-{AR[n]['p']+q*(-1j)**AR[n]['h']for q in K}for n in'DCVU'}
assert all(q.imag>=0 and q.real+q.imag>=0 for a in AO.values()for q in a)
L={0,1j,1,1+1j};rows=[];roles={}
for base,source,g,held,originwant,fs in [('V','VC',1+1j,{0,1},{('V',3+2j),('U',4+3j)},'FQB'),('U','UC',2j,L,{('V',2+3j),('U',2+3j),('U',3+4j)},'QB')]:
 Cstart=raw[base]['p'];assert raw[base]['h']==0
 rr=[(i,c)for i,(q,h,c)in enumerate(raw[source]['reads'])if q==g]
 assert rr==[(i,c)for i,(q,h,c)in enumerate(raw[base]['reads'])if q==g]and rr[-1][1]=='L'
 assert g not in outputs[source]and g not in{raw[source]['p']+q*(-1j)**raw[source]['h']for q in K}
 origins=[];ro=[]
 for h in(2,1):
  for a in'DCVU':
   for o in sorted(AO[a],key=xy):
    e=g-o*(-1j)**h;end=e+AR[a]['p']*(-1j)**h
    why='sector'if(int(e.real+e.imag)+h)%2 else'held_preforeign_context'if held&{e+q*(-1j)**h for q in AC[a]['req']}else'late_C4'if h==1 and a=='C'else'E3_origin'
    ro.append([h,a,xy(o),xy(e),xy(end),why])
    if why=='E3_origin':assert h==1;origins.append((a,e,end))
 assert len(ro)==38 and {(a,end)for a,e,end in origins}==originwant
 roles[base]=ro
 for f,oldp in [('F',2-5j),('Q',4-5j),('B',5-4j)]:
  if f not in fs:continue
  fp=Cstart+oldp;fr=walk(W[f]);comb=walk(W[f]+W['C']+M);assert comb['feasible']
  ep=fp+fr['p']*(-1j);assert ep==Cstart-1j and(fr['h']+1)%4==3
  loc=(g-fp)*1j
  assert loc not in fr['req']and loc not in K and comb['req'][loc]is True
  first=next((i,c)for i,(q,h,c)in enumerate(comb['reads'])if q==loc)
  assert first==(len(W[f])+1,'L')
  eq=[]
  for a,e,end in origins:
   dx,down=int(fp.real-end.real),int(end.imag-fp.imag);solutions=[]
   assert end!=fp
   for v in range(max(0,down+1)):
    d=down-v;rem=dx-d-3*v
    if rem>=0 and rem%4==0:
     u=rem//4;assert u==0 and(v==0 or f=='B');solutions.append((d,v,u))
   eq.append([a,xy(e),xy(end),solutions])
  rows.append(dict(source=source,old_C_entry=xy(Cstart),foreign=f,foreign_entry=xy(fp),foreign_heading='E',returned_C_entry=xy(ep),returned_heading='W',deleted_guard=xy(g),source_reads=rr,foreign_RAW_misses=True,foreign_core_misses=True,combined_first_read_tick0=first[0],physical_owner='returned C tick1/read2',all_origin_endpoint_counts=eq))
assert len(rows)==5
D=ROOT/'seven_word_spatial_return_2026-10-23';mp=D/'returned_C_VC_UC_deleted_guard_lift_manifest.json';mh=hashlib.sha256(mp.read_bytes()).hexdigest();assert mh=='c5d21196c5050fdcbc22349968807e4100aab59ed0e08ae333f3ed8f11039350'
manifest=json.loads(mp.read_text())
for f,h in manifest['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
for f,h in manifest['dependencies'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
out={'status':'PASS five VC/UC containing-role source-deletion lifts; only old C1 of DC remains in the three old-C residues','author_manifest_sha256':mh,'five_actual_role_transforms':rows,'all76_atomic_rebirth_roles':roles,'analytic':['Actual old C1 starts at source-base exit, at the same full-source ENTRY C clock zero. Consequently foreign old-C age3 is also age3 from the genuine V/U full-source entry. Source own C tail preserves the actual deletion, and the deleted cell is absent from residual outputs and full exit core.','The needed black cell is outside foreign entry core and never RAW-read by the foreign. The actual returned C tick1/read2 therefore imposes a BLACK condition already at foreign entry. This is a preforeign residual-rebirth obligation, not a physical-white permanence assertion or a fabricated foreign read.','For genuine V-family ancestry, original r and B are held before clock3 by independently signed first-retirement5/4. For genuine U-family ancestry, original L-star remains held throughout the old-eight prefix. These facts require simple old-eight U-entry history but not contact with the creating base.','Source-exit N0 and W1 output cones rule out early production; all38 S/E roles per base rule out S2 and retain only the listed E3 plain origins. C4 and positive-C full tails cannot complete by foreign3. Thus all remaining continuation is zero-C E, with no omitted S run. Exact d+3v+4u and d+v equations, including empty-continuation rejection, exclude every target with the actual required last V/U or U.','The dependency lifted is precisely the target-specific rebirth argument, not the previous first-contact classification. Returned atom type never enters the rebirth proof after the BLACK-at-foreign-entry premise is verified.'],'scope':'Only these five old-C containing fullproducer roles in the three signed residues. With separate UC/F core and both double-tail exclusions only old C1 DC remains. No complete returned simplicity, second foreign or universal capture conclusion.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
