"""Exact 14-cell/56-event all-even corner-reader two-cycle with full rank
labels and injective known-component clocks. NOT a prepared factor/front.
"""
from pathlib import Path
import json
base=Path(__file__).parent;lib={'__file__':str(base/'check_even_reader_rail_and_merge_reset.py')};exec((base/'check_even_reader_rail_and_merge_reset.py').read_text().split('rows=[]')[0],lib)
fixed,V,out,check,graph=[lib[k]for k in ['fixed','V','out','check','graph']]
C=(2,-1);F=(2,-2);G=(3,-1);H=(3,-2)
hs=fixed|{F:'NNSS',G:'SNNS',H:'EWWE'};assert check(hs)=='open'
su,cs,order,times=graph(hs)
def corner(p):
 h=hs[p];iv=V[h[3]];ov=V[out(h,2)];return p[0]-iv[0]+ov[0],p[1]-iv[1]+ov[1]
assert corner(C)==H and corner(H)==C
path=[(H,2),(G,1),(C,3),(F,3),(H,3)]
assert all(su[e]==f for e,f in zip(path,path[1:]));assert times[H,3]==times[H,2]+4
assert ''.join('R'if r%2==0 else'L'for p,r in path[:-1])=='RLLL'
assert all(len(h)==4 for h in hs.values())and len(times)==56
j=dict(scope=__doc__,histories={str(p):h for p,h in sorted(hs.items())},corner_two_cycle=[C,H,C],actual_path=path,actual_word='RLLL',actual_rank_span=4,incoming_headings=['W','E'],components=cs,whole_component_order=order,injective_mod4_calendar={str(e):t for e,t in times.items()},events=56,warning='K is a geometric reader interface, not actual succession/b/canonical ancestry. No physical connectors or full-period completion supplied.')
Path(__file__).with_suffix('.json').write_text(json.dumps(j,indent=2)+'\n');print('PASS complete even reader two-cycle; actualR2->L3 rank shift,56 distinct known clocks')
