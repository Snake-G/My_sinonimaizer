import gensim
from gensim.models import Word2Vec
from modul_word2vec.normalization_words import normalization_word
import time
from webapp import config


def get_sinonim_for_word(word_from_html):
    word_for_normalize = word_from_html.split()
    word = []
    if word_for_normalize[0].isalpha():
        word = normalization_word(word_for_normalize[0])
    else:
        return 'Введенное слово должно содержать только буквы'
    # model = gensim.models.KeyedVectors.load(PATH_FOR_MODEL_MODEL)
    model = gensim.models.KeyedVectors.load_word2vec_format(config.PATH_FOR_MODEL_BIN, binary=True)
    word = ''.join(word)
    # Попросим у модели ххх ближайших соседей для каждого слова и коэффициент косинусной близости для каждого:
    # есть ли слово в модели? Может быть, и нет
    return_words = []
    if word in model:
        # выдаем сколько-то (topn=...) ближайших соседей слова:
        for i in model.most_similar(positive=[word], topn=15):
            # слово  # + коэффициент косинусной близости
            if i not in return_words:
                return_words.append(i[0].split('_')[0])
            else:
                continue
        return return_words
    else:
        # Увы!
        # return_words = f"Слово {word.split('_')[0]} отсутствет в словаре"
        return f"Слово {word.split('_')[0]} отсутствет в словаре"


def get_sinonims_for_text(text_from_html):
    # model = gensim.models.KeyedVectors.load('d:/My_sinonimaizer/Rus2Vec_models/214/model.model')
    model = gensim.models.KeyedVectors.load_word2vec_format(config.PATH_FOR_MODEL_BIN, binary=True)
    word_for_normalize = input().split()
    print(len(word_for_normalize))
    # try:
    #     if len(word_for_normalize) == 1 and word_for_normalize[0].isalpha():
    #         words = normalization_word(word_for_normalize)
    # except:
    #     raise ValueError('Введите одно слово')
    words = normalization_word(word_for_normalize)
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
    get_sinonim_for_word()
    print(f'работало {time.time() - start} секунд')
