from pathlib import Path
from collections import defaultdict,Counter
from functools import lru_cache
import json,hashlib
S=Path(__file__);R=S.parents[1];D=R/'Q_B_hook_three_C_foreign_transfer_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();MF=D/'manifest.json';assert sha(MF)=='11b355e04075d4663789eca8d80a9da7b5b91cf8c0c4a7cdabb4156db4464be6';mf=json.loads(MF.read_text())
for f,h in mf['files'].items():assert sha(D/f)==h
for f,h in mf['dependencies'].items():assert sha(R/f)==h
J=json.loads((D/'three_C_hook_transfer.json').read_text());ns={'__file__':str(S.with_name('check_old_V_second_age1_independent.py'))};exec(Path(ns['__file__']).read_text().split('# Universal')[0],ns);W,M,K,tr,rot,xy=[ns[k]for k in('W','M','K','tr','rot','xy')];key=lambda q:(q.real,q.imag)
HOOK={-1-1j,-2-1j,-3-1j,-3-2j};NE={-1-1j,-1,-1+1j,0j,1j,1,1+1j,1+2j,2,2+1j};FIELD=HOOK|NE;assert len(FIELD)==13
@lru_cache(None)
def ctx(packet):
 raw=''.join(W[a]for a in packet);z=tr(raw+M);first={}
 for t,(p,h,c)in enumerate(z['reads']):first.setdefault(p,(c,t))
 return z,first
I={a:{q for q,(c,t)in ctx(a)[1].items()if c=='L'and q not in K}for a in'DCVUFQB'};assert not I['C']and sum(len(I[a])for a in'DVU')==8
raw={a:tr(W[a])for a in W}
def signature(packet,p,h):
 first=ctx(packet)[1];out=[]
 for g in sorted(FIELD,key=key):
  loc=(g-p)/rot(h);f=first.get(loc)
  if loc in K or(f and f[0]=='R'):out.append((tuple(xy(g)),tuple(xy(loc)),'ENTRY_CORE'if loc in K else'first_WHITE',None if f is None else(f[1],f[0])))
 return out

def checkconf(packet,p,h,rows):
 got=signature(packet,p,h);want=[]
 for r in rows:
  own=r['first_read'];f=None if own is None else(own['context_tick0'],own['turn'])
  if own is not None:
   t=own['context_tick0'];assert own['context_read_number1']==t+1 and own['RAW_length']==sum(len(W[a])for a in packet)
   off=0
   for a in packet:
    if t<off+len(W[a]):assert own['owner_tick0']==t-off and own['turn']==W[a][t-off];break
    off+=len(W[a])
   else:assert own['owner_tick0']==t-off and own['next_word_tick0']==t-off and own['turn']==M[t-off]
  want.append((tuple(r['SAME_initial_cell']),tuple(r['local_cell']),r['reason'],f))
 assert got==want
for rr in J['all2_source_birth_interfaces']:
 a=rr['source'];z=raw[a];oo={q for q,(c,t)in z['last'].items()if c=='R'and(q-z['p'])/rot(z['h'])not in K};assert FIELD|{-4+1j,-4-1j}<=oo and z['h']==2 and z['p'].imag<=-4
 assert rr['actual_EXIT']==[*xy(z['p']),2]and rr['tracked_originals']==[dict(cell=xy(q),own_last_R_tick0=z['last'][q][1])for q in sorted(FIELD|{-4+1j,-4-1j},key=key)]and z['last'][-4-1j]==('R',55)
counts=Counter();gate=[]
for g in NE:
 for a in'DVU':
  for slot in I[a]:
   p=g-rot(3)*slot;kind='sector'if(int(p.real+p.imag)+3)%2 else('held_FIELD'if signature(a,p,3)else'only_possible_W3_first_NE_loss')
   rr=next(r for r in J['all80_first_NE_loss_W3_roles']if r['cell']==xy(g)and r['consumer']==a and r['true_input']==xy(slot));assert rr['ENTRY']==[*xy(p),3]and rr['route']==kind
   if kind!='sector':checkconf(a,p,3,rr['conflicts'])
   if kind=='only_possible_W3_first_NE_loss':gate.append((g,a,p,slot))
   counts[kind]+=1
assert counts=={'sector':40,'held_FIELD':39,'only_possible_W3_first_NE_loss':1}and gate==[(1+2j,'U',2+3j,-1+1j)]and tr(W['U'],2+3j,3)['p']==-2+3j
goals=defaultdict(list)
for a in'FQB':
 for g in HOOK:
  for slot in I[a]:
   p=g-rot(3)*slot
   if(int(p.real+p.imag)+3)%2==0:goals[a,p].append((g,slot,ctx(a)[1][slot][1]))
assert len(goals)==57;stats=Counter();kept=set()
for(a,p),ws in goals.items():
 rr=next(r for r in J['all57_next_foreign_hook_loss_poses_unspent_NE_branch']if r['target']==a and r['ENTRY']==[*xy(p),3]);assert set(ws)=={(complex(*r['cell']),complex(*r['true_input']),r['first_L']['context_tick0'])for r in rr['hook_input_witnesses']};checkconf(a,p,3,rr['conflicts']);kind='held_FIELD'if signature(a,p,3)else'extra_source_output_guard';assert rr['route']==kind;stats[kind]+=1
 if kind=='extra_source_output_guard':kept.add((a,p))
assert stats=={'held_FIELD':53,'extra_source_output_guard':4}and kept=={(a,-4+1j)for a in'FQB'}|{('B',-5+0j)}
assert max(p.imag for a,p in goals)==4 and {(a,p)for a,p in goals if p.imag>=4}=={(a,x+4j)for a in'FQB'for x in(-1,1)}
assert(tr(W['C'],3+3j,0)['p'],tr(W['C'],3+3j,0)['h'])==(3+4j,3)
assert tr(W['C']+W['U'])['bad'][:2]==(29,1)
for a in'DVU':assert raw[a]['p'].imag>0
assert [tr(W[a],0j,3)['p']for a in'DVU']==[-1+1j,-3+1j,-4+0j]
@lru_cache(None)
def paths(dx,dy):
 if dx<0 or dy<0:return ()
 if dx==dy==0:return ('',)
 out=[]
 for a,x,y in [('D',1,1),('V',3,1),('U',4,0)]:
  if dx>=x and dy>=y:out.extend(a+w for w in paths(dx-x,dy-y))
 return tuple(out)
packets=[]
for a,p in goals:
 for suffix in paths(int(-2-p.real),int(p.imag-3)):
  packet='U'+suffix+a;zz=ctx(packet)[0];assert not zz['bad'];assert tr(''.join(W[z]for z in packet[:-1]),2+3j,3)['p']==p
  rr=next(r for r in J['all4_endpoint_exhaustive_W_continuations_after_W3_first_NE_loss']if r['packet']==packet);assert rr['suffix_after_first_U']==suffix and rr['target_ENTRY']==[*xy(p),3];checkconf(packet,2+3j,3,rr['immutable_initial_FIELD_conflicts']);assert signature(packet,2+3j,3);packets.append(packet)
assert sorted(packets)==['UB','UF','UQ','UUQ']
ports=[]
for a in'DVU':
 for slot in I[a]:
  delta=raw[a]['p']-slot;wd=rot(3)*delta
  assert slot.imag>=1 and-slot.real<=1 and delta.imag>=0 and(delta.imag>0 or delta.real==1)and wd.imag>=0 and(wd.imag>0 or wd.real<=-1)
  rr=next(r for r in J['all8_true_input_exit_bounds']if r['atom']==a and r['true_input']==xy(slot));assert rr['N_RAW_EXIT_minus_tag']==xy(delta)and rr['W_RAW_EXIT_minus_tag']==xy(wd)and rr['actual_L']['context_tick0']==ctx(a)[1][slot][1];ports.append((a,slot,delta,wd))
assert len(ports)==8
for a in'FQB':assert(-4+1j-(-4+1j))/rot(3)in K
r=-4-1j;target=-5+0j;assert(r-target)/rot(3)in K
for a,slot,delta,wd in ports:
 p=r-rot(3)*slot;ep=p+rot(3)*raw[a]['p'];dx=int(ep.real-target.real);dy=int(target.imag-ep.imag);assert not paths(dx,dy)
 rr=next(z for z in J['final_B_R55_current_guard']['all8_W3_first_loss_exit_equations']if z['consumer']==a and z['input']==xy(slot));assert rr['actual_ENTRY']==[*xy(p),3]and rr['actual_RAW_EXIT']==[*xy(ep),3]and rr['remaining_W_displacement_weights']==[dx,dy]and rr['remaining_counts_D_V_U']==[]
assert all(-3-4*u!=-5 for u in range(3)) # Exact nonnegative integer equation4u=2 is impossible.
controls=[]
for rr in J['genuine_three_C_prefix_controls']:
 packet=rr['packet'];word=''.join(W[a]for a in packet)+M;z=tr(word);assert not z['bad'];seed={q for q,b in z['req'].items()if b};assert sorted(map(xy,seed))==rr['seed']and len(seed)==rr['seed_mass'];B=set(seed)
 for q,h,c in z['reads']:assert(q in B)==(c=='L');B.symmetric_difference_update({q})
 exit=tr(word[:-len(M)]);assert rr['RAW_EXIT']==[*xy(exit['p']),exit['h']]and rr['after_actual_M_prefix']==[*xy(z['p']),z['h']]and rr['actual_reads']==len(word)and rr['final_mass']==len(B)
 controls.append(dict(packet=packet,seed=len(seed),reads=len(word),final_mass=len(B)))
O=dict(status='PASS generic one next-FOREIGN Q/B SAME hook transfer after exactly three ordinary Cs only',manifest=sha(MF),script=sha(S),W_first_loss_counts=dict(counts),foreign_unspent_counts=dict(stats),endpoint_exhaustive_W_continuations=sorted(packets),complete_input_exit_bounds=8,controls=controls,analytic_review=[
'ActualsourceQ/B births give13distinctNE/hookIDs plus twoauxiliarytags; sharedR46notdoublecounted andR55at-4,-1genuineexternalO. Ordinaryhookmin4 isusedonlythroughordinaryC3. S0/E1preserveNE, signedN2firstloss istrueU3,-1includingits simultaneousinputs. C hasnoexternalinputorunaccountedCOREcapture.',
'Fresh80W3roles give40sector39heldCORE/firstWHITE andoneU2,3gate. Everytrueinputincludingmarker-ownedCURRENTcapture retained; arbitraryextraentrycolors cannotrepair aheldoriginalCORE/WHITEconflict. IfNEsurvivesnextentry,57foreigntruehookposes split53field+fourtargets. This isnot assumingNEthroughforeign.',
'AnN2gate exits3,3N; subsequentNbase strictlyraisesy andC3adds1. Allhooktargets y<=4, equalityonlyx+-1. EqualityforbidsNbases/W D,V; anynonemptyheightpreservingWrailwouldstartUimmediatelyafterC, literalCU repeatedL1/29. ThusNspentbranchcannotreachanytarget, withno railbound.',
'Wfirstgate exits-2,3W. Exactnonnegative displacementdx=d+3v+4u,dy=d+v derivesallorderswithoutdepthcap andonlyUF,UQ,UUQ,UB. Eachwholeword isfreelyprepared-feasiblebut firstR conflictswithanoriginal13fieldidentity currentatgateentry. FullpacketRAW/markerownerlabels independentlyreconstructed; neitherallfieldpersistenceaftergate norphysicalretirementisassumed.',
'Auxiliarytagsa=-4,1 andr=-4,-1cannotloseS/E byactualinputcones. EveryNfirstloss RAWexity>=tagy,equalityexitx=tagx+1; everyWloss exity>=tagy,equalityexitx<tagx. ActualCs/strictNrise andmonotoneW displacement makeaCURRENTat-4,1targetCORE. Forr/B-5,0 anNloss requires-3,-1thenCto-3,0 and4u=2impossible; all8Wloss exitsemigroups havezerosolutions. TheseareCURRENT first-loss proofs retainingaliveCORE inputs, notrestoration/age assumptions.',
'AllcandidatefirsthookCURRENTlosses inthenextFOREIGN arethereforeeitherentryCORE/firstWHITE contradictionsorexhaustivelyexcludedtrueinputs. Samefourhooks surviveitsRAWexitandactualM. Togetherwithsigned330 gives0..3CsforONE nextforeign, notiteration, sourceF, C4, arbitrarytailsimplicity, languageentry orcapture. Genuine31/34cell UQ/UBthreeCprefixes replaywhole194/204reads andremainvalid.'
]);S.with_suffix('.json').write_text(json.dumps(O,indent=2)+'\n');print(O['status']);print(sha(S.with_suffix('.json')))
