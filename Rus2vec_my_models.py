import gensim
from gensim.models import Word2Vec
import normalization_words

# import logging
# import sys
# import wget as wget
# import zipfile


# model_url = 'http://vectors.nlpl.eu/repository/11/180.zip'
# m = wget.download(model_url)
# model_file = model_url.split('/')[-1]
# with zipfile.ZipFile(model_file, 'r') as archive:
#     stream = archive.open('model.bin')
#     model = gensim.models.KeyedVectors.load_word2vec_format(stream, binary=True)
# model = gensim.models.KeyedVectors.load(f)
# model = gensim.models.KeyedVectors.load_word2vec_format('214/model.model', binary=False)

# with open('214/model.model', 'r') as f:

model = gensim.models.KeyedVectors.load('Rus2Vec_models/214/model.model')

# Модели fasttext в новой версии gensim загружаются при помощи следующей команды::
# gensim.models.KeyedVectors.load("model.model")

# Перед загрузкой скачанный архив с моделью fasttext необходимо распаковать. Определить необходимый для загрузки файл
# несложно, чаще всего это файл с расширением .model (остальные файлы из архива должны быть в той же папке).
# Вернемся к нашей модели, созданной на основе НКРЯ. Скажем, нам интересны такие слова (пример для русского языка):

#words = ['день_NOUN', 'ночь_NOUN', 'человек_NOUN', 'семантика_NOUN', 'студент_NOUN', 'студент_ADJ']
words = normalization_words.input_word(input())


# Попросим у модели 10 ближайших соседей для каждого слова и коэффициент косинусной близости для каждого:
for word in words:
    # есть ли слово в модели? Может быть, и нет
    if word in model:
        print(word)
        # выдаем 10 ближайших соседей слова:
        for i in model.most_similar(positive=[word], topn=10):
            # слово + коэффициент косинусной близости
            print(i[0], i[1])
        print('\n')
    else:
        # Увы!
        print(word + ' is not present in the model')

# Находим косинусную близость пары слов:
# print(model.similarity('человек_NOUN', 'обезьяна_NOUN'))

# Найди лишнее!
# print(model.doesnt_match('яблоко_NOUN груша_NOUN виноград_NOUN банан_NOUN лимон_NOUN картофель_NOUN'.split()))

# Реши пропорцию!
# print(model.most_similar(positive=['пицца_NOUN', 'россия_NOUN'], negative=['италия_NOUN'])[0][0])
