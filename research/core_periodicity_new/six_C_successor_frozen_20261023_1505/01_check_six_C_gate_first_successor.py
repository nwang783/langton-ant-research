"""Earlier-vertex repetition removes source UC/UCC and a first D successor.
Pure actual atomic center geometry, no path search or age kernel.
"""
from pathlib import Path
from fractions import Fraction as F
import json,hashlib
W=Path(__file__).resolve().parent;GP=W/'chronology_dcuv/literal_residual_geometry.json';NP=W/'six_C_contact_frozen_20261023_1454/manifest.json';AP=W/'atomic_exit_bud_frozen_20261023_1325/02_atomic_exit_bud_maturation.json';G=json.loads(GP.read_text())['geometry'];C=json.loads(AP.read_text())['C_word'];IDS=[0,1,4,5,6,7,8,9]
def rot(z,h):x,y=z;return((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def center(p,h):u,v=rot((F(-1,2),F(-1,2)),h);return p[0]+u,p[1]+v
Uend=tuple(G[7]['endpoint'][:2]);assert Uend==(0,4)and G[7]['endpoint'][2]==0
later_entry=center((0,4),2);later_contact=(F(-1,2),F(3,2));assert later_entry==(F(1,2),F(9,2))and later_contact!=later_entry
ce=tuple(json.loads(AP.read_text())['C_endpoint']);assert ce==(0,1,3)
checks=[]
for first in ['D','C']:
 e=G[0]['endpoint']if first=='D'else ce;p=(Uend[0]+e[0],Uend[1]+e[1]);h=e[2];z=center(p,h);assert z==later_entry
 checks.append(dict(next_atom=first,next_exit=[*p,h],next_exit_center=[str(q)for q in z],next_exit_C_clock=0 if first=='D'else 1,final_V_entry_C_clock=6,reason='REVISITS_EARLIER_NEXT_ATOM_EXIT_BEFORE_FINAL_V_ENDPOINT_CONTACT'))
source_cases=[]
for a in[7,8,9]:
 tail=G[a]['word'][len(G[7]['word']):];assert tail==C*G[a]['name'].count('C')
 source_cases.append(dict(full_source=a,has_immediate_C=bool(tail),excluded_as_six_C_FIRST_contact=bool(tail)))
successors=[]
for a in IDS:
 first='D'if a in[0,1]else'V'if a in[4,5,6]else'U';successors.append(dict(next_full_packet=a,next_base=first,excluded_after_plain_U=first=='D'))
O=dict(status='AUTHOR_SIX_C_GATE_PLAIN_U_AND_NON_D_SUCCESSOR_NECESSITY_PASS',scope='In the signed remaining canonical six-C FIRST contact U0,N→V(0,4,S), source full packet must be plainU, and its immediately following packet has V/U base. UC/UCC source or D/DC successor causes an earlier repeated center at finalVentry. No exclusion/attainment of remaining gate or fuel.',source_U_base_exit=[0,4,0],later_V_entry=[0,4,2],later_V_entry_center=[str(q)for q in later_entry],actual_next_atom_exit_checks=checks,full_source_cases=source_cases,next_full_packet_cases=successors,dependencies={str(p.relative_to(W)):hashlib.sha256(p.read_bytes()).hexdigest()for p in[GP,NP,AP,Path(__file__).resolve()]})
OUT=W/'chronology_dcuv/six_C_gate_first_successor.json';OUT.write_text(json.dumps(O,indent=2)+'\n');print(dict(source='U only',next_base='V or U',two_exact_vertex_equalities=len(checks)))
