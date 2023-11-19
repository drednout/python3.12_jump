#!/bin/bash
rm perf.data
perf record -F 9999 -g -o perf.data /home/dr/devel/cpython/local_install/bin/python3  -X perf $1
perf script |  FlameGraph/stackcollapse-perf.pl > out.perf-folded
FlameGraph/flamegraph.pl out.perf-folded > perf.svg
