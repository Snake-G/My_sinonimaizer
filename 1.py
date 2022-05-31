import bs4 as bs
import urllib.request
import re
import nltk
from nltk.corpus import stopwords
from gensim.models import Word2Vec

#  Будем парсить страницу «Википедии» о романе Филипа Дика Do Androids Dream of Electric Sheep.
scrapped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Do_Androids_Dream_of_Electric_Sheep')
article = scrapped_data.read()

# С помощью объекта BeautifulSoup извлекаем из абзацев текст.
parsed_article = bs.BeautifulSoup(article, 'lxml')
paragraphs = parsed_article.find_all('p')

# Объединяем весь текст в переменной article_text.
article_text = ""
for p in paragraphs: article_text += p.text

# Дальнейшая работа любого скрипта зависит от того, насколько хорошо вы провели очистку исходного текста.
# Поэтому мы переводим все символы в нижний регистр.
cleaned_article = article_text.lower()

# Оставляем только буквы и убираем пробелы, используя регулярные выражения.
cleaned_article = re.sub('[^a-z]', ' ', cleaned_article)
cleaned_article = re.sub(r'\s+', ' ', cleaned_article)

# Готовим датасет для обучения.
all_sentences = nltk.sent_tokenize(cleaned_article)
all_words = [nltk.word_tokenize(sent) for sent in all_sentences]

# Проходимся по датасету и удаляем стоп-слова (те, которые не добавляют смысла, например, is).
for i in range(len(all_words)):
    all_words[i] = [w for w in all_words[i] if w not in stopwords.words('english')]

# Создаем модель Word2Vec со словами, чаще всего встречающимися в тексте. Например, теми,
# которые встречаются минимум 3 раза (min_count=3).
word2vec = Word2Vec(all_words, min_count=3)

# В рамках модели находим и выводим самое близкое по смыслу (topn=1) слово для book.
print(word2vec.wv.most_similar('try', topn=1))
