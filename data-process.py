#!/bin/env python3
import os
import argparse
import utils

def main():
	parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--icse-dir', type=str, default='funcom', help='path to data from ast-attend-gru')
	parser.add_argument('--data', type=str, default='data', help='path to data directory')
	parser.add_argument('--ast-vocab-size', type=int, default=10000, help='vocabulary size of ast')
	parser.add_argument('--code-vocab-size', type=int, default=50000, help='vocabulary size of code')
	parser.add_argument('--nl-vocab-size', type=int, default=50000, help='vocabulary size of comment')
	args = parser.parse_args()

	icse_dir = os.path.join(args.icse_dir, 'data', 'standard', 'output')
	standard = os.path.join(args.data, 'standard')
	challenge = os.path.join(args.data, 'challenge')
	assert os.path.isdir(args.icse_dir)
	assert os.path.isfile(os.path.join(icse_dir, 'smls.test'))

	dir2file = {'train': 'train', 'val': 'test', 'test': 'test'}
	ext_conv = {'smls': 'ast', 'dats': 'code', 'coms': 'nl'}
	def old_path(ori_ext, dir_name):
		return os.path.join(icse_dir, '.'.join([ori_ext, dir_name]))
	def new_dir(dir_name, root=standard):
		return os.path.join(root, dir_name, '.'.join([dir2file[dir_name], 'token']))
	def new_path(new_ext, dir_name, root=standard):
		return '.'.join([new_dir(dir_name, root=root), new_ext])
	def get_vocab(ext, root=standard):
		return os.path.join(root, 'vocab.'+ext)
	def symlink(to, name):
		os.symlink(os.path.abspath(to), name)

	# standard
	# rename
	for dir_name in dir2file:
		os.makedirs(os.path.join(standard, dir_name), exist_ok=True)
		for ori_ext, new_ext in ext_conv.items():
			os.rename(old_path(ori_ext, dir_name), new_path(new_ext, dir_name))
	# align
	def build_write_aligned(dir_name):
		stem = new_dir(dir_name) + '.'
		postfix = list(ext_conv.values())
		sentences = list(utils.build_words(stem, postfix).values())
		for sentence3 in sentences:
			sentence3['nl'] = utils.remove_bos_eos(sentence3['nl'])
		utils.write_into(sentences, stem, postfix)
		return sentences
	for dir_name in dir2file.keys() - {'train'}:
		build_write_aligned(dir_name)
	train_corpus = build_write_aligned('train')
	# build vocabulary
	for ext in ext_conv.values():
		def yielder():
			for line3 in train_corpus:
				yield line3[ext]
		vocab = utils.build_vocab(yielder)
		vocab = [('<s>', 0), ('</s>', 0), ('<unk', 0), ('<pad>', 0)] + vocab
		with open(get_vocab(ext), 'w') as f:
			for word, _ in vocab[:getattr(args, ext+'_vocab_size')]:
				print(word, file=f)
	symlink(get_vocab('nl'), get_vocab('exemplar'))
	symlink(get_vocab('code'), get_vocab('exemplar_code'))

	# challenge
	ext_conv2 = {'ast': 'code', 'nl': 'nl'}
	for dir_name in dir2file:
		os.makedirs(os.path.join(challenge, dir_name), exist_ok=True)
		for old_ext, new_ext in ext_conv2.items():
			symlink(new_path(old_ext, dir_name, root=standard),
			           new_path(new_ext, dir_name, root=challenge))
	for old_ext, new_ext in ext_conv2.items():
		symlink(get_vocab(old_ext, root=standard),
		           get_vocab(new_ext, root=challenge))
	symlink(get_vocab('nl', root=challenge), get_vocab('exemplar', root=challenge))
	symlink(get_vocab('code', root=challenge), get_vocab('exemplar_code', root=challenge))

if __name__ == '__main__':
	main()
