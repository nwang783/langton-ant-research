#!/usr/bin/env python3
"""All-length exact language of the four standard discovery-cycle modules."""
from pathlib import Path
from collections import defaultdict
import itertools,json,hashlib,sys
from check_extremal_read_coupling import event_word,quotient
from check_all_cut_wave_interfaces import WORDS
R=Path(__file__).resolve().parent
sys.path.insert(0,str(R.parent/'computability'))
from periodic_tail_checker import first_mismatch
from check_rigid_reachability import State

def finite(w,h0=3):
 E,d,h=event_word(w,h=h0);seen={};seed=set();field=set();witness=None
 for e in E:
  q=e['p'];c=e['c']
  if q in seen and seen[q]['c']==c:
   witness={'cell':q,'first':seen[q],'second':e,'complete_visits_between':[z for z in E if z['p']==q and seen[q]['t']<=z['t']<=e['t']]};break
  if q not in seen and c=='L':seed.add(q);field.add(q)
  field.symmetric_difference_update({q});seen[q]=e
 if witness:
  assert len(witness['complete_visits_between'])==2
  return {'word':w,'legal_on_some_board':False,'witness':witness}
 return {'word':w,'legal_on_some_board':True,'initial_black':sorted(seed),'final_black':sorted(field),'head':d,'heading':h,'all_events':E}

def main():
 S=WORDS['S104'];part=lambda i,n:''.join(S[(i+j)%104]for j in range(n))
 words={'A':part(45,10),'B':part(55,94),'C':part(13,14),'D':part(27,90)}
 assert words['A']=='RRRRLLLLRL';assert words['A']+words['B']==part(45,104);assert words['C']+words['D']==part(13,104)
 profiles={};delta=(-1,1)
 for a,w in words.items():
  E,d,h=event_word(w,h=3);assert d==delta and h==3
  H=defaultdict(list)
  for e in E:q,k=quotient(e['p'],delta);H[q].append({'relative_module_index':-k,**e})
  profiles[a]={'word':w,'length':len(w),'growth':w.count('R')-w.count('L'),'full_events':E,'complete_sources':[{'representative':q,'reads':sorted(es,key=lambda z:(z['relative_module_index'],z['t']))}for q,es in sorted(H.items())]}
 pairs={a+b:finite(words[a]+words[b])for a,b in itertools.product(words,repeat=2)}
 legal=[w for w,z in pairs.items()if z['legal_on_some_board']];assert legal==['AA','AB','BA','CA','CD','DC']
 triples={w:finite(''.join(words[a]for a in w))for w in['AAB','CAB']}
 assert all(not z['legal_on_some_board']for z in triples.values())
 # Keep the precise complete cell histories, not only the earliest failure flag.
 assert (triples['AAB']['witness']['first']['t'],triples['AAB']['witness']['second']['t'],triples['AAB']['witness']['cell'])==(5,45,(0,-1))
 assert (triples['CAB']['witness']['first']['t'],triples['CAB']['witness']['second']['t'],triples['CAB']['witness']['cell'])==(10,50,(1,-1))
 assert len(pairs['CA']['initial_black'])==2 and len(pairs['CA']['final_black'])==6
 # Finite transition proof obligations, transparent without SCC or a solver.
 succ={a:[b for b in words if pairs[a+b]['legal_on_some_board']]for a in words}
 assert succ=={'A':['A','B'],'B':['A'],'C':['A','D'],'D':['C']}
 assert [b for b in succ['A']if 'AA'+b not in triples]==['A']
 assert [b for b in succ['A']if 'CA'+b not in triples]==['A']
 surviving=[w for w in legal if w not in['AA','CA']];assert surviving==['AB','BA','CD','DC']
 # Both positive cycles materialized on the complete literal blank trajectory.
 base=9977+3*104;cuts={base+13:'CD',base+45:'AB'};B=set();p=(0,0);h=0;states={};V=[(0,1),(1,0),(0,-1),(-1,0)]
 for t in range(max(cuts)+1):
  if t in cuts:
   W=''.join(words[a]for a in cuts[t]);state=State(frozenset(B),p,h);assert first_mismatch(state,W)is None
   states[cuts[t]]={'time':t,'black':sorted(B),'head':p,'heading':h,'word':W,'exact_infinite_checker_result':None}
  if t==max(cuts):break
  c='L'if p in B else'R';B.symmetric_difference_update({p});h=(h+(1 if c=='R'else-1))%4;p=(p[0]+V[h][0],p[1]+V[h][1])
 # Proper rotations of every literal pair/triple preserve all conclusions.
 rot=[]
 for h in range(4):
  for w,z in {**pairs,**triples}.items():
   zz=finite(''.join(words[a]for a in w),h);assert zz['legal_on_some_board']==z['legal_on_some_board']
   if not zz['legal_on_some_board']:assert (zz['witness']['first']['t'],zz['witness']['second']['t'],zz['witness']['first']['c'])==(z['witness']['first']['t'],z['witness']['second']['t'],z['witness']['first']['c'])
   rot.append({'word':w,'heading':h,'compatible':zz['legal_on_some_board']})
 out={'status':'AUTHOR all-length intrinsic four-module language classification; independent audit pending',
  'scope':'Only these four literal fixed-cut modules with a common orientation, no inserted router. No statement that arbitrary trajectories admit this alphabet.',
  'module_profiles':profiles,'common_heading':3,'common_displacement':delta,'all16_pair_controls':pairs,'two_triple_controls':triples,
  'all_legal_pair_edges':legal,'successor_table':succ,'edges_left_after_finite_field_infinite_tail_filter':surviving,
  'full_blank_standard_positive_controls':states,'all72_rotation_controls':rot,
  'theorem_statements':['Every stable periodically repeated module word, even on an infinitely prepared board, is a power/phase of A alone, AB, or CD. A alone needs its signed infinite input ray.','Every complete WHITE periodic word in this alphabet is a standard104 power/phase.','An infinite actual trajectory from a finite whole field that follows this alphabet from its initial module must alternate AB or CD from that module. AA or CA would force A forever, impossible with finite input stock.'],
  'dependencies':{str(p):hashlib.sha256(p.read_bytes()).hexdigest()for p in[R/'STANDARD_TWO_MODULE_ALL_LENGTH_CLASSIFICATION.md',R/'standard_two_module_language_certificate.json',R/'C_CYCLE_EXCURSIONS_AND_STANDARD_SELF_FEEDING.md',R.parent/'computability/periodic_tail_checker.py',R.parent/'computability/check_rigid_reachability.py']}}
 dest=R/'four_intrinsic_module_language_certificate.json';dest.write_text(json.dumps(out,indent=2)+'\n');print('PASS six literal pair fields, ten pair obstructions, two triple obstructions; only A / AB / CD periodic candidates');print('CA input/output',pairs['CA']['initial_black'],pairs['CA']['final_black']);print('full positive field sizes',{a:len(s['black'])for a,s in states.items()});print(hashlib.sha256(dest.read_bytes()).hexdigest())
if __name__=='__main__':main()
