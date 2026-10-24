import json,sys
from pathlib import Path
base=sys.argv[1];out=sys.argv[2];g=json.load(open(base+'_grammar.json'));M=g['macros'];pairs=[tuple(w)for w in g['pairs']];idx={p:i for i,p in enumerate(pairs)}
macros=[{'word':M[a]['word'],'end_marker':M[b]['word']+M[b]['end_marker'],'context':[a,b],'start_marker':M[a]['start_marker']}for a,b in pairs];edges=sorted({(idx[(a,b)],idx[(a,b)],idx[(b,c)])for a,b,c in g['triples']})
Path(out+'_port_quotient.json').write_text(json.dumps({'macro_words':macros,'quotient_edges':edges,'classes':len(pairs),'scope':'overlapping two-macro context presentation; raw block remains the first original macro'},indent=2));print('context objects',len(pairs),'edges',len(edges))
