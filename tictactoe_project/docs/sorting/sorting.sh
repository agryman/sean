#!/usr/bin/env bash
cd $(dirname $0)
pwd
cat ../shared/fuzzlib\
 sorting.sty > sorting.prelude
fuzz -p sorting.prelude sorting