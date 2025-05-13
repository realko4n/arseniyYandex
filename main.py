import ru_core_news_md
from spacy.lang.ru.stop_words import STOP_WORDS
from textblob import TextBlob
from googletrans import Translator

import asyncio

model = ru_core_news_md.load()
text = model("Норм фильм")
text_list = [word.lemma_ for word in text]
print(text_list)

filter_text_list = [elem for elem in text_list if not elem in STOP_WORDS]
print(filter_text_list)
async def translate_text(text):
    translator = Translator()
    translated = await translator.translate(text, src='ru', dest='en')

    return  translated.text

text_to_translate = str(filter_text_list)
res = asyncio.run(translate_text(text_to_translate))

analys = TextBlob(res)

ocenka = analys.sentiment.polarity
print(ocenka)
if ocenka > 0:
    print("Положительный")
elif ocenka < 0:
    print("Негативный")
else:
    print("Нейтральный")