from pathlib import Path
from collections import Counter
import json,hashlib
S=Path(__file__).resolve();R=S.parents[1];P=R/'seven_atom_wave_scope_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();mf=P/'manifest.json';assert sha(mf)=='15a0cb354eab78fb9510d15e48e32e5e5854203432ac2087ab13f498adc01c6a'
m=json.loads(mf.read_text())
for k,h in m['files'].items():assert sha(P/k)==h
for k,h in m['dependencies'].items():assert sha(R/k)==h
source=json.loads((R/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json').read_text());W={a:z['word']for a,z in zip('DCVUFQB',source['macro_words'])};M='LLLLRLRRRRL';assert len(set(W.values()))==7
atoms={}
for a,w in W.items():
 pos=[i for i in range(len(w)+1)if(w+M)[i:i+11]==M];assert pos==[0,len(w)];atoms[a]={'length':len(w),'marker_starts':pos}
assert max(map(len,W.values()))==74 and len(W['D'])==10
ref=json.loads((P/'wave_first_return_parse.json').read_text());out=[]
for rr in ref['exact_wave_reports']:
 w=json.loads((R/rr['word_source']).read_text())['word'];n=len(w)
 def sub(i,l):return ''.join(w[(i+j)%n]for j in range(l))
 starts=[i for i in range(n)if sub(i,11)==M];assert starts==rr['cyclic_M11_start_ticks0']
 returns=[]
 for i,a in enumerate(starts):
  b=starts[(i+1)%len(starts)]+(n if i==len(starts)-1 else 0);s=sub(a,b-a);label=next((z for z,v in W.items()if s==v),None)
  assert len([j for j in range(b-a+1)if sub(a+j,11)==M])==2
  z=rr['all_exact_cyclic_first_returns'][i];assert z['canonical_period_tick0']==a and z['unwrapped_end_tick0']==b and z['RAW_length']==b-a and z['literal_word']==s and z['seven_atom']==label and z['word_sha256']==hashlib.sha256(s.encode()).hexdigest()
  returns.append((a,b,label))
 counts=Counter(z or'OUTSIDE_SEVEN'for a,b,z in returns)
 assert dict(counts)==rr['first_return_counts'] and sum(b-a for a,b,z in returns)==n
 occ={}
 for a in('D','C','V','U','F','Q','B','UC','UCC'):
  raw=''.join(W[x]for x in a);bare=[i for i in range(n)if sub(i,len(raw))==raw];complete=[i for i in range(n)if sub(i,len(raw)+11)==raw+M];r=next(z for z in rr['all_atom_and_U_family_RAW_and_complete_occurrences']if z['packet']==a);assert bare==r['exact_RAW_occurrence_ticks0']and complete==r['exact_RAW_plus_actual_M11_occurrence_ticks0'];occ[a]=(len(bare),len(complete))
  if a in('V','U','F','Q','B','UC','UCC'):assert bare==complete==[]
 outside=[(a,b)for a,b,z in returns if z is None];rep=rr['representative_nonwrapping_outside_return'];assert(rep['canonical_period_tick0'],rep['unwrapped_end_tick0'])in outside
 out.append({'period':n,'starts':starts,'returns':returns,'counts':dict(counts),'bare_complete_counts':occ,'nonwrapping_long_interval':(rep['canonical_period_tick0'],rep['unwrapped_end_tick0'])})
assert out[0]['counts']=={'C':7,'OUTSIDE_SEVEN':14}and out[1]['counts']=={'C':14,'D':3,'OUTSIDE_SEVEN':28}
assert out[0]['nonwrapping_long_interval']==(30,151)and out[1]['nonwrapping_long_interval']==(107,190)
res={'status':'PASS phase-independent literal seven-atom exclusion for the two named waves only','manifest':sha(mf),'all_atoms':atoms,'independently_reparsed_waves':out,'analytic_review':[
'Each seven-atom RAW followed by the actual marker has marker starts exactly at0 and its RAW end. This handles D RAW10 even though marker length11: its start marker includes the next actual word first read. No extra marker is executed.',
'Any bi-infinite or cyclic tiling by these seven RAW atoms must make every actual marker occurrence an atom boundary, since none may lie strictly inside an atom, including a marker crossing its endpoint. Thus every consecutive marker interval must be one exact atom. Both periodic words have explicit nonwrapping intervals longer than maximum74, so no phase or period multiple admits the tiling.',
'The proof scans all cyclic start positions, including seam-crossing matches, and distinguishes bare RAW occurrences from RAW plus actual following marker. Bare D10 is the marker prefix and is not a complete D atom. No V/U/F/Q/B or UC/UCC RAW occurs, so no stationary genuine U-family entry can be supplied.',
'Only frozen words were parsed. Complete prepared backgrounds, unread cells and XOR caps are retained unchanged and are not premises for this pure word obstruction. Named finite-wave episodes contain these intervals but this supplies no wave proxy, global coverage, physical first-contact, termination or attraction theorem.'
]}
S.with_suffix('.json').write_text(json.dumps(res,indent=2)+'\n');print(res['status'])
