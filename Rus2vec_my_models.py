import gensim
from gensim.models import Word2Vec
from webapp.modul_vord2vec.normalization_words import normalization_word
import time

PATH_FOR_MODEL_bin = 'd:/My_sinonimaizer/Rus2Vec_models/220/model.bin'
PATH_FOR_MODEL_model = 'd:/My_sinonimaizer/Rus2Vec_models/.../model.model'


def get_sinonim_for_word():
    word_for_normalize = input().split()
    words = []

    try:
        if word_for_normalize[0].isalpha() and len(word_for_normalize) == 1:
            words = normalization_word(word_for_normalize)
    except (ValueError, TypeError):
        print('ошибочка')

    # model = gensim.models.KeyedVectors.load(PATH_FOR_MODEL_model)
    model = gensim.models.KeyedVectors.load_word2vec_format(PATH_FOR_MODEL_bin, binary=True)
    # print(len(word_for_normalize))

    # words = normalization_word(word_for_normalize)

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


def get_sinonims_for_text():
    # # model = gensim.models.KeyedVectors.load('d:/My_sinonimaizer/Rus2Vec_models/214/model.model')
    # model = gensim.models.KeyedVectors.load_word2vec_format(PATH_FOR_MODEL_bin, binary=True)
    # word_for_normalize = input().split()
    # print(len(word_for_normalize))
    # try:
    #     if len(word_for_normalize) == 1 and word_for_normalize[0].isalpha():
    #         words = normalization_word(word_for_normalize)
    # except:
    #     raise ValueError('Введите одно слово')
    #
    # # Попросим у модели 10 ближайших соседей для каждого слова и коэффициент косинусной близости для каждого:
    # for word in words:
    #     # есть ли слово в модели? Может быть, и нет
    #     if word in model:
    #         print(f'Слово: {word}')
    #         # выдаем 10 ближайших соседей слова:
    #         for i in model.most_similar(positive=[word], topn=15):
    #             # слово  # + коэффициент косинусной близости
    #             print(i[0])  # , i[1])
    #         print('\n')
    #     else:
    #         # Увы!
    #         print(f'Слово {word} отсутствет в словаре')
    pass


if __name__ == '__main__':
    start = time.time()
    get_sinonim_for_word()
    print(f'работало {time.time() - start} секунд')
