"""Evaluate the EXISTING ordinary witness on sector-dependent columns.

This is a reuse check, not a new dual search. A negative aggregate means
the ordinary certificate does not certify the sector ansatz.
"""
from pathlib import Path
import json
from collections import Counter
from verify_fold_farkas import coefficients,canonical_sector

HERE=Path(__file__).resolve().parent
def main():
    cert=json.loads((HERE/'fold_farkas_certificate.json').read_text())
    data=json.loads((HERE.parent/'factor_language/conditioned_macro_contexts.json').read_text())
    aggregate=Counter()
    for t in cert['terms']:
        row=coefficients(data['contexts'][t['context']],t['outside_black'],sector=True)
        for k,v in row.items():aggregate[k]+=t['lambda_integer']*v
    classes={canonical_sector(s,p) for s in (0,1) for p in range(512)}-{0}
    negative={str(k):v for k,v in sorted(aggregate.items()) if v<0}
    out={'status':'PASS sector extension' if not negative else 'FAIL: ordinary witness has negative sector columns',
         'sector_column_count':len(classes),'negative_column_count':len(negative),
         'positive_column_count':sum(v>0 for v in aggregate.values()),
         'negative_coefficients':negative,
         'all_aggregate_coefficients':{str(k):v for k,v in sorted(aggregate.items()) if v}}
    (HERE/'fold_farkas_sector_reuse_check.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps({k:v for k,v in out.items() if k not in ('negative_coefficients','all_aggregate_coefficients')},indent=2))

if __name__=='__main__':main()
