import gensim
from gensim.models import Word2Vec
from webapp.normalization_words import input_word
import time

# import logging
# import sys

def sin():
    # model = gensim.models.KeyedVectors.load('d:/My_sinonimaizer/Rus2Vec_models/214/model.model')
    model = gensim.models.KeyedVectors.load_word2vec_format('d:/My_sinonimaizer/Rus2Vec_models/220/model.bin', binary=True)
    words = input_word(input())

    # Попросим у модели 10 ближайших соседей для каждого слова и коэффициент косинусной близости для каждого:
    for word in words:
        # есть ли слово в модели? Может быть, и нет
        if word in model:
            print(f'Слово: {word}')
            # выдаем 10 ближайших соседей слова:
            for i in model.most_similar(positive=[word], topn=15):
                # слово  # + коэффициент косинусной близости
                print(i[0])  # , i[1])
            print('\n')
        else:
            # Увы!
            print(f'Слово {word} отсутствет в словаре')


if __name__ == '__main__':
    start = time.time()
    sin()
    print(f'работало {time.time() - start}')

