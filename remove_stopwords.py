import pandas as pd
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# Baixar recursos do NLTK
nltk.download('punkt')
nltk.download('stopwords')

# Carregar os posts
df = pd.read_csv("posts-limpos-manual.csv")

# Configurar stop words
stop_words = set(stopwords.words('portuguese'))

# Remover stop words e salvar resultado
df["text_clean"] = df["text"].astype(str).apply(lambda post: " ".join(
    [w for w in word_tokenize(post.lower()) if w.isalnum() and w not in stop_words]
))

# Salvar em um novo arquivo CSV
df.to_csv("posts-sem-stopwords.csv", index=False)
