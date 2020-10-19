def build_words(stem: str, prefix: list):
	d = dict()
	for p in prefix:
		def add_word(no, word):
			if no not in d:
				d[no] = dict()
			d[no][p] = word
		for line in open(stem+p):
			no, word = line.strip().split(maxsplit=1)
			add_word(no, word)
	return d

def write_into(l: list, stem: str, prefix: list):
	for p in prefix:
		with open(stem+p, 'w') as f:
			for terms in l:
				print(terms[p], file=f)

def build_with_other(indices: str, content: str):
	d = dict()
	for l, c in zip(open(indices), open(content)):
		d[l.strip().split(maxsplit=1)[0]] = c.strip()
	return d

def remove_bos_eos(s: str):
	return ' '.join(s.strip().split()[1:-1])

def build_vocab(f):
	d = dict()
	def add_word(word):
		if word not in d:
			d[word] = 1
		else:
			d[word] += 1
	for line in f():
		for word in line.strip().split():
			add_word(word)
	d = list(d.items())
	d = sorted(d, key=lambda x: x[1], reverse=True)
	return d

def build_corpus(stem: str, prefix: list):
	d = dict()
	for p in prefix:
		def add_word(no, word):
			if no not in d:
				d[no] = dict()
			d[no][p] = word
		for no, line in enumerate(open(stem+p)):
			word = line.strip()
			add_word(no, word)
	return d

def remove_word(l: list, words: set):
	for line in l:
		t = line.split()
		for word in t:
			if word in words:
				t.remove(word)
		line = ' '.join(t)
	return l
