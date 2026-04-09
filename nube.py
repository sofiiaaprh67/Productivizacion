import wikipedia
import re
from stop_words import get_stop_words
import matplotlib.pyplot as plt
from wordcloud import WordCloud

stop_words = get_stop_words('es')

def plot_cloud(wordcloud):
    plt.figure(figsize=(16, 10))
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

def limpiar_texto(texto):
    texto = re.sub(r'==.*?==+', '', texto)
    texto = texto.replace('\n', ' ')
    return texto

def crear_nube(x):
    wikipedia.set_lang("es")
    wiki = wikipedia.page(x)
    text = limpiar_texto(wiki.content)

    wordcloud = WordCloud(
        width=3000,
        height=2000,
        random_state=1,
        background_color='white',
        colormap='viridis',
        collocations=False,
        stopwords=stop_words + [x.lower(), x, "puede", "pueden", "si"]
    ).generate(text)

    plot_cloud(wordcloud)

crear_nube("Madrid")
crear_nube("Toledo")
