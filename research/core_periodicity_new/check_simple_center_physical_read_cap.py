"""Exact104 physical read cap for a simple corrected-center atomic path."""
from collections import Counter,defaultdict
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parent
GP=ROOT/'chronology_dcuv/literal_residual_geometry.json'
G=json.loads(GP.read_text())['geometry']
WORDS={'D':G[0]['word'],'V':G[4]['word'],'U':G[7]['word'],'C':G[1]['word'][len(G[0]['word']):]}
STEPS=((0,1),(1,0),(0,-1),(-1,0))
def rot(p,h):
 x,y=p;return ((x,y),(y,-x),(-x,-y),(-y,x))[h%4]
def trace(word):
 p,h=(0,0),0;reads=[]
 for tick,t in enumerate(word):
  reads.append({'tick':tick,'cell':p,'heading':h,'turn':t})
  h=(h+(-1 if t=='L' else 1))%4;p=(p[0]+STEPS[h][0],p[1]+STEPS[h][1])
 return reads,(*p,h)
paths={};options=defaultdict(list)
for a,w in WORDS.items():
 reads,endpoint=trace(w);counts=Counter(tuple(r['cell']) for r in reads)
 paths[a]={'word':w,'raw_length':len(w),'endpoint':endpoint,'read_trace':reads,'footprint':[{'local_cell':q,'multiplicity':n} for q,n in sorted(counts.items())]}
 assert endpoint==((0,1,3) if a=='C' else tuple(G[0 if a=='D' else 4 if a=='V' else 7]['endpoint']))
 for h in range(4):
  for q,n in counts.items():
   # Normalize the fixed physical read cell to0. head=-rot(q,h), so twice
   # the entry center is rot((-1,-1)-2q,h).
   center=rot((-1-2*q[0],-1-2*q[1]),h)
   options[center].append({'atom':a,'heading':h,'read_offset':q,'multiplicity':n})
centers=[]
for c,op in sorted(options.items()):
 weight=max(o['multiplicity'] for o in op)
 centers.append({'twice_center_relative_to_fixed_cell':c,'maximum_multiplicity':weight,'all_local_options':op})
assert len(centers)==60
weights=Counter(row['maximum_multiplicity'] for row in centers)
assert weights=={1:28,2:20,3:12}
cap=sum(row['maximum_multiplicity'] for row in centers)
assert cap==104
marker_reads,marker_end=trace(G[0]['marker']);marker_counts=Counter(tuple(r['cell']) for r in marker_reads)
assert len(marker_reads)==11 and max(marker_counts.values())==2
result={'status':'AUTHOR_EXACT_SIMPLE_CENTER_PATH_PHYSICAL_READ_CAP_104',
 'scope':'Any finite atomic D/V/U/C raw path whose corrected-center polygon is injective has at most104 reads of any fixed physical cell. This standalone geometric footprint lemma does not assert injectivity for actual ant histories. A following actual M11 adds at most2 reads per cell. The sum104 is a conservative per-center bound, not a jointly attained word.',
 'four_literal_atomic_read_paths':paths,'all_60_possible_entry_centers_and_maxima':centers,
 'maximum_multiplicity_histogram':dict(weights),'physical_read_cap_raw':cap,
 'terminal_marker_trace':marker_reads,'terminal_marker_endpoint':marker_end,
 'terminal_marker_per_cell_cap':2,'raw_plus_terminal_marker_per_cell_cap':106,
 'dependency_hashes':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in (GP,Path(__file__).resolve())}}
(ROOT/'chronology_dcuv/simple_center_physical_read_cap.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'atomic_raw_lengths':{a:len(w) for a,w in WORDS.items()},'possible_centers':len(centers),'weight_histogram':dict(weights),'raw_cap':cap,'with_terminal_M11_cap':106}))
