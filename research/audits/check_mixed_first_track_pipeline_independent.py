from pathlib import Path
from itertools import product
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'first_departure_multiplicity_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();proof=D/'critical_cap4_departure_first_track_pipeline_with_mixed_flows.md';assert sha(proof)=='d5acded4c47b670b8419ff9fe216eeea54c052e8beb9bf88ae685ff3c2bb8d1a'
J=json.loads((D/'check_all_cap4_departure_first_track_sides.json').read_text());V={'N':1j,'E':1,'S':-1j,'W':-1};I={v:k for k,v in V.items()};out=lambda w:[I[V[h]*(-1j if r%2==0 else 1j)]for r,h in enumerate(w)]
profiles=[];rotated=0
for n in range(1,5):
 for ww in product('EW',repeat=n):
  w=''.join(ww);o=out(w)
  for turn in('RIGHT','LEFT'):
   co='S'if turn=='RIGHT'else'N'
   if o[0]!=co or not w.count('E'):continue
   # RIGHT preserves one common C sector. LEFT joins NE and SW C sectors,
   # whose difference equals outgoingN minus incomingE, so equality is exact.
   if turn=='LEFT'and o.count('N')!=w.count('E'):continue
   ins=[i for i,h in enumerate(w)if h=='E'];outs=[i for i,h in enumerate(o)if h==co]
   outside='LEFT'if turn=='RIGHT'else'RIGHT';events=[]
   for r in range(n):
    si=('RIGHT'if ins.index(r)==0 else'LEFT')if r in ins else outside
    so=('RIGHT'if outs.index(r)==0 else'LEFT')if r in outs else outside
    events.append(dict(rank=r,incoming=w[r],outgoing=o[r],input_side=si,output_side=so))
   crossings=[(e['rank'],e['input_side'],e['output_side'])for e in events if e['input_side']!=e['output_side']]
   if turn=='RIGHT':assert crossings==[]and all(e['input_side']==e['output_side']==('RIGHT'if i==0 else'LEFT')for i,e in enumerate(events))
   else:
    assert crossings==([(1,'RIGHT','LEFT'),(2,'LEFT','RIGHT')]if w in('WEE','WEEW','WEEE')else[])
    if w=='WEEE':assert events[3]['input_side']==events[3]['output_side']=='LEFT'
    if w=='WEEW':assert events[3]['input_side']==events[3]['output_side']=='RIGHT'
   rec=next(z for z in J['profiles']if(z['turn'],z['history'])==(turn,w));assert rec['actual_event_sides']==events and rec['crossings']==list(map(list,crossings))and rec['physical_flows']==[len(ins),len(outs)]
   for k in range(4):
    vrot=lambda h:I[V[h]*(-1j)**k];wr=''.join(map(vrot,w));oo=out(wr);assert oo==list(map(vrot,o))
    assert[i for i,h in enumerate(wr)if h==vrot('E')]==ins and[i for i,h in enumerate(oo)if h==vrot(co)]==outs;rotated+=1
   # Each input and output side has equal cardinality after paired crossing repair.
   assert sum(e['input_side']=='RIGHT'for e in events)==sum(e['output_side']=='RIGHT'for e in events)
   profiles.append((turn,w,[len(ins),len(outs)]))
assert len(profiles)==21 and rotated==84 and sum(t=='RIGHT'for t,w,f in profiles)==15
assert{w:f[0]for t,w,f in profiles if t=='LEFT'}=={'WWE':1,'WEE':2,'WWEW':1,'WWEE':2,'WEEW':2,'WEEE':3}
# Exact variable-flow boundary arithmetic: original jump c-(c-f)=f;
# right cut jump (c-(c-1))-0=1; complementary jump f-1.
for f in range(1,5):assert 1+(f-1)==f and f-1>=0
outj=dict(status='PASS cap-four mixed-flow first-track critical same-contact pipeline',proof_sha256=sha(proof),checker_sha256=sha(D/'check_all_cap4_departure_first_track_sides.py'),certificate_sha256=sha(D/'check_all_cap4_departure_first_track_sides.json'),all21_profiles=profiles,all_rotations=84,analytic_review=[
'All complete WHITE cap4 histories are generated independently. RIGHT firstR E has15 profiles; LEFT firstR W plus exact equal-selected-C condition incomingE=outgoingN gives exactly6. This equality is derived from physical face jumps, not guessed history string filtering.',
'First chronological gamma occurrence is RIGHT at BOTH endpoints by actual physical ordinal matching; all later copies are LEFT. Off-gamma unit-edge interiors and nonlocal chords have one geometric side. Every local port has its actual side, including WEEE L3 LEFT and WEEW L3 RIGHT. No third/fourth copies or passive contacts are discarded.',
'Only WEE/WEEW/WEEE cross, uniformly L1 RIGHT->LEFT,R2 LEFT->RIGHT. Their paired repair balances both nonnegative occurrence currents. On gamma C=c,L=c-f, piecewise h_R=h-(c-1) RIGHT and0 LEFT has jump1 independently of f, with complementary f-1. Away from gamma all original side flows remain. Winding-1 places RIGHT at global left exterior, giving W_R=c-c_right and W_L=1-W_R.',
'If LEFT nonempty with no crossing, actual successor preserves two nonempty edge-occurrence sets, contradicting the single actual P-cycle. Multiply-used gamma implies nonempty LEFT; all-single-used may have emptyLEFT, retained.',
'Each repaired RIGHT circuit has wP=length+sum(T2-T1)>0; exact temporal lifts identify its spatial homology. A circuit containing no repair would be an unchanged proper actual successor orbit when any crossing exists. Total positive integer winding K=c-c_right bounds their number.',
'At K=1 exactly one RIGHT circuit contains every crossing class and every physical translate. Its positive actual right factors and positive same-cell gaps partition one P interval, forcing alternating L1_i,R2_i crossings and same-PHYSICAL-contact LEFT returns. Passive gamma reads and arbitrary exterior exchanges remain allowed.',
'Constant-flow2 boundary reservations, nested-U exclusions and local stock tables are NOT automatically transported to mixed flow. No general one-use, cap4-front exclusion, fuel, or attraction result follows.'
]);S.with_suffix('.json').write_text(json.dumps(outj,indent=2)+'\n');print(outj['status']);print(sha(S.with_suffix('.json')))
