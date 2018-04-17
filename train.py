
#!/usr/bin/env python
# ‐*‐ coding: utf‐8 ‐*‐
# train_word2vec_model.py 用于训练模型
import logging
import os.path
import sys
import multiprocessing
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
import gensim
#model = gensim.models.KeyedVectors.load_word2vec_format('***.bin',binary=True)
#model = gensim.models.Word2Vec.load('.model')
#model = gensim.models.KeyedVectors.load('**.model')
Word2Vec.load_word2vec_format()
if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logging.root.setLevel(level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))
    # check and process input arguments
    if len(sys.argv) < 4:
        print( globals()['__doc__'] % locals())
        sys.exit(1)
    inp, outp1, outp2 = sys.argv[1:4]
    #inp为分词后的文件
    model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())
    # trim unneeded model memory = use(much) less RAM
    #model.init_sims(replace=True)
    model.save(outp1)
    model.save_word2vec_format(outp2, binary=False)
