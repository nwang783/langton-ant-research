#!/usr/bin/env python3
"""Exact cross-cycle excursion interleavings and their imported actual roots."""
from pathlib import Path
import json,hashlib
from certify_active_C_entry_exit_forests import analyze,active_C
from check_extremal_read_coupling import event_word
from certify_C_excursion_triangular_winding import control,occ,winding
R=Path(__file__).resolve().parent

def interleavings(z,detail=False):
 cs=control(z,True);w=z['word'];E,d,h=event_word(w,h=z['initial_heading']);P=len(E);roots=[]
 for c,cy in enumerate(cs):
  for ex in cy['excursions']:
   r=ex['R_time']%P;a=ex['length'];roots.append((c,r,a))
 ans=[]
 for ci,r,a in roots:
  li=r+a;ei=[occ(E,d,t) for t in range(r,li)];poly=[e['p'] for e in ei]+[ei[0]['p']]
  for cj,s0,b in roots:
   for k in [0,1]:
    s=s0+k*P;lj=s+b
    if not r<s<li<lj:continue
    assert ci!=cj
    ri=occ(E,d,r);lli=occ(E,d,li);rj=occ(E,d,s);llj=occ(E,d,lj)
    assert ri['p']==lli['p'] and ri['hi']==lli['hi'] and ri['c']=='R' and lli['c']=='L'
    assert [e['t'] for e in ei if e['p']==rj['p']]==[s]
    uj=active_C(rj['p'],rj['hi']);vj=active_C(rj['p'],(rj['hi']+2)%4)
    assert winding(poly,uj)==1 and winding(poly,vj)==0
    ej=[occ(E,d,t) for t in range(s,lj)]
    assert [e['t'] for e in ej if e['p']==ri['p']][0]==li
    row={'older_cycle':ci,'younger_cycle':cj,'R_older':r,'R_younger':s,'L_older':li,'L_younger':lj,
     'older_length':a,'younger_length':b,'younger_root_period':k,'imported_root_cell':ri['p'],
     'actual_import_owner':r,'actual_import_consumption':li,'import_age':a,'younger_parent':uj,'younger_child':vj,
     'older_winding_at_younger_parent':1,'older_winding_at_younger_child':0}
    if detail:row.update({'older_polygon':poly,'younger_events':ej,'older_root_event':ri,'consumed_older_root_event':lli,'younger_root_event':rj})
    ans.append(row)
 return ans

def main():
 base=json.loads((R/'active_C_entry_exit_forests_certificate.json').read_text())['base_controls']
 bs={n:interleavings(z,True) for n,z in base.items()}
 assert [(a['R_older'],a['R_younger'],a['L_older'],a['L_younger']) for a in bs['S104']]==[(28,56,116,148),(56,132,148,220)]
 assert all(not bs[n] for n in ['P1564','Q4352','M10','F80'])
 controls=[]
 for h in range(4):
  for q in [1,2,3,5]:
   z=analyze(base['S104']['word']*q,h);v=interleavings(z);assert len(v)==2*q
   controls.append({'heading':h,'power':q,'interleavings':v})
 for cut in [1,13,28,45,56,103]:
  w=base['S104']['word'];v=interleavings(analyze(w[cut:]+w[:cut]));assert len(v)==2
  controls.append({'phase':cut,'interleavings':v})
 deps=['C_DISCOVERY_EXCURSION_TRIANGULAR_WINDING.md','C_CYCLE_EXCURSIONS_AND_STANDARD_SELF_FEEDING.md','active_C_entry_exit_forests_certificate.json']
 out={'status':'AUTHOR checked, independent audit pending','scope':'If strict interleaving exists, exact winding/owner consequences follow. No necessity of interleaving or two cycles is proved.',
 'base_controls':bs,'representation_controls':controls,'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest() for f in deps}}
 p=R/'C_excursion_interleaving_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS',len(controls),'representations',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
