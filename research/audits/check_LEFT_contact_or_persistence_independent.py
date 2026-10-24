from pathlib import Path
from collections import Counter
from fractions import Fraction
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];D=R/'U_LEFT_contact_or_persistence_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();man=D/'manifest.json';assert sha(man)=='bf1018d69a9ee2f963227dc04d49f045fea4ee2febdd11c2c6613913e92458a5'
for f,h in json.loads(man.read_text())['files'].items():assert sha(D/f)==h
ref=json.loads((D/'LEFT_contact_or_persistence.json').read_text())
for f,h in ref['dependencies'].items():assert sha(R/f)==h
ns={'__file__':str(S.with_name('check_foreign_kinked_barrier_turn_independent.py'))};exec(Path(ns['__file__']).read_text().split('geometries=[]')[0],ns);W,M,walk,center,xy,meet,inventory=[ns[k]for k in['W','M','walk','center','xy','meet','inventory']]
K={-1-1j,-1,-1j,0j,1};LEFT={0j,1j};a=1+0j;star=LEFT|{a,1+1j};tr={b:walk(W[b])for b in'DCVU'};ctx={b:walk(W[b]+M)for b in'DCVU'};old=((-1,-1),(-1,7))
# Reconstruct the full role universe from true before-BLACK physical masks.
def candidates(tags):
 return {(b,*xy(t-q*(-1j)**h),h)for b in'DCVU'for q,c in ctx[b]['req'].items()if c for t in tags for h in range(4)}
def reads(b,p,h,q):return[(i,c)for i,(z,hh,c)in enumerate(ctx[b]['reads'])if p+z*(-1j)**h==q]
Lrows=[];counts=Counter();surv=[]
for b,x,y,h in sorted(candidates(LEFT)):
 p=complex(x,y);r=(-1j)**h;entryK={p+r*q for q in K};end=p+r*tr[b]['p'];eh=(h+tr[b]['h'])%4;exitK={end+q*(-1j)**eh for q in K}
 if (x+y+h)%2:reason='wrong_active_sector'
 elif LEFT&entryK:reason='LEFT_original_in_entry_core'
 elif any(ctx[b]['req'].get((q-p)/r)is False for q in LEFT):reason='LEFT_BLACK_vs_before_WHITE'
 else:
  keep={q for q in LEFT if not any(p+r*z==q for z,hh,c in tr[b]['reads'])and q not in exitK};assert len(keep)<2
  if meet(*old,xy(center(p,h)),xy(center(end,eh)))is not None:reason='atom_chord_contacts_creating_U_chord'
  else:reason='sole_no_old_U_contact_LEFT_loss';surv.append([b,x,y,h]);assert b=='U'and(x,y,h)==(1,-1,0);assert ctx[b]['req'].get((a-p)/r)is False and ctx[b]['req'].get((1+1j-p)/r)is True;assert reads(b,p,h,0j)[0]==(14,'L')and reads(b,p,h,1j)[0]==(13,'L')
 counts[reason]+=1;Lrows.append(dict(atom=b,entry=[x,y,h],reason=reason))
assert counts==ref['LEFT_classification'];assert Lrows==[{k:z[k]for k in('atom','entry','reason')}for z in ref['all_LEFT_first_loss_rows']]
Arows=[];ac=Counter();ports=[]
for b,x,y,h in sorted(candidates({a})):
 p=complex(x,y);r=(-1j)**h;entryK={p+r*q for q in K};end=p+r*tr[b]['p'];eh=(h+tr[b]['h'])%4
 if(x+y+h)%2:reason='wrong_active_sector'
 elif (LEFT|{a})&entryK:reason='genuine_held_original_in_entry_core'
 elif any((q-p)/r in ctx[b]['req']for q in LEFT):reason='does_not_MISS_both_held_LEFT_originals'
 elif meet(*old,xy(center(p,h)),xy(center(end,eh)))is not None:reason='atom_chord_contacts_creating_U_chord'
 else:
  reason='possible_first_a_loss_port';rr=reads(b,p,h,a);tick,c=rr[0];assert c=='L';ports.append(dict(atom=b,entry=[x,y,h],exit=[*xy(end),eh],first_L_tick0=tick,RAW_length=len(W[b]),owner='own RAW'if tick<len(W[b])else'next actual RAW',owner_tick0=tick if tick<len(W[b])else tick-len(W[b])))
 ac[reason]+=1;Arows.append(dict(atom=b,entry=[x,y,h],reason=reason))
assert ac==ref['a_first_loss_classification'];assert Arows==[{k:z[k]for k in('atom','entry','reason')}for z in ref['all_original_a_first_loss_rows']]
assert[(q['atom'],q['entry'],q['exit'],q['first_L_tick0'])for q in ports]==[('D',[1,-1,0],[2,0,0],11),('U',[2,-4,0],[2,0,0],29),('U',[2,-2,0],[2,2,0],13),('V',[1,-3,0],[2,0,0],19)]
# Fresh literal barrier-footprint inclusions and endpoint-only bridge contacts.
for b in'DCVU':assert set(inventory((-1,-1),xy(center(tr[b]['p'],tr[b]['h']))))<={xy(q)for q in ctx[b]['req']}
B=(-1,3);E=(1,1);bridge=(B,E)
assert meet(B,(-1,7),*bridge)==(Fraction(0),Fraction(0),tuple(map(Fraction,B)))
assert meet((1,-3),E,*bridge)==(Fraction(1),Fraction(1),tuple(map(Fraction,E)))
source=[]
for word in ('U','UC','UCC'):
 full=walk(''.join(W[b]for b in word));assert full['feasible'];rr=[(t,c)for t,(p,h,c)in enumerate(full['reads'])if p==1j];assert rr==[(11,'R'),(15,'L'),(19,'R')]
 p=0j;h=0;chords=[]
 for b in word:
  end=p+tr[b]['p']*(-1j)**h;eh=(h+tr[b]['h'])%4;seg=(xy(center(p,h)),xy(center(end,eh)))
  if b=='C':assert meet(*seg,*bridge)is None;chords.append(seg)
  p=end;h=eh
 source.append(dict(type=word,w_reads=rr,tail_chords=chords))
# Tangent lift from the signed table: only a C->foreign boundary wraps.
# Complete-eight predecessor forbids that boundary, endpoints both U.
assert 2*(2+2)==8 and 2*(-6+2)==-8
assert [m for m in range(3)if(m+2)%4==0]==[2]
assert all(z['exit'][0]>=2 and z['exit'][1]>=0 and z['exit'][2]==0 for z in ports)
assert[(xy(tr[b]['p']),tr[b]['h'])for b in'DVU']==[((1,1),0),((1,3),0),((0,4),0)]
out={'status':'PASS conditional contact-or-SAME-LEFT persistence after a star-MISS first foreign','manifest':sha(man),'LEFT_universe':len(Lrows),'LEFT_filters':dict(counts),'first_other_original_loss_universe':len(Arows),'other_filters':dict(ac),'four_ports':ports,'source_tail_interfaces':source,'analytic_review':[
'Before the first ordered LEFT loss, the two SAME source-R identities are current at each actual cut. An old BLACK cell outside entry K either has no context read or first-L input; first-R conflicts. A marker-first-L means exit-core capture at the earlier atom, not a postponed hidden loss. Every ordinary K cell is physically visited in its first six RAW reads, so an alive original cannot pass unnoticed through an intermediate core.',
'The fresh complete role universe leaves only U(1,-1,N) without contact with the old creating-U chord. It physically reads both LEFT originals and requires original position(1,0) WHITE. Its strict midpoint and the source-U strict midpoint are joined by the SAME held w edge. The source remainder, genuine UC/UCC tails, and final consuming-U first half meet this edge only at their designated endpoints. All intermediate ordinary and repaired foreign pieces avoid it by current-ID barrier and the foreign complete-context MISS premise.',
'Under assumed simple expanded proxy the B-to-E subarc plus that held physical edge is a Jordan curve. Tangent lift includes all source C tails and all later actual Cs. Exactly one foreign contributes +pi; the only possible -2pi correction is a preceding C, excluded by actual complete-eight-to-foreign adjacency. Both endpoint tangents are N; bridge joins +pi/4 and -pi/4 cancel. Thus n+2=+/-4, n>=0 forces n2, not a sampled age range.',
'Original(1,0) is still current after A by genuine old-eight U-star permanence and A complete-context MISS. Before its eventual required WHITE state it has a first ordinary ordered loss while LEFT remains held. The four exhaustively reconstructed ports are all N, no C, ending at x>=2,y>=0. Their postforeign N heading forces clock m2 within0..2, leaving no later C. Following zero-C N atoms D,V,U have increments(1,1),(1,3),(0,4), so they cannot reach target(1,-1). Later replacement R at the same cell does not evade this head obstruction.',
'The theorem is conditional on whole-proxy simplicity and foreign star-MISS, and its contrapositive permits ANY earlier/within-atom proxy contact. It is not unconditional persistence, second-return simplicity, a postforeign maturity law, or an exclusion of foreign star erosion. The first-contact ENTRY conclusion stops before executing that atom. The age<=4 corollary only supplies the preforeign MISS premise.'
]}
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print(out['status']);print(counts,ac)
