from pathlib import Path
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'autonomous_controllers_2026-10-24'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
files={'C_EXCURSION_INTERLEAVING_ROOT_OWNERSHIP.md':'caa0fc77237c06599948665fe49a09528106abc11ebd748f8bffbf7194586540','certify_C_excursion_interleaving.py':'1bc5e02944da602085f28399d2a7dbd9a9b431fb369640c999a8beb6ffef16c2','C_excursion_interleaving_certificate.json':'83b316c25c6f52c9b053873bbdccc31032a45900a793a16d12b185c9a2e7a9b6'}
for f,h in files.items():assert sha(D/f)==h
J=json.loads((D/'C_excursion_interleaving_certificate.json').read_text())
for f,h in J['dependencies'].items():assert sha(D/f)==h
q=R/'audits/check_C_excursion_triangular_independent.py';ns={'__file__':str(q)};exec(q.read_text().split('def reconstruct')[0],ns);analyze,winding,xy,off,base=[ns[k]for k in('analyze','winding','xy','off','base')]
def verify(word,h0,author):
 a=analyze(word,h0);P=a['n'];d=a['d'];rep=a['rep'];ev=a['ev'];starts=a['starts'];fw=a['fw'];roots=[]
 for ci,(classes,vol,gap)in enumerate(a['cycles']):
  inv={complex(*fw[c]['target']):c for c in classes};u=min(classes,key=lambda q:(q.real,q.imag));initial=u
  for _ in classes:
   q,k=rep(u);v=inv[q];edge=fw[v];child=v+(k-edge['voltage'])*d;lt=starts[v]+(k-edge['voltage'])*P-1;root,hh,turn,ph=ev(lt);rc,rk=rep(root);hist=a['H'][rc];rt=hist[0][0]+rk*P
   assert hist[0][1]['c']=='R'and hist[1][0]+rk*P==lt and ev(rt)[:2]==(root,hh)and turn=='L';assert 0<lt-rt<P
   roots.append((ci,rt%P,lt-rt));u=child
  assert u==initial+d
 found=[]
 for ci,r,age in roots:
  li=r+age;ei=[ev(t)for t in range(r,li)];poly=[z[0]for z in ei]+[ei[0][0]]
  for cj,s0,agej in roots:
   # age<P makes these the complete possible physical lifts after r in[0,P).
   for k in(0,1):
    s=s0+k*P;lj=s+agej
    if not r<s<li<lj:continue
    assert ci!=cj
    qi,hi,ti,_=ev(r);qj,hj,tj,_=ev(s);assert ti==tj=='R'and ev(li)[:3]==(qi,hi,'L')and ev(lj)[:3]==(qj,hj,'L')
    assert[t for t in range(r,li)if ev(t)[0]==qj]==[s]
    assert[t for t in range(s,lj)if ev(t)[0]==qi][0]==li
    par=qj+off[hj];child=qj+off[(hj+2)%4];assert winding(poly,par)==1 and winding(poly,child)==0
    row=dict(R_older=r,R_younger=s,L_older=li,L_younger=lj,older_length=age,younger_length=agej,younger_root_period=k,imported_root_cell=xy(qi),actual_import_owner=r,actual_import_consumption=li,import_age=age,younger_parent=xy(par),younger_child=xy(child),older_winding_at_younger_parent=1,older_winding_at_younger_child=0)
    aa=next(z for z in author if(z['R_older'],z['R_younger'],z['L_older'],z['L_younger'])==(r,s,li,lj));assert all(aa[key]==v for key,v in row.items())
    if'older_polygon'in aa:
     assert aa['older_polygon']==[xy(q)for q in poly]
     assert len(aa['younger_events'])==agej
     for t,z in zip(range(s,lj),aa['younger_events']):
      qp,hp,cp,phase=ev(t);assert z['t']==t and z['p']==xy(qp)and z['hi']==hp and z['c']==cp
    found.append(row)
 assert len(found)==len(author)
 return found
controls={n:verify(z['word'],z['initial_heading'],J['base_controls'][n])for n,z in base.items()}
for row in J['representation_controls']:
 w=base['S104']['word'];h=0
 if'phase'in row:cut=row['phase'];w=w[cut:]+w[:cut]
 else:w*=row['power'];h=row['heading']
 verify(w,h,row['interleavings'])
assert len(J['representation_controls'])==22
assert [(r['R_older'],r['R_younger'],r['L_older'],r['L_younger'])for r in controls['S104']]==[(28,56,116,148),(56,132,148,220)]
review=[
'Strict lifted interleaving r_i<r_j<l_i<l_j imports the actual SAME R_i lifetime into E_j. R_i/L_i are the first two physical reads, so its consumption at l_i is the first read of that cell inside E_j and its birth lies before E_j. No cropped field or hypothetical replacement is used.',
'The root of E_j is read exactly once during E_i, at r_j:R. Thus the local clockwise-current identity gives f_i(parent_j)-f_i(child_j)=1. Child_j and every face on its proper forward discovery ray have not yet been activated by time l_i<l_j. The unread future-ray escape argument therefore applies to E_i as well and makes child_j winding0, hence parent_j1.',
'Excursions on one selected discovery cycle are event-disjoint, so strictly interleaving ones necessarily belong to different cycles. They are not disjoint actual channels and cannot enter a component-packing or period-length sum. Standard88+92 exceeds104 precisely because they overlap.',
'Each selected age<P follows from the signed excursion-plus-nonempty-connector period partition. Therefore older r normalized to[0,P) and younger lifts0/1 exhaust all interleavings, including all q-fold full-drift classes. Fresh own active-C graph, lifetime lifts and independent left-ray winding validate all five controls and22 rotations/powers/phases.',
'The two standard root links have exact voltages0 and+1, hence total temporal winding1. This conditional feedback does not account for all imported cells, prove interleaving/two-cycle necessity, detect hidden prepared inputs, or classify WHITE fronts.'
]
out=dict(status='PASS conditional strict C-excursion interleaving ownership and winding',files=files,script=sha(S),controls=controls,representation_controls=22,analytic_review=review,scope='Actual WHITE-owned discovery excursions; no necessity of interleaving, no disjoint-channel packing, no two-cycle or global attraction theorem.')
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(sha(S.with_suffix('.json')))
