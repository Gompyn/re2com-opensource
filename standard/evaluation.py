import nltk
from nltk.translate.bleu_score import SmoothingFunction
from utils import log

def nltk_sentence_bleu(hypothesis, reference, order=4):
    cc = SmoothingFunction()
    return nltk.translate.bleu([reference], hypothesis, smoothing_function=cc.method4)


def nltk_corpus_bleu(hypotheses, references, order=4):
    refs = []
    count = 0
    total_score = 0.0

    cc = SmoothingFunction()

    for hyp, ref in zip(hypotheses, references):
        hyp = hyp.split()
        ref = ref.split()

        refs.append([ref])
        if len(hyp) == 1:
            count += 1
            continue

        score = nltk.translate.bleu([ref], hyp, smoothing_function=cc.method4)
        total_score += score
        count += 1

    avg_score = total_score / count
    corpus_bleu = nltk.translate.bleu_score.corpus_bleu(refs, hypotheses)
    print('corpus_bleu: %.4f avg_score: %.4f' % (corpus_bleu, avg_score))
    return corpus_bleu, avg_score


from nltk.translate.bleu_score import corpus_bleu
"""
code adapted from https://github.com/mcmillco/funcom/blob/master/bleu.py
GPLv3
"""
def bleu_so_far(preds, refs):
    refs = [[ref.split()] for ref in refs]
    preds = [pred.split() for pred in preds]
    
    Ba = corpus_bleu(refs, preds)
    B1 = corpus_bleu(refs, preds, weights=(1,0,0,0))
    B2 = corpus_bleu(refs, preds, weights=(0,1,0,0))
    B3 = corpus_bleu(refs, preds, weights=(0,0,1,0))
    B4 = corpus_bleu(refs, preds, weights=(0,0,0,1))

    def r(B):
        return round(B * 100, 2)

    log(f'BLEU: {r(Ba)}\tB1: {r(B1)}\tB2: {r(B2)}\tB3: {r(B3)}\tB4: {r(B4)}')

    return Ba
