#!/bin/bash
./search.sh standard-corpus ../data/standard/train/train.token.code standard/train.exemplar ../data/standard/val/test.token.code standard/val.exemplar ../data/standard/test/test.token.code standard/test.exemplar

./search.sh challenge-corpus ../data/challenge/train/train.token.code challenge/train.exemplar ../data/challenge/val/test.token.code challenge/val.exemplar ../data/challenge/test/test.token.code challenge/test.exemplar
