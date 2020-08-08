import argparse
from nltk.translate.bleu_score import corpus_bleu, sentence_bleu
from nltk.translate.bleu_score import SmoothingFunction

def my_sentence_bleu(preds, refs, verbose=False):
    refs = [refs.split()]
    preds = preds.split()
    cc = SmoothingFunction()
    Ba = sentence_bleu(refs, preds, smoothing_function=cc.method4)

    def r(B):
        return round(B * 100, 4)

    if verbose:
        B1 = corpus_bleu(refs, preds, weights=(1,0,0,0))
        B2 = corpus_bleu(refs, preds, weights=(0,1,0,0))
        B3 = corpus_bleu(refs, preds, weights=(0,0,1,0))
        B4 = corpus_bleu(refs, preds, weights=(0,0,0,1))
        print('BLEU: {}\tB1: {}\tB2: {}\tB3: {}\tB4: {}'.format(r(Ba), r(B1), r(B2), r(B3), r(B4)))

    return Ba

def my_corpus_bleu(preds, refs, verbose=False):
    refs = [[ref.strip().split()] for ref in refs]
    preds = [pred.strip().split() for pred in preds]
    Ba = corpus_bleu(refs, preds)

    def r(B):
        return round(B * 100, 4)

    if verbose:
        B1 = corpus_bleu(refs, preds, weights=(1,0,0,0))
        B2 = corpus_bleu(refs, preds, weights=(0,1,0,0))
        B3 = corpus_bleu(refs, preds, weights=(0,0,1,0))
        B4 = corpus_bleu(refs, preds, weights=(0,0,0,1))
        print('BLEU: {}\tB1: {}\tB2: {}\tB3: {}\tB4: {}'.format(r(Ba), r(B1), r(B2), r(B3), r(B4)))

    return Ba

def main():
	parser = argparse.ArgumentParser(formatter=argparse.ArgumentDefaultsHelpFormatter)
	parser.add_argument('--preds', type=str, help='file of predicates')
	parser.add_argument('--refs', type=str, help='file of references')
	args = parser.parse_args()

	my_corpus_bleu(open(args.preds), open(args.refs))
