"""Independent integer verifier for the saved fold-only Farkas certificate.

No optimizer, floating arithmetic, ContextProblem, or energy_row is used.
Every supported inequality is reconstructed directly from its black/white
context and the supplied outside bits.
"""
from pathlib import Path
import json,gzip,hashlib
from collections import Counter

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent

def canonical(pattern):
    forms=[]
    for _ in range(4):
        forms.append(pattern)
        pattern=sum(((pattern>>(x+3*y))&1)<<((2-y)+3*x)
                    for y in range(3) for x in range(3))
    return min(forms)

def canonical_sector(phase,pattern):
    forms=[]
    for _ in range(4):
        forms.append((phase<<9)|pattern)
        phase^=1
        pattern=sum(((pattern>>(x+3*y))&1)<<((2-y)+3*x)
                    for y in range(3) for x in range(3))
    return min(forms)

def coefficients(context,outside,sector=False):
    fixed_black=set(map(tuple,context['initial_black']))
    fixed_white=set(map(tuple,context['initial_white']))
    toggled=set(map(tuple,context['toggled']))
    assert not fixed_black&fixed_white
    assert toggled<=fixed_black|fixed_white
    origins={(x-dx,y-dy) for x,y in toggled for dx in range(3) for dy in range(3)}
    nearby={(x+dx,y+dy) for x,y in origins for dx in range(3) for dy in range(3)}
    outside=set(map(tuple,outside))
    assert outside<=nearby-(fixed_black|fixed_white)
    before=fixed_black|outside;after=before^toggled
    row=Counter()
    for x,y in origins:
        for field,sign in ((before,-1),(after,1)):
            pattern=0
            for dy in range(3):
                for dx in range(3):
                    if (x+dx,y+dy) in field:pattern|=1<<(dx+3*dy)
            c=canonical_sector((x+y)&1,pattern) if sector else canonical(pattern)
            if c:row[c]+=sign
    return {c:v for c,v in row.items() if v}

def main():
    cert_path=HERE/'fold_farkas_certificate.json'
    context_path=ROOT/'factor_language/conditioned_macro_contexts.json'
    cuts_path=ROOT/'global_structure/conditioned_rank_cuts.json.gz'
    certificate=json.loads(cert_path.read_text())
    data=json.loads(context_path.read_text())
    records=json.loads(gzip.decompress(cuts_path.read_bytes()))
    assert hashlib.sha256(context_path.read_bytes()).hexdigest()==certificate['source_sha256']['contexts']
    assert hashlib.sha256(cuts_path.read_bytes()).hexdigest()==certificate['source_sha256']['compressed_cuts']
    energy=Counter();potential=Counter();macro_cost=Counter();cost=0;mass=0;seen=set()
    for term in certificate['terms']:
        lam=term['lambda_integer']
        assert type(lam) is int and lam>0
        rid=term['cut_index'];assert rid not in seen;seen.add(rid)
        record=records[rid]
        assert record['edge']==term['edge'] and record['outside_black']==term['outside_black']
        edge=data['edges'][term['edge']]
        for k in ('source','target','context','macro'):assert edge[k]==term[k]
        row=coefficients(data['contexts'][edge['context']],term['outside_black'])
        assert row=={int(k):v for k,v in term['energy_coefficients'].items()}
        for k,v in row.items():energy[k]+=lam*v
        potential[edge['target']]+=lam;potential[edge['source']]-=lam
        cost+=lam*int(edge['macro'] in 'CQB');mass+=lam
        macro_cost[edge['macro']]+=lam
    assert not any(potential.values())
    assert all(v>=0 for v in energy.values())
    assert cost>0
    assert cost==certificate['total_fold_cost'] and mass==certificate['multiplier_sum']
    assert {k:v for k,v in energy.items() if v}=={int(k):v for k,v in certificate['nonzero_aggregate_energy_coefficients'].items()}
    result={'status':'PASS: exact integer Farkas inequalities independently verified',
            'supported_cuts':len(seen),'nonzero_aggregate_energy_terms':sum(v>0 for v in energy.values()),
            'potential_balance_zero':True,'all_energy_coefficients_nonnegative':True,
            'strictly_positive_fold_cost':cost,
            'strictly_positive_J_cost':macro_cost['V']+macro_cost['Q'],
            'weighted_cost_by_macro':dict(macro_cost),
            'all_five_macro_weights_positive':all(macro_cost[c]>0 for c in 'UVBCQ'),
            'largest_multiplier_digits':max(len(str(t['lambda_integer'])) for t in certificate['terms']),
            'certificate_sha256':hashlib.sha256(cert_path.read_bytes()).hexdigest()}
    (HERE/'fold_farkas_verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
