# Actual-channel packing requires event-disjoint components

24 October 2026. Mandatory premise qualification for frozen e75edaf9,
cap_free_actual_channel_packing_and_voltage_cycles.md. No source is edited.

The finite physical channels in Section1 must be EVENT-DISJOINT literal
successor components, or an explicitly event-disjoint partition into
literal subchannels. They are not arbitrary distinct contiguous windows
of the same cursor trajectory: two such windows can share reads and
legitimately overlap. The whole-interval exclusion is asserted only for
channel occurrences known to share NO actual read event.

This premise is automatic in the intended application of Section2:
OPEN components of the known one-step successor graph partition the
known event CLASSES. Their chosen lifted full-drift occurrences have
disjoint actual event sets. Different components cannot share a class;
different translates of one component cannot share an event because
its event classes are distinct and d is nonzero. Closed components are
handled separately by Section4, not by ignoring aliasing.

With this event-disjointness premise, overlap at an integer time would
require two different read events by the one cursor. Hence one component
occurrence's genuine rank order before another forces their WHOLE time
blocks to have that order. The voltage signs and inequalities(3)-(5)
remain unchanged. No packing inference is authorized for overlapping
marked windows, lifetime paths, flow/repair paths, or phase calendars
whose alleged components have not been checked to partition events.
