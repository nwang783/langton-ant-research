import json,sys
from pathlib import Path
p=sys.argv[1];i=int(sys.argv[2]);out=sys.argv[3];q=json.load(open(p+'_port_quotient.json'));r=json.load(open(p+'_patch2_pruned_graph.json'));keep=r['recurrent_components'][i];ix={a:j for j,a in enumerate(keep)}
M=[dict(q['macro_words'][a],old_context_type=a)for a in keep];E=[(ix[a],ix[a],ix[b])for a,b in r['remaining_edges']if a in ix and b in ix]
Path(out+'_port_quotient.json').write_text(json.dumps({'source':p,'kept_context_types':keep,'macro_words':M,'quotient_edges':E,'classes':len(M),'scope':'Eventual residual component after finite use of marked source-context types.'},indent=2));print(out,len(M),len(E))
