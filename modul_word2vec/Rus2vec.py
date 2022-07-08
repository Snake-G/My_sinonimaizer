import gensim
from gensim.models import Word2Vec
from modul_word2vec.normalization_words import normalization_word, normalization_text
# import time
from webapp import config


def get_synonym_for_word(word_from_html):
    word_for_normalize = word_from_html.lower().split()
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
            if i[0].split('_')[0] not in return_words and i[0].split('_')[0] != word.split('_')[0]:
                return_words.append(i[0].split('_')[0])
            else:
                continue
        return return_words
    else:
        # Увы!
        return f"Слово {word.split('_')[0]} отсутствет в словаре"


def get_synonym_for_text(text_from_html):
    # model = gensim.models.KeyedVectors.load('d:/My_sinonimaizer/Rus2Vec_models/214/model.model')
    model = gensim.models.KeyedVectors.load_word2vec_format(config.PATH_FOR_MODEL_BIN, binary=True)
    words = normalization_text(text_from_html.split())
    dict_words = {x.split('_')[0]: None for x in words}
    # Попросим у модели 10 ближайших соседей для каждого слова и коэффициент косинусной близости для каждого:
    for word in words:
        words_list = []
        # есть ли слово в модели? Может быть, и нет
        if word in model:
            # выдаем 10 ближайших соседей слова:
            for i in model.most_similar(positive=[word], topn=5):
                # слово  # + коэффициент косинусной близости
                words_list.append(i[0].split('_')[0])
            dict_words[word.split('_')[0]] = words_list
    return dict_words

# if __name__ == '__main__':
#     start = time.time()
#     get_synonym_for_word()
#     print(f'работало {time.time() - start} секунд')
