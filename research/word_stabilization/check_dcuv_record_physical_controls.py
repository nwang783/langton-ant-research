"""Physical positive controls for historical-record weights; no absence inference."""
from pathlib import Path
import json,sys,hashlib,collections
R=Path(__file__).resolve().parents[1];D=R/'core_periodicity_new/chronology_dcuv';controls=D/'observed_transfers_fast_depth11.json';potential=Path(sys.argv[1]);out=Path(sys.argv[2]);J=json.loads(potential.read_text());v=J['values'];geo=json.loads((D/'literal_residual_geometry.json').read_text());G=geo['geometry'];core={complex(*q)for q in geo['core']};keep=set(J['kept_packet_types']);dr=complex(v['ax'],v['ay']);phase_turn=[1,-1j,-1,1j]
def L(p):return int(p.real)*v['ax']+int(p.imag)*v['ay']
def A(h):return L(complex(-1,1)*phase_turn[h%4])+v[f'c{h%4}']
def peak(a,h):
 g=G[a];e=g['endpoint'];return max([2*L(complex(*e[:2])*phase_turn[h%4])+A(h+e[2])]+[2*L(complex(*q)*phase_turn[h%4])+v[f'w_{a}_{i}_{h%4}']for i,q in enumerate(g['outputs'])])
I=max(peak(a,h)-2*L(complex(*q)*phase_turn[h])for a in keep for h in range(4)for q in G[a]['inputs']);K=max(I+2*L(complex(*q)*phase_turn[h])-A(h)for a in keep for h in range(4)for q in G[a]['inputs']);events=[];unfunded=[];bare_false=[];all_u=[];counts=collections.Counter();scope_factors=0
for wi,w in enumerate(json.loads(controls.read_text())['witnesses']):
 seed={complex(*q)for q in w['initial_black_seed']};p=0j;h=0;board=set(seed)
 for letter in w['raw_word']+w['terminal_marker']:
  assert (p in board)==(letter=='L');board.symmetric_difference_update({p});h=(h+(1 if letter=='R'else-1))%4;p+=1j*phase_turn[h]
 board=set(seed);p=0j;h=0;poses=[];boards=[];tokens={z:None for z in board-core}
 for index,a in enumerate(w['packet_ids']):
  g=G[a];poses.append((p,h));boards.append(set(board));ins=[p+complex(*q)*phase_turn[h]for q in g['inputs']];old=[tokens.pop(q)for q in ins]
  if a in (7,8,9):all_u.append({'witness':wi,'packet_index':index,'packet':a,'initial_inputs':sum(x is None for x in old),'all_produced':all(x is not None for x in old)})
  for q in g['outputs']:
   z=p+complex(*q)*phase_turn[h];assert z not in tokens;tokens[z]=index
  for letter in g['word']:
   assert (p in board)==(letter=='L');board.symmetric_difference_update({p});h=(h+(1 if letter=='R'else-1))%4;p+=1j*phase_turn[h]
  assert board==set(tokens)|{p+z*phase_turn[h]for z in core}
 path=w['packet_ids'];i=0
 while i<len(path):
  if path[i]not in keep:i+=1;continue
  start=i
  while i<len(path)and path[i]in keep:i+=1
  stop=i;scope_factors+=1;p0,h0=poses[start];initial=boards[start]-{p0+z*phase_turn[h0]for z in core}
  for ph in range(4):
   labels={q:None for q in initial};M=bare=2*L(p0*phase_turn[ph])+A(h0+ph)
   for index in range(start,stop):
    a=path[index];p,h=poses[index];g=G[a];ins=[p+complex(*q)*phase_turn[h]for q in g['inputs']];old=[labels.pop(q)for q in ins];prior=M;prior_bare=bare;activated=[]
    for q,producer in zip(ins,old):
     if producer is None:activated.append(I+2*L(q*phase_turn[ph]))
    M=max([M]+activated);created=2*L(p*phase_turn[ph])+peak(a,h+ph);fully=all(z is not None for z in old);counts['packet_phase_checks']+=1;counts['all_produced_input_events']+=fully
    if fully:
     row={'witness':wi,'factor_start':start,'packet_index':index,'packet':a,'phase':ph,'producers':old,'created_peak':created,'previous_historical_max':prior,'previous_bare_max':prior_bare,'unfunded':created>M};events.append(row)
     if created>prior_bare and created<=M:bare_false.append(row)
    if created>M:unfunded.append({'witness':wi,'factor_start':start,'packet_index':index,'packet':a,'phase':ph,'producers':old,'created_peak':created,'funded_max_before':M,'initial_activations':activated})
    M=max(M,created);bare=max(bare,created)
    for q in g['outputs']:
     z=p+complex(*q)*phase_turn[h];assert z not in labels;labels[z]=index
summary={'status':'Exact finite positive-control replay; no all-length absence inference','controls':str(controls),'controls_sha256':hashlib.sha256(controls.read_bytes()).hexdigest(),'potential':str(potential),'potential_sha256':hashlib.sha256(potential.read_bytes()).hexdigest(),'I':I,'activation_cost_K':K,'physical_witnesses':79,'maximal_recurrent8_factors':scope_factors,'counts':dict(counts),'all_U_events_full10':len(all_u),'minimum_initial_U_inputs':min(e['initial_inputs']for e in all_u),'all_produced_U_events':sum(e['all_produced']for e in all_u),'all_produced_by_packet':dict(collections.Counter(G[e['packet']]['name']for e in events)),'unfunded_record_count':len(unfunded),'bare_record_funded_by_earlier_activation_count':len(bare_false),'unfunded_records':unfunded,'bare_record_controls':bare_false,'all_produced_events':events,'U_events':all_u};out.write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps({k:v for k,v in summary.items()if k not in ('unfunded_records','bare_record_controls','all_produced_events','U_events')},indent=2))
