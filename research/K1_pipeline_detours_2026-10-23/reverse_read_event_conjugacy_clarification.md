# Exact reverse read-event convention

23 October 2026. Clarification for the signed reverse plateau notes b48f7a9d and ab9fad0a; their scopes and conclusions are unchanged.

At a forward read q, let v be its cell, I its incoming heading and O its outgoing heading after the forward turn. The matching reverse read is at v on the POSTFLIP board, with incoming heading -O. It reads the opposite color, turns oppositely, restores the forward preflip color and departs with heading -I to the previous forward read cell. Thus R becomes reverse L and L becomes reverse R. This is the shifted read-event conjugacy, not an instruction to reverse the unshifted incoming heading at the forward poststep head.

Applying this at q,q-1,... gives the literal reversed orbit. Over the actual full period its drift is -d. Its checker sectors swap: reverse C is original L and reverse L is original C. With h_rev=-h one has H_rev=1-H_original on every face. Original even complete cells end white and reverse-start R; original odd cells end black and reverse-start L. The reverse black-input class count is exactly N_odd.

No global reverse WHITE assumption, positivity upgrade, new ancestry conclusion or original-fuel count is introduced by this convention.
