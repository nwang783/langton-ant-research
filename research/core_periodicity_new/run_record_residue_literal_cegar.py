"""Discovery loop: exact residue-age resource controls + forbidden literal factors.

CLI DIRECTORY FIRST_EXISTING_ROUND LAST_ROUND. Frozen root_out.json and
patternsNN.json are retained. A finite search cap is never an exclusion.
"""
from pathlib import Path
import sys,json,subprocess
D=Path(sys.argv[1]);first,last=map(int,sys.argv[2:4]);R=Path('/workspace/shared/langton');W=R/'word_stabilization';B=R/'core_periodicity_new';P=B/'chronology_dcuv/delayed_height_probe';history=[r for r in json.loads((D/'summary.json').read_text())if r['round']<first]if(D/'summary.json').exists()else[]
base_dfa=D/'base_dfa.json'if(D/'base_dfa.json').exists()else B/'chronology_dcuv/literal_factor_dfa_k6.json'
def run(cmd,log):
 with log.open('w')as f:subprocess.run(list(map(str,cmd)),stdout=f,stderr=subprocess.STDOUT,check=True)
for n in range(first,last+1):
 tag=f'{n:02}';res=D/f'residue{tag}';inter=D/f'interval{tag}';weighted=D/f'weighted{tag}'
 if n==first and(D/f'weighted{tag}_fast4m.txt').exists():weighted=D/f'weighted{tag}_fast4m'
 if n>first or not weighted.with_suffix('.txt').exists():
  run([sys.executable,W/'refine_packet_dfa_forbidden_factors.py',base_dfa,D/f'patterns{tag}.json',D/f'dfa{tag}'],D/f'dfa{tag}.log')
  run([sys.executable,W/'build_delayed_height_probe.py',D/'root_out.json',D/f'dfa{tag}.json',D/f'geometry{tag}'],D/f'geometry{tag}.log')
  run([sys.executable,B/'build_record_height_petri.py',D/f'geometry{tag}.json',D/f'petri{tag}'],D/f'petri{tag}.log')
  run([sys.executable,B/'build_record_height_residue_age_petri.py',D/f'petri{tag}.json',res,4,P/'u1_k6_residue4_allplaces.json'],D/f'residue{tag}.log')
  run([B/'record_height_age_petri_interval',res.with_suffix('.dat'),8,inter],inter.with_suffix('.log'))
  with weighted.with_suffix('.txt').open('w')as out,weighted.with_suffix('.log').open('w')as err:subprocess.run([str(B/'record_height_age_petri_weightedbest_fast'),str(inter.with_suffix('.dat')),'4000000',str(weighted.with_suffix('.basis')),str(P/'u1_k6_residue4_full.height_weights')],stdout=out,stderr=err,check=True)
 status=weighted.with_suffix('.txt').read_text().splitlines()[0];entry=dict(round=n,status=status,patterns=len(json.loads((D/f'patterns{tag}.json').read_text())),dfa_classes=len(json.loads((D/f'dfa{tag}.json').read_text())['transitions']));history.append(entry)
 if not status.startswith('status AGE_PETRI_WITNESS'):
  (D/'summary.json').write_text(json.dumps(history,indent=2)+'\n');print(json.dumps(entry),flush=True);break
 with inter.with_suffix('.dat').open()as f:m,np,ne,ni,ng=map(int,f.readline().split())
 inter.with_suffix('.json').write_text(json.dumps(dict(format='record_age_petri_identity_control_projection_v1',class_map=list(range(np)),source_file=str(res.with_suffix('.dat')),scope='Identity control map solely for lifting a pruned positive witness; not a no-hit certificate.')))
 replay=weighted.with_suffix('.replay.json');run([sys.executable,B/'replay_record_residue_age_witness.py',res.with_suffix('.json'),inter.with_suffix('.json'),weighted.with_suffix('.txt'),replay],weighted.with_suffix('.replay.log'))
 J=json.loads(replay.read_text());assert J['status']=='FULL_RESIDUE_AGE_WITNESS';bad=J['minimal_illegal_factors'];entry.update(word_length=len(J['word']),illegal_occurrences=len(bad),shortest_illegal_length=len(bad[0]['word'])if bad else None)
 patterns={tuple(p)for p in json.loads((D/f'patterns{tag}.json').read_text())};old=len(patterns);patterns|={tuple(v['word'])for v in bad};entry['new_patterns']=len(patterns)-old
 (D/'summary.json').write_text(json.dumps(history,indent=2)+'\n');print(json.dumps(entry),flush=True)
 if not bad or len(patterns)==old:break
 (D/f'patterns{n+1:02}.json').write_text(json.dumps(sorted(patterns))+'\n')
