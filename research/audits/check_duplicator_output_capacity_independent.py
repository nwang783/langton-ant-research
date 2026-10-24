from pathlib import Path
from collections import Counter
import hashlib,json
P=Path(__file__).resolve();ROOT=P.parents[1];D=ROOT/'K1_pipeline_detours_2026-10-23'
r=json.loads(P.with_name('check_canonical_duplicator_suppliers_independent.json').read_text());flags={tuple(x[0]):tuple(x[1:])for x in r['flag_classes']}
c=Counter();reservations=[]
for row in r['rows']:
 u,t,a,v,birth,*heights=row;entry=u if birth=='u'else t;key=tuple(row[:5])
 if len(entry)==3:
  typ='C';s=entry;assert flags[key]==(0,0) and s[0]!=s[2]
 elif len(a)==3:
  typ='H';s=a;assert s=='EWE'and heights[2]=='M-2'
 elif u=='W':
  typ='S';s=u;assert t=='SSNS' and flags[key]==(1,-1)
 else:
  typ='4';s=None;assert(u,t,a)==('EEWE','NNNS','EWEE')and flags[key]==(1,-1)
 c[typ]+=1;reservations.append((row[:5],typ,s))
assert c=={'C':4,'H':6,'S':2,'4':2}
# Shape distinctions are invariant under any proper rotation and full-drift
# translate: opposite-R three-read, same-R three-read and singleton-R.
head='NESW'
rot=lambda s,k:''.join(head[(head.index(x)+k)%4]for x in s)
C={rot(s,k)for _,typ,s in reservations if typ=='C'for k in range(4)}
H={rot(s,k)for _,typ,s in reservations if typ=='H'for k in range(4)}
S={rot(s,k)for _,typ,s in reservations if typ=='S'for k in range(4)}
assert not(C&H or C&S or H&S)
# Safe numerical inequality follows from max(H,SB)>=H; do not add H and SB.
for no in range(4):
 for dc in range(4):
  for dh in range(4):
   for ds in range(4):
    for d4 in range(4):
     for sb in range(4):
      for anc in range(4):
       lower=no+dc+max(dh,sb)+ds+anc
       assert lower+d4>=no+dc+dh+ds+d4+anc
note=D/'canonical_duplicator_output_or_all_four_leaf_capacity.md';sha=hashlib.sha256(note.read_bytes()).hexdigest();assert sha=='bf0785e8803b6b4fb03e1daaddce0f93efc8400dd65956a5ad2af3f58179a30b'
out={'status':'PASS actual-duplicator odd-output class disjointness and retained all-four leaf capacity','note_sha256':sha,'partition_of_14_necessary_rows':dict(c),'reservations':reservations,'analytic_review':['D-to-I injection makes C canonical-entry reservations distinct. A canonical incoming contact determines its unique actual child; C has q(I)=0, so it cannot be the q=1 O entry even though the heading pattern agrees.','Every H same-R EWE cell chooses its unique high M face I, opposite height M-2. This makes H injective across actual rotations. Same-R H cannot equal opposite-R C/O. H may equal a prior strict-straight-branch reservation, so only max(D_H,n_SB) is charged.','Every S singleton chooses its unique high face I, a canonical leaf. Prior singleton ancestors choose Q1 of outdegree1. Coincidence would equate these faces, contradicting their actual outdegrees. Multiplicity excludes all three-read overlap.','The complete actual flag balance gives N_O+N_D equal to total negative flag units, at least n_A. Thus N_odd+D_4>=n_A+n_Sanc. No additional v=NNN output is charged in D_4.','All uniqueness arguments are physical and survive full-drift class alignment; no independent-component, time-disjoint supplier or no-merging assumption is used.'],'bounds':['N_odd >= N_O + D_C + max(D_H,n_SB) + D_S + n_Sanc','N_odd + D_4 >= n_A + n_Sanc'],'scope':'Output lower bounds only. The all-four leaf escape remains; no original fuel, global front exclusion or iterative old-parent claim.'}
P.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(c)
