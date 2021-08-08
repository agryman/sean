#!/usr/bin/env bash
cd $(dirname $0)
pwd
cat ../shared/fuzzlib\
 minimax.sty > minimax.prelude
fuzz -p minimax.prelude minimax