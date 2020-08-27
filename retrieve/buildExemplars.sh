#!/bin/bash
mkdir standard-exemplars
./search.sh standard-corpus ../data/standard/train/train.token.code standard-exemplars/train.exemplar ../data/standard/val/test.token.code standard-exemplars/val.exemplar ../data/standard/test/test.token.code standard-exemplars/test.exemplar
python3 generate_exemplar.py --exemplars standard-exemplars --output ../data/standard

mkdir challenge-exemplars
./search.sh challenge-corpus ../data/challenge/train/train.token.code challenge-exemplars/train.exemplar ../data/challenge/val/test.token.code challenge-exemplars/val.exemplar ../data/challenge/test/test.token.code challenge-exemplars/test.exemplar
python3 generate_exemplar.py --exemplars challenge-exemplars --output ../data/challenge