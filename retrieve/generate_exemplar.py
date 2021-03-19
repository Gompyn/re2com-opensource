#!/bin/env python3
import argparse
import os
from os import path

def proj_exemplar(exemplar: str, src, tgt: str):
	with open(exemplar) as indices, open(tgt, 'w') as tgt:
		for index in indices:
			index = index.strip()
			if index == '' or index == 'xxx':
				print('', file=tgt)
			else:
				index = int(index)
				print(src[index], file=tgt)

def main():
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--exemplars', type=str, help='path to directory of exemplars')
	parser.add_argument('--output', type=str, help='path to output directory')
	args = parser.parse_args()
	
	assert path.exists(path.join(args.exemplars, 'train.exemplar'))
	assert path.exists(path.join(args.output, 'train', 'train.token.nl'))

	nls = [line.strip() for line in open(path.join(args.output, 'train', 'train.token.nl'))]
	for exemplar, tgt in [(path.join(args.exemplars, from_+'.exemplar'), path.join(args.output, to_+'.token.exemplar')) for from_, to_ in [('train', 'train/train'), ('val', 'val/test'), ('test', 'test/test')]]:
		proj_exemplar(exemplar, nls, tgt)
	del nls

	codes = [line.strip() for line in open(path.join(args.output, 'train', 'train.token.code'))]
	for exemplar, tgt in [(path.join(args.exemplars, from_+'.exemplar'), path.join(args.output, to_+'.token.exemplar_code')) for from_, to_ in [('train', 'train/train'), ('val', 'val/test'), ('test', 'test/test')]]:
		proj_exemplar(exemplar, codes, tgt)
	del codes

if __name__ == '__main__':
	main()
