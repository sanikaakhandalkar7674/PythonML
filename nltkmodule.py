


import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.probability import FreqDist

#tokenization
from nltk.tokenize import sent_tokenize
text="""Hello my name is sanika, how are you doing today? The weather is great and cheerful, and city is awesome.
The sky is blue."""
tokenized_text=sent_tokenize(text)
print(tokenized_text)

from nltk.tokenize import word_tokenize
tokenized_word=word_tokenize(text)
print(tokenized_word)
from nltk.corpus import stopwords
stop_words=set(stopwords.words("english"))
print(stop_words)


lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer
stem = PorterStemmer()


print("Lemmatized Word:",lem.lemmatize(text,"v"))
print("Stemmed Word:",stem.stem(text))##pos

tokens=nltk.word_tokenize(text)
print(tokens)

nltk.pos_tag(tokens)

ps = PorterStemmer()


#Lexicon Normalization
#performing stemming and Lemmatization

