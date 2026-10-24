from pathlib import Path
import json,hashlib
SELF=Path(__file__).resolve();R=SELF.parents[1];ns={'__file__':str(SELF.parent/'check_returned_C_source_reduction_independent.py')};exec(Path(ns['__file__']).read_text().split('# Independently reconstruct')[0],ns);W,M,walk,orders=[ns[k]for k in('W','M','walk','orders')]
D=R/'seven_word_spatial_return_2026-10-23';allcases=[]
for f,(X,Y)in {'F':(2,-5),'Q':(4,-5),'B':(5,-4)}.items():
 tuples=[];words=[]
 for e in range(-Y+1):
  for v in range((-Y-e)//3+1):
   for u in range((-Y-e-3*v)//4+1):
    if not e+v+u:continue
    rem=-Y-e-3*v-4*u
    for k in range(rem+1):
     l=rem-k;r=X+1+e+v-k-3*l
     if r<0 or r%4:continue
     m=r//4;tuples.append((e,v,u,k,l,m))
     for sw in orders(e,v,u):
      for ew in orders(k,l,m):
       if not ew or ew[-1]not in('VU'if f!='B'else'U'):continue
       for source in('VCC','UCC'):
        word=''.join(W[b]for b in source+sw+'C'+ew+f+'C')+M;z=walk(word);assert not z['feasible'];words.append({'source':source,'S':sw,'E':ew,'failure':z['i'],'cell':[int(z['q'].real),int(z['q'].imag)],'prior':z['first']})
 assert len(tuples)=={'F':10,'Q':10,'B':6}[f]and len(words)=={'F':24,'Q':40,'B':16}[f]
 allcases.append({'foreign':f,'counts':tuples,'words':words})
man=D/'returned_C_double_tail_source_manifest.json';sha=hashlib.sha256(man.read_bytes()).hexdigest();assert sha=='5ca7b68cac3ff890706c6c500287478020e178ce5213f0e74d805e08538e6f03';a=json.loads(man.read_text())
for f,h in a['files'].items():assert hashlib.sha256((D/f).read_bytes()).hexdigest()==h
out={'status':'PASS C1 of actual VCC/UCC cannot supply the three returned raw-C residues','manifest_sha256':sha,'families':allcases,'analytic':['Mandatory second C in the same VCC/UCC fullpacket leaves pose(-1,1,S); the absent W stage is a literal parser fact ONLY for those two source roles. Exactly one further C must be attached to a real S base, and the E suffix must end in the signed allowed plain V/U predecessor.','The exact y budget e+3v+4u+k+l=-Y bounds every variable except E U count m, then x fixes m uniquely. All26 count tuples and80 whole literal words are reconstructed independently and fail immutable repeated-cell alternation. No spatial/path/horizon cutoff is used.','The actual full creating packet is included, the last old C is its genuine S-base tail, the returned C is its own raw15 word, and only the observed terminal M11 is appended.'],'scope':'Two of seven containing old-C roles only. C1 of DC/VC/UC and C2 of VCC/UCC with genuine W excursions are not excluded; no U-entry returned-C closure or capture.'}
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status'])
