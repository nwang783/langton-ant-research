from pathlib import Path
import json,hashlib,sys
SELF=Path(__file__).resolve();R=SELF.parents[1];D=R/'stateful_growth_application_2026-10-23';a=json.loads((D/'guard_exchange_exit.json').read_text());g=json.loads((D/'guard_exchange.json').read_text());sample=json.loads((D/'guard_exchange_exit_M50_r51.json').read_text());V='LLRLRRRRLRRRRLLLLRLR';dirs=(1j,1,-1j,-1)
assert V==(R/'new_constructive_2026-10-23/two_layer_gap_frame_r10_k10.word.txt').read_text()[960:980]
sys.path.insert(0,str(R/'stateful_growth_quadratic_2026-10-23'));from quadratic_lap_validator import Context
ctx=Context(max_operations=10000000);before=ctx.set(g['complete_returned_relation']);after=before;p=0j;h=1;odd=set();domain='M>=1 and r>=10 and r>M'
def cell(p):return ctx.set(f'[M,r]->{{[x,y]:{domain} and x=-2M+{int(p.real)} and y={int(p.imag)}}}')
for ch in V:
 q=cell(p);actual=after.intersect(q);assert actual.is_equal(q)if ch=='L'else actual.is_empty();after=after.subtract(q).union(q.subtract(after));odd.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
assert(p,h)==(-4,3);clear={0,1j,-1+2j};add={-2+3j,-1+3j,-2+1j,-3+2j,-3};assert odd==clear|add
for q in clear:assert before.intersect(cell(q)).is_equal(cell(q))and after.intersect(cell(q)).is_empty()
for q in add:assert before.intersect(cell(q)).is_empty()and after.intersect(cell(q)).is_equal(cell(q))
assert after.is_equal(ctx.set(a['complete_returned_relation']));assert all(after.intersect(cell(q)).is_empty()for q in(-1,0,1j,-4))
old=json.loads((D/'guard_exchange_M50_r51.json').read_text());assert sample['word']==old['word']+V and sample['seed']==old['seed'];black={complex(*q)for q in old['seed']};p=0j;h=1
for ch in sample['word']:assert(p in black)==(ch=='L');black.symmetric_difference_update({p});h=(h+(1 if ch=='R'else-1))%4;p+=dirs[h]
assert(p,h,len(black),len(sample['word']))==(-104,3,121,1480);assert black=={complex(*q)for q in sample['returned']}
note=D/'guard_exchange_exit.md';out=dict(status='PASS exact no-new-fuel two-guard physical exit with complete retained field',note_sha256=hashlib.sha256(note.read_bytes()).hexdigest(),domain=domain,clears=sorted((int(q.real),int(q.imag))for q in clear),adds=sorted((int(q.real),int(q.imag))for q in add),pose_relative=[-4,0,3],sample={'reads':1480,'input_mass':107,'output_mass':121},scope='Same complete minimum seed, all parameter values; new live port is white and west-headed, not a clean old-port restart. No next outbound supply or repeatability is certified.')
SELF.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(out['note_sha256'])
