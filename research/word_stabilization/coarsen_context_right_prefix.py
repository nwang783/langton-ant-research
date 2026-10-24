"""Conservative projection: retain RAW word and only k actual right turns."""
import json,sys
from pathlib import Path
p,k,out=sys.argv[1],int(sys.argv[2]),sys.argv[3];q=json.load(open(p+'_port_quotient.json'));M=q['macro_words'];keys=sorted({(a['word'],a['end_marker'][:k])for a in M});ix={v:i for i,v in enumerate(keys)};mp=[ix[(a['word'],a['end_marker'][:k])]for a in M]
assert all(s==a for s,a,t in q['quotient_edges'])
rows=[{'word':w,'end_marker':r,'start_marker':'','old_context_types':[a for a,z in enumerate(mp)if z==i]}for i,(w,r)in enumerate(keys)];E=sorted({(mp[s],mp[s],mp[t])for s,a,t in q['quotient_edges']})
Path(out+'_port_quotient.json').write_text(json.dumps({'source':p,'right_prefix_length':k,'source_type_map':mp,'macro_words':rows,'quotient_edges':E,'classes':len(rows),'scope':'Conservative source-context projection retaining literal raw word and an actual right-context prefix.'},indent=2));print('types',len(rows),'edges',len(E))
