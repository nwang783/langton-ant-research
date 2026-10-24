"""Phase-independent M11 first-return parses of the two retained waves.

Only frozen literal words are parsed. No prepared black class, XOR cap,
continuation, finite episode, or physical U ancestry is manufactured.
"""
from pathlib import Path
from collections import Counter
import importlib.util
import hashlib
import json

R = Path('/workspace/shared/langton')
H = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location('ownership', R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py')
owner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(owner)
WORDS = owner.WORDS
M = owner.MARKER
inverse = {w: a for a, w in WORDS.items()}
assert len(inverse) == 7

atoms = []
for a in 'DCVUFQB':
    w = WORDS[a]
    starts = [i for i in range(len(w) + 1) if (w + M)[i:i + len(M)] == M]
    assert starts == [0, len(w)]
    atoms.append(dict(atom=a, RAW_length=len(w), RAW_word=w,
                      exact_M11_positions_in_RAW_plus_actual_next_M11=starts))

sources = [
    ('P1564', 'nonlinear_global_budget_2026-10-23/prepared_travelling_wave_certificate.json',
     'nonlinear_global_budget_2026-10-23/prepared_wave_five_band_normal_form.json'),
    ('Q4352', 'nonlinear_global_budget_2026-10-23/second_prepared_wave_certificate.json',
     'nonlinear_global_budget_2026-10-23/three_standard_band_wave_normal_form.json')]
reports = []
for name, source, background in sources:
    src = R / source
    cert = json.loads(src.read_text())
    w = cert['word']
    n = len(w)
    assert n == (1564 if name == 'P1564' else 4352)
    periodic = w * 3
    starts = [i for i in range(n) if periodic[i:i + len(M)] == M]
    assert starts
    returns = []
    for j, i in enumerate(starts):
        end = starts[j + 1] if j + 1 < len(starts) else starts[0] + n
        word = periodic[i:end]
        following_context = periodic[i:end + len(M)]
        marker_positions = [k for k in range(len(word) + 1)
                            if following_context[k:k + len(M)] == M]
        assert marker_positions == [0, len(word)]
        returns.append(dict(canonical_period_tick0=i, unwrapped_end_tick0=end,
                            RAW_length=len(word), literal_word=word,
                            word_sha256=hashlib.sha256(word.encode()).hexdigest(),
                            seven_atom=inverse.get(word),
                            first_return_marker_positions=marker_positions,
                            wraps_canonical_period_boundary=end > n))
    assert sum(r['RAW_length'] for r in returns) == n
    counts = Counter(r['seven_atom'] or 'OUTSIDE_SEVEN' for r in returns)
    if name == 'P1564':
        assert len(starts) == 21 and counts == {'C': 7, 'OUTSIDE_SEVEN': 14}
        assert starts[0] == 15
    else:
        assert len(starts) == 45 and counts == {'C': 14, 'D': 3, 'OUTSIDE_SEVEN': 28}
        assert starts[0] == 92
    occurrences = []
    for packet in ('D', 'C', 'V', 'U', 'F', 'Q', 'B', 'UC', 'UCC'):
        raw = ''.join(WORDS[a] for a in packet)
        bare = [i for i in range(n) if periodic[i:i + len(raw)] == raw]
        complete = [i for i in range(n) if periodic[i:i + len(raw) + len(M)] == raw + M]
        occurrences.append(dict(packet=packet, exact_RAW_occurrence_ticks0=bare,
                                exact_RAW_plus_actual_M11_occurrence_ticks0=complete))
        if packet in ('V', 'U', 'F', 'Q', 'B', 'UC', 'UCC'):
            assert bare == complete == []
    unknown = [r for r in returns if r['seven_atom'] is None]
    assert unknown
    representative = next(r for r in unknown if not r['wraps_canonical_period_boundary'])
    assert representative['RAW_length'] > max(map(len, WORDS.values()))
    reports.append(dict(name=name, word_source=source,
        source_file_sha256=hashlib.sha256(src.read_bytes()).hexdigest(),
        word_sha256=hashlib.sha256(w.encode()).hexdigest(), period=n,
        cyclic_M11_start_ticks0=starts, all_exact_cyclic_first_returns=returns,
        first_return_counts=dict(counts),
        first_return_label_sequence=[r['seven_atom'] or f"OUTSIDE({r['RAW_length']})" for r in returns],
        number_of_distinct_outside_words=len({r['literal_word'] for r in unknown}),
        representative_nonwrapping_outside_return=representative,
        all_atom_and_U_family_RAW_and_complete_occurrences=occurrences,
        phase_independent_no_seven_atom_cover=True,
        no_genuine_U_family_complete_entry_inside_stationary_wave=True,
        retained_complete_prepared_background=dict(path=background,
            sha256=hashlib.sha256((R / background).read_bytes()).hexdigest(),
            used_for_this_pure_literal_parse=False,
            no_unread_classes_or_XOR_cap_deleted=True)))

paths = [R / 'word_stabilization/shifted1_llrlrrrrlll_fold_coalesced_port_quotient.json',
         R / 'seven_word_return_bridge_2026-10-23/manifest.json',
         R / 'audits/check_seven_word_D_return_bridge_independent.json',
         R / 'literal_ownership_conventions_2026-10-24/canonical_read_ownership.py']
paths += [R / s for _, s, b in sources] + [R / b for _, s, b in sources]
assert all(p.exists() for p in paths)
out = dict(status='AUTHOR_FROZEN_PHASE_INDEPENDENT_WAVE_SEVEN_ATOM_SCOPE_PENDING_REVIEW',
    scope='Exact cyclic M11 first-return words of retained1564/4352 waves. Neither lies in the D/C/V/U/F/Q/B language at any cyclic phase. No proxy, renewal, field reduction, physical first-contact or global attraction conclusion.',
    actual_common_marker=M, all7_indivisible_first_return_atoms=atoms,
    exact_wave_reports=reports,
    phase_independence_argument='Every seven-atom boundary has actual M11 and every such atom has no interior M11. Thus in any hypothetical cyclic or bi-infinite seven-atom tiling, ALL actual M11 occurrences would be boundaries and each consecutive M11 interval would be one of the seven exact RAW words. The frozen outside intervals contradict that at every phase and every period multiple.',
    bare_prefix_warning='D RAW10 is the common ten-symbol prefix of every M11 occurrence, so bare D matches are not complete D atoms. C RAW matches can also lack a next marker. RAW+actualM11 and exact first-return words are retained separately.',
    finite_episode_interpretation='The signed finite-seed N-wave families literally contain these nonwrapping outside return intervals. Their unbounded defects remain valid, but they are not seven-atom trajectory controls and have no U-family entry within the stationary wave body.',
    global_attraction_gap='Even terminating this restricted seven-atom language would still require a separate coverage/transition theorem for arbitrary ant trajectories. Neither the two prepared wave words nor this literal parser supplies it.',
    dependencies={str(p.relative_to(R)): hashlib.sha256(p.read_bytes()).hexdigest() for p in paths})
(H / 'wave_first_return_parse.json').write_text(json.dumps(out, indent=2) + '\n')
print('1564:21 returns = 7 C + 14 outside;4352:45 = 14 C + 3 D + 28 outside.')
print('No cyclic RAW V/U/F/Q/B or U-family occurrence; neither wave has any phase or period-multiple seven-atom cover.')
