"""Canonical zero-based literal ownership, with separate human read numbers.
Use describe(packet, context_tick0) to generate labels; never write naked 'phase1'.
For a marker-owned read the next actual word must provide the actual M11 prefix.
This module attributes physical reads only, not earlier residual/core absorption.
"""
from pathlib import Path
import json, hashlib
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json'
J=json.loads(SOURCE.read_text());WORDS={a:r['word']for a,r in zip('DCVUFQB',J['macro_words'])};MARKER='LLLLRLRRRRL'
PACKETS=('D','DC','V','VC','VCC','U','UC','UCC');K={-1-1j,-1,-1j,0,1};DIR=(1j,1,-1j,-1)
def describe(packet, context_tick0):
 if not isinstance(context_tick0,int) or context_tick0<0:raise ValueError('context_tick0 must be a nonnegative integer')
 raw=''.join(WORDS[a]for a in packet)
 if context_tick0>=len(raw)+len(MARKER):raise ValueError('tick is outside supplied RAW+M11 context')
 result={'packet':packet,'context_tick0':context_tick0,'context_read_number1':context_tick0+1,'RAW_length':len(raw)}
 if context_tick0>=len(raw):
  t=context_tick0-len(raw);result.update(owner='next actual word RAW',owner_tick0=t,owner_read_number1=t+1,turn=MARKER[t],next_word_tick0=t,next_word_read_number1=t+1)
 else:
  offset=0;cnumber=0
  for a in packet:
   if a=='C':cnumber+=1
   if context_tick0<offset+len(WORDS[a]):
    t=context_tick0-offset;owner=f'own C-tail {cnumber} RAW'if a=='C'else f'own {a}-base RAW'
    result.update(owner=owner,owner_tick0=t,owner_read_number1=t+1,turn=WORDS[a][t],next_word_tick0=None,next_word_read_number1=None);break
   offset+=len(WORDS[a])
 result['label']=f"context tick {context_tick0} (zero-based), RAW length {len(raw)}; {result['owner']} tick {result['owner_tick0']} (zero-based), read {result['owner_read_number1']} (one-based), {result['turn']}"
 return result

def input_rows():
 rows=[]
 chosen=dict(zip(PACKETS,(1j,1j,1+2j,1+2j,3j,-1+4j,-1+4j,-1+4j)))
 for packet in PACKETS:
  word=''.join(WORDS[a]for a in packet)+MARKER;p=0j;h=0;par=set();req={};first={}
  for t,ch in enumerate(word):
   b=(ch=='L')^(p in par)
   assert p not in req or req[p]==b
   req[p]=b;first.setdefault(p,t);par.symmetric_difference_update({p});h=(h+(1 if ch=='R'else -1))%4;p+=DIR[h]
  inputs={p for p,b in req.items()if b}-K
  for p in sorted(inputs,key=lambda p:(p.real,p.imag)):
   r=describe(packet,first[p]);assert r['turn']=='L';r.update(input_cell=[int(p.real),int(p.imag)],ordered_W_choice=p==chosen[packet]);rows.append(r)
 return rows
if __name__=='__main__':
 rows=input_rows();assert len(rows)==23
 examples=[describe('D',11),describe('U',29),describe('V',19),describe('DC',11),describe('UC',29),describe('VC',19)]
 for e in examples:assert e['owner_tick0']==1 and e['owner_read_number1']==2
 out={'status':'CANONICAL_LITERAL_READ_OWNERSHIP','source_sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),'conventions':['Every tick/offset with suffix0 is zero-based. Every read number with suffix1 is one-based.','RAW length L means ticks0 through L-1 are owned RAW; context tick L is next actual word tick0/read1.','A marker is a verified prefix of the following actual word, not an extra executed word. Full-context ledger/core absorption can precede the physical read.','Atomic source births such as R8 mean zero-based literal tick8/read9 unless explicitly stated otherwise. Bare phase labels must not be used.'],'all23_full_packet_input_first_reads':rows,'critical_examples':examples}
 Path(__file__).with_name('ownership_table.json').write_text(json.dumps(out,indent=2)+'\n')
 lines=['# Canonical literal read ownership','', 'Ticks are always explicitly zero-based; human read numbers are explicitly one-based. Generate ownership labels with `describe(packet, context_tick0)`. Do not manually write a bare phase number.','', 'A packet of RAW length L owns ticks 0 through L-1. Context tick L is the first read of the next actual word. Marker-only residual absorption is not a physical read and need not coincide with it. An actual following word supplies M11; no extra marker is executed.','', '| Packet | Input | Context tick0 | RAW length | Physical owner | Owner tick0 | Owner read1 |','|---|---|---:|---:|---|---:|---:|']
 for r in rows:lines.append(f"| {r['packet']} | {tuple(r['input_cell'])} | {r['context_tick0']} | {r['RAW_length']} | {r['owner']} | {r['owner_tick0']} | {r['owner_read_number1']} |")
 lines+=['','Common traps: D input(0,1), U input(-1,4), and V input(0,3) are at context ticks11,29,19 respectively. Their raw lengths10,28,18 make all three the SECOND read of the next word. DC/UC/VC own the corresponding read inside their first C tail, still tick1/read2.','', 'No frozen theorem source is changed by this generated table. Mandatory errata remain separate; this utility does not decide lifetime clocks, original source roles, or whether a claimed parser continuation is actual.','']
 Path(__file__).with_name('README.md').write_text('\n'.join(lines));print('23 input ownership rows; all critical examples are tick1/read2.')
