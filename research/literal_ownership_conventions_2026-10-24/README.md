# Canonical literal read ownership

Ticks are always explicitly zero-based; human read numbers are explicitly one-based. Generate ownership labels with `describe(packet, context_tick0)`. Do not manually write a bare phase number.

A packet of RAW length L owns ticks 0 through L-1. Context tick L is the first read of the next actual word. Marker-only residual absorption is not a physical read and need not coincide with it. An actual following word supplies M11; no extra marker is executed.

| Packet | Input | Context tick0 | RAW length | Physical owner | Owner tick0 | Owner read1 |
|---|---|---:|---:|---|---:|---:|
| D | (0, 1) | 11 | 10 | next actual word RAW | 1 | 2 |
| DC | (0, 1) | 11 | 25 | own C-tail 1 RAW | 1 | 2 |
| V | (0, 3) | 19 | 18 | next actual word RAW | 1 | 2 |
| V | (1, 2) | 13 | 18 | own V-base RAW | 13 | 14 |
| VC | (0, 3) | 19 | 33 | own C-tail 1 RAW | 1 | 2 |
| VC | (1, 2) | 13 | 33 | own V-base RAW | 13 | 14 |
| VCC | (0, 3) | 19 | 48 | own C-tail 1 RAW | 1 | 2 |
| VCC | (1, 2) | 13 | 48 | own V-base RAW | 13 | 14 |
| U | (-1, 1) | 14 | 28 | own U-base RAW | 14 | 15 |
| U | (-1, 2) | 13 | 28 | own U-base RAW | 13 | 14 |
| U | (-1, 4) | 29 | 28 | next actual word RAW | 1 | 2 |
| U | (0, 2) | 12 | 28 | own U-base RAW | 12 | 13 |
| U | (0, 3) | 23 | 28 | own U-base RAW | 23 | 24 |
| UC | (-1, 1) | 14 | 43 | own U-base RAW | 14 | 15 |
| UC | (-1, 2) | 13 | 43 | own U-base RAW | 13 | 14 |
| UC | (-1, 4) | 29 | 43 | own C-tail 1 RAW | 1 | 2 |
| UC | (0, 2) | 12 | 43 | own U-base RAW | 12 | 13 |
| UC | (0, 3) | 23 | 43 | own U-base RAW | 23 | 24 |
| UCC | (-1, 1) | 14 | 58 | own U-base RAW | 14 | 15 |
| UCC | (-1, 2) | 13 | 58 | own U-base RAW | 13 | 14 |
| UCC | (-1, 4) | 29 | 58 | own C-tail 1 RAW | 1 | 2 |
| UCC | (0, 2) | 12 | 58 | own U-base RAW | 12 | 13 |
| UCC | (0, 3) | 23 | 58 | own U-base RAW | 23 | 24 |

Common traps: D input(0,1), U input(-1,4), and V input(0,3) are at context ticks11,29,19 respectively. Their raw lengths10,28,18 make all three the SECOND read of the next word. DC/UC/VC own the corresponding read inside their first C tail, still tick1/read2.

No frozen theorem source is changed by this generated table. Mandatory errata remain separate; this utility does not decide lifetime clocks, original source roles, or whether a claimed parser continuation is actual.
