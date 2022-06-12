import gensim
from gensim.models import Word2Vec
from webapp.modul_vord2vec.normalization_words import normalization_word
import time


PATH_FOR_MODEL_bin = 'd:/My_sinonimaizer/Rus2Vec_models/220/model.bin'
PATH_FOR_MODEL_model = 'd:/My_sinonimaizer/Rus2Vec_models/.../model.model'

def get_sinonims():
    # model = gensim.models.KeyedVectors.load('d:/My_sinonimaizer/Rus2Vec_models/214/model.model')
    model = gensim.models.KeyedVectors.load_word2vec_format(PATH_FOR_MODEL_bin, binary=True)
    words = normalization_word(input())

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
    get_sinonims()
    print(f'работало {time.time() - start} секунд')
