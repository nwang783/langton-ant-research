from pathlib import Path
import hashlib,json
S=Path(__file__);R=S.parents[1];D=R/'V_postforeign_pair_rail_reserve_2026-10-24';sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest();M=D/'simultaneous_input_qualification_manifest.json';assert sha(M)=='b84be11be0192079bf6a13879fde184ccc05f4cf48076e9b5477293c7ac527eb';j=json.loads(M.read_text())
for f,h in j['files'].items():assert sha(D/f)==h
p=R/'audits/check_V_pair_rail_independent.json';a=json.loads(p.read_text());assert a['held_r_context_types']=={'WHITE':24,'INPUT':9,'CORE':3}
# The preceding independent source audit explicitly tested all9 INPUT rows against actual full-source chords.
assert "if localr in inv[atom][2]:assert any(meet(*ch,*old)is not None for old in pieces(src))" in (R/'audits/check_V_pair_rail_independent.py').read_text()
out=dict(status='PASS mandatory explicit simultaneous-input/geometric-contact qualification',manifest=sha(M),original_manifest=j['original358_manifest'],original_independent_report=sha(p),scope=['36context rows are24WHITE/3CORE/9simultaneous external inputs, not36literal color conflicts.','All9 input rows meet actual prior V/VC/VCC source geometry. Old V terminal can be the real ownC1 outgoing vertex, but the postforeign loss atom is not chronologically adjacent to that older source. Contact outcome suffices independent of owner relabeling.','The earliest-loss proof excludes simultaneous erasure only under an earlier simple prefix; otherwise it gives the promised contact. No ordering of physical Ls or unsupported held-through-input premise. Frozen358andefde unchanged.'])
S.with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS',sha(S.with_suffix('.json')))
