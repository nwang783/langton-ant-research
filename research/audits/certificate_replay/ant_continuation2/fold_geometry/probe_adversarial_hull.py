"""Replay exact max-plus counterfields against the sharp fuel-hull conjecture.

This is a targeted falsification experiment, not a proof of a uniform bound.
Each input field is an actual after-marker state with a feasible149-letter
history.  We reverse the last marker, follow its deterministic physical future,
and retain only completed before-marker five-block prefixes.
"""
from pathlib import Path
import argparse
import json
import time

ROOT=Path(__file__).resolve().parents[2]
DATA=json.loads((ROOT/'ant_continuation/factor_language/five_macro_footprints.json').read_text())
DIRS=((0,1),(1,0),(0,-1),(-1,0))
M='LLLLRLRRRRLR'


def bbox_extend(b,x,y):
    return min(b[0],x),min(b[1],y),max(b[2],x),max(b[3],y)


def reverse_marker(black,pose):
    black=set(black);x,y,h=pose;letters=[]
    for _ in M:
        dx,dy=DIRS[h];x-=dx;y-=dy
        c='R' if (x,y) in black else 'L';letters.append(c)
        black.symmetric_difference_update({(x,y)})
        h=(h+(-1 if c=='R' else 1))%4
    assert ''.join(reversed(letters))==M
    return black,(x,y,h)


def direct_certificate(seq):
    black=set();last={};x=y=h=0;rb=(10**9,10**9,-10**9,-10**9);bb=rb
    for name in seq:
        for c in DATA[name]['word']:
            p=x,y;assert last.get(p)!=c
            if p not in last and c=='L':black.add(p);bb=bbox_extend(bb,x,y)
            last[p]=c;rb=bbox_extend(rb,x,y)
            h=(h+(1 if c=='R' else -1))%4;dx,dy=DIRS[h];x+=dx;y+=dy
    gaps=[bb[0]-rb[0],bb[1]-rb[1],rb[2]-bb[2],rb[3]-bb[3]]
    return {'macros':seq,'macro_count':len(seq),'steps':sum(DATA[k]['length'] for k in seq),
            'first_L_seed':sorted(black),'first_L_box':bb,'read_box':rb,'gaps':gaps,
            'maximum_gap':max(gaps),'end_pose':[x,y,h]}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',default=str(Path(__file__).with_name('maxplus_full_history_sft_refinement.json')))
    p.add_argument('--output',default=str(Path(__file__).with_name('adversarial_hull_replay.json')))
    p.add_argument('--max-blocks',type=int,default=1000)
    p.add_argument('--limit',type=int,default=0)
    args=p.parse_args()
    records=json.loads(Path(args.input).read_text())['counterexamples']
    trie={}
    for name,d in DATA.items():
        node=trie
        for c in d['word']:node=node.setdefault(c,{})
        assert not node;node['macro']=name
    started=time.time();bestgap=-1;best=None;maxblocks=0;tested=0;steps=0;seen=set();violations=[]
    for ri,record in enumerate(records):
        # Horizontal/vertical translations are immaterial.  Normalize each
        # after-marker field to its current head to deduplicate repeats.
        y0=record['start_y'];h=record['heading']
        field=frozenset((x,y-y0) for x,y in record['initial_black'])
        key=(field,h)
        if key in seen:continue
        seen.add(key)
        black,(x,y,h)=reverse_marker(field,(0,0,h))
        rb=(10**9,10**9,-10**9,-10**9);bb=rb;visited=set();seq=[];node=trie
        tested+=1
        for _ in range(args.max_blocks*74):
            c='L' if (x,y) in black else 'R'
            if c not in node:break
            node=node[c];steps+=1
            if (x,y) not in visited:
                visited.add((x,y))
                if c=='L':bb=bbox_extend(bb,x,y)
            rb=bbox_extend(rb,x,y)
            black.symmetric_difference_update({(x,y)})
            h=(h+(1 if c=='R' else -1))%4;dx,dy=DIRS[h];x+=dx;y+=dy
            if 'macro' in node:
                seq.append(node['macro']);node=trie
                gaps=[bb[0]-rb[0],bb[1]-rb[1],rb[2]-bb[2],rb[3]-bb[3]]
                gap=max(gaps)
                if gap>bestgap:
                    bestgap=gap;best=direct_certificate(''.join(seq));best['source_record']=ri
                    print({'tested':tested,'new_maximum_gap':gap,'word':best['macros']},flush=True)
                if gap>4:
                    cert=direct_certificate(''.join(seq));assert cert['maximum_gap']>4
                    cert['source_record']=ri;violations.append(cert);break
                if len(seq)>=args.max_blocks:break
        maxblocks=max(maxblocks,len(seq))
        if violations:break
        if args.limit and tested>=args.limit:break
        if tested%2000==0:print({'tested':tested,'maximum_gap':bestgap,'maximum_blocks':maxblocks},flush=True)
    out={'status':'Counterexample found' if violations else 'No counterexample in targeted finite replay; not a proof',
         'input':args.input,'input_records':len(records),'distinct_fields_replayed':tested,
         'literal_steps':steps,'maximum_completed_macros':maxblocks,'maximum_gap':bestgap,
         'best':best,'violations':violations,'elapsed_seconds':time.time()-started}
    Path(args.output).write_text(json.dumps(out,indent=2)+'\n')
    print({k:v for k,v in out.items() if k not in ('best','violations')},flush=True)


if __name__=='__main__':main()
