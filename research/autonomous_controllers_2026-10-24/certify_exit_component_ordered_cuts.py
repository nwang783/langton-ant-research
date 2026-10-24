#!/usr/bin/env python3
from pathlib import Path
import json,hashlib
from certify_exit_component_turn_flux import analyze
R=Path(__file__).resolve().parent

def check(a):
 d=a['drift'];cs=a['components'];P=a['period'];ranges=[]
 for c in cs:
  vals=[d[0]*p[1]-d[1]*p[0]for p in c['last_spine']['cells']];ranges.append({'component_id':c['component_id'],'minimum':min(vals),'maximum':max(vals),'outputs':c['O']})
 # The supplied standard controls have separated normal ranges; no general
 # theorem that all embedded spines have separated normal ranges is asserted.
 order=sorted(ranges,key=lambda r:r['minimum']);assert all(a['maximum']<b['minimum']for a,b in zip(order,order[1:]))
 ix={r['component_id']:i for i,r in enumerate(order)};J=[[0]*4 for _ in range(len(cs)-1)];cnt=[[0,0]for _ in J]
 for e in a['all_actual_cross_component_steps']:
  i=ix[e['source_component']];j=ix[e['target_component']];assert abs(i-j)==1;k=min(i,j);sgn=1 if i<j else-1
  J[k][e['direction']]+=sgn;cnt[k][0 if sgn==1 else 1]+=1
 assert all(o==i and o>0 for o,i in cnt)
 rows=[];prev=[0]*4;sumq=0;sumg=0
 for i,r in enumerate(order):
  c=cs[r['component_id']];after=J[i]if i<len(J)else[0]*4;b=[u-v for u,v in zip(after,prev)];assert b==c['out_minus_in_direction_counts']
  phi=sum(h*v for h,v in enumerate(after));before=sum(h*v for h,v in enumerate(prev));assert c['color_charge']==4*c['branch_cut_wrap_count']+phi-before
  sumq+=c['branch_cut_wrap_count'];sumg+=c['color_charge'];assert sumg==4*sumq+phi
  rows.append({'component_id':c['component_id'],'outputs':c['O'],'inputs':c['I'],'Q':c['branch_cut_wrap_count'],'lower_cut_flux':before,'upper_cut_flux':phi,'prefix_charge':sumg,'prefix_Q':sumq});prev=after
 return {'transverse_spine_ranges_in_order':order,'adjacent_cut_direction_vectors':J,'each_cut_out_in_counts':cnt,'component_and_prefix_identities':rows}

def main():
 z=json.loads((R/'exit_component_turn_flux_certificate.json').read_text());base={n:check(a)for n,a in z['base_controls'].items()};S=z['base_controls']['S104'];assert base['S104']['adjacent_cut_direction_vectors']==[[0,-4,4,0]]
 assert[(x['minimum'],x['maximum'],x['outputs'])for x in base['S104']['transverse_spine_ranges_in_order']]==[(-4,-2,4),(0,2,8)]
 controls=[]
 for h in range(4):
  for q in[1,2,3,5]:controls.append({'heading':h,'power':q,'result':check(analyze(S['word']*q,h))})
 out={'status':'AUTHOR checked, independent audit pending','scope':'General path adjacency follows from the stated embedded-spine cylinder-separation proof. These concrete controls do not assume a universal separated-normal-range property or establish any flux sign/output bound.',
  'base_controls':base,'all16_standard_representation_controls':controls,
  'dependencies':{f:hashlib.sha256((R/f).read_bytes()).hexdigest()for f in['PHYSICAL_EXIT_COMPONENT_COLOR_TURN_AND_BOUNDARY_FLUX.md','exit_component_turn_flux_certificate.json']}}
 p=R/'exit_component_ordered_cuts_certificate.json';p.write_text(json.dumps(out,indent=2)+'\n');print('PASS ordered-cut identities,16 standard representations',hashlib.sha256(p.read_bytes()).hexdigest())
if __name__=='__main__':main()
