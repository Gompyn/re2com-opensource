#!/bin/bash
CLASSPATH='lucene-analyzers-common.jar:lucene-demo.jar:lucene.jar:lucene-queryparser.jar:.'
mkdir standard-corpus
java -cp $CLASSPATH IndexBuilder ../data/standard/train/train.token.retrieval standard-corpus

mkdir challenge-corpus
java -cp $CLASSPATH IndexBuilder ../data/challenge/train/train.token.retrieval challenge-corpus
