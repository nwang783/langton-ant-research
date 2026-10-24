"""Exact one/two-successor extension test for fixed violating upper strips.

All choices follow the actual995-port graph.  Unspecified initial cells below
the strip can be assigned either color on first read.  Hence failure is exact
for that fixed upper strip, while success gives a literal finite extension.
"""
from pathlib import Path
from collections import defaultdict
import argparse
import json
import time

from verify_maxplus_sft import ROOT,context_data,rot,value,DIRS


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--input',default=str(Path(__file__).with_name('maxplus_last_port_candidate.json')))
    p.add_argument('--limit',type=int,default=0)
    args=p.parse_args()
    raw=json.loads(Path(args.input).read_text());w=raw['weights'];records=raw['counterexamples']
    graph=json.loads(Path(__file__).with_name('full_history_macro_contexts.json').read_text())
    data=context_data(Path(__file__).with_name('full_history_macro_contexts.json'),True)
    adj=defaultdict(list)
    for i,e in enumerate(graph['edges']):adj[e['source']].append(i)
    lo=-max(w[1:512]);stats={'tested':0,'no_one_successor':0,'one_but_no_two':0,'two_successors':0,
                           'attempted_macro_extensions':0};examples={};started=time.time()
    for ri,r in enumerate(records):
        name=r['macro'];d=data[name];eid=int(name.split('_')[1]);e=graph['edges'][eid]
        h0=r['heading'];y0=r['start_y'];original=set(map(tuple,r['initial_black']))
        known={}
        for key,bit in (('first_L',1),('first_R',0)):
            for p in d[key]:
                x,y=rot(p,h0);known[x,y+y0]=bit
        assert all(((p in original)==bool(b)) for p,b in known.items())
        assigned={}
        def apply(word,pose):
            x,y,h=pose;changes=[];new=[]
            for c in word:
                p=x,y;required=int(c=='L');old=known.get(p)
                initial=(int(p in original) if y>=lo else None)
                actual=old if old is not None else initial
                if actual is not None and actual!=required:
                    undo(changes,new);return None
                changes.append((p,old));known[p]=1-required
                if actual is None:assigned[p]=required;new.append(p)
                h=(h+(1 if c=='R' else -1))%4;dx,dy=DIRS[h];x+=dx;y+=dy
            return (x,y,h),changes,new
        def undo(changes,new):
            for p,old in reversed(changes):
                if old is None:del known[p]
                else:known[p]=old
            for p in new:del assigned[p]
        first=apply(d['word'],(0,y0,h0));assert first is not None
        pose,_,_=first;one=False;two=False;success=None
        for e1 in adj[e['target']]:
            stats['attempted_macro_extensions']+=1
            a=apply(data['edge_'+str(e1)]['word'],pose)
            if a is None:continue
            one=True;q,ch,new=a
            for e2 in adj[graph['edges'][e1]['target']]:
                stats['attempted_macro_extensions']+=1
                b=apply(data['edge_'+str(e2)]['word'],q)
                if b is None:continue
                two=True
                success=(e1,e2,set(p for p,v in assigned.items() if v))
                undo(b[1],b[2]);break
            undo(ch,new)
            if two:break
        stats['tested']+=1
        kind='two_successors' if two else ('one_but_no_two' if one else 'no_one_successor')
        stats[kind]+=1
        if kind not in examples:
            example={'source_record':ri,'first_edge':eid,'heading':h0,'start_y':y0,'strip_low_row':lo}
            if two:
                e1,e2,extra=success;initial=original|extra
                assert all(y<lo for x,y in extra-original)
                allwords=[d['word'],data['edge_'+str(e1)]['word'],data['edge_'+str(e2)]['word']]
                actual=set(initial);x=0;y=y0;h=h0;pre=value(actual,(x,y,h),w,e['source']);post=None
                for j,word in enumerate(allwords):
                    for c in word:
                        assert ((x,y) in actual)==(c=='L')
                        actual.symmetric_difference_update({(x,y)})
                        h=(h+(1 if c=='R' else -1))%4;dx,dy=DIRS[h];x+=dx;y+=dy
                    if j==0:post=value(actual,(x,y,h),w,e['target'])
                assert pre<=0<post
                example.update({'edge_path':[eid,e1,e2],'macro_types':[graph['edges'][k]['macro'] for k in (eid,e1,e2)],
                                'added_initial_black':sorted(extra-original),'initial_black':sorted(initial),
                                'pre_value':pre,'after_first_value':post,'end_pose':[x,y,h]})
            examples[kind]=example
        if stats['tested']%5000==0:print(stats,flush=True)
        if args.limit and stats['tested']>=args.limit:break
    out={'status':'Exact fixed-upper-strip extension classification; no universal future-conditioned invariant claimed',
         'statistics':stats,'examples':examples,'input':args.input,'elapsed_seconds':time.time()-started}
    Path(__file__).with_name('counterfield_lookahead_verification.json').write_text(json.dumps(out,indent=2)+'\n')
    print(out,flush=True)


if __name__=='__main__':main()
