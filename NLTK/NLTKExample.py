from nltk.tokenize import word_tokenize, sent_tokenize 
# 1 Tokenizing 
# Word tokenizers .... Sentence tokenizers
# Terms: lexicon and corporas
# Corpora - Body of text. ex: medical journals, presidential speeches
# Lexicon - Words and their means

# investor-speak .... regular english-speak

# Investor speak "bull" = someone who is positive about the market
# Engilish speak "bull" = scary animal 

example_text = "Hello Mr. Smith, how are you doing today? The weather is great and Python is awesome. The sky is pinkish-blue. You should not eat cardboard."

print (word_tokenize(example_text))
print()
print (sent_tokenize(example_text))
print()

# 2 Stop Words
from nltk.corpus import stopwords
example_sentence = "This is an example showing off stop word filtration."
stop_words = set(stopwords.words("english"))
print (stop_words)
print()

words = word_tokenize(example_sentence)

filtered_sentence = []
for w in words:
    if w not in stop_words:
        filtered_sentence.append(w)

print (filtered_sentence)
print()

filtered_sentence = [w for w in words if w not in stop_words]
print (filtered_sentence)
print()

# 3 Stemming
from nltk.stem import PorterStemmer

ps = PorterStemmer()

example_words = ["python","pythoner","pythoning","pythoned", "pythonly"]

stem_words = [ps.stem(w) for w in example_words]

print (stem_words)
print()

new_text = "It is very important to be pythonly while you are pythoning with python. All pythoner have pythoned poorly at least once."

words = word_tokenize(new_text)

stem_words = [ps.stem(w) for w in words]
print(stem_words)
print()

# Nowadays, most of time we do not need to use stemming since we have word net.

# 4 Part of Speech Tagging (label every word)
import nltk 
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# PunktSentenceTokenizer is an unsupervised machine learning based tokenizer. You can train it if you want. It's already pretrained.
train_text = state_union.raw("2005-GWBush.txt")
sample_text = state_union.raw("2006-GWBush.txt")
cumstom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = cumstom_sent_tokenizer.tokenize(sample_text)

def process_content():
        try:
                for i in tokenized:
                        words = nltk.word_tokenize(i)
                        tagged = nltk.pos_tag(words)
                        print (tagged)

        except Exception as e:
                print(str(e))

#process_content()

# 5 Chunking (Chunking is like grouping. This part needs Regular Expression)
chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>+<NN>?}"""
chunkParser = nltk.RegexpParser(chunkGram)
def process_content_chunk():
        try:
                for i in tokenized:
                        words = nltk.word_tokenize(i)
                        tagged = nltk.pos_tag(words)
                        chunked = chunkParser.parse(tagged)
                        chunked.draw()

        except Exception as e:
                print(str(e))

#process_content_chunk()

# 6 Chinking (removal of something)
chunkGram = r"""Chunk: {<.*>+} 
                }<VB.?|IN|DT|TO>+{"""  # This is regular expression. 
chunkParser = nltk.RegexpParser(chunkGram)
def process_content_chink():
        try:
                for i in tokenized[:5]:
                        words = nltk.word_tokenize(i)
                        tagged = nltk.pos_tag(words)
                        chunked = chunkParser.parse(tagged)
                        chunked.draw()

        except Exception as e:
                print(str(e))

#process_content_chink()

# 7 Name Entity Recognition
def process_content_NER():
        try:
                for i in tokenized[:5]:
                        words = nltk.word_tokenize(i)
                        tagged = nltk.pos_tag(words)
                        nameEnt = nltk.ne_chunk(tagged, binary=True)
                        nameEnt.draw()
        except Exception as e:
                print(str(e))

#process_content_NER()

# 8 Lemmatizing 
# Lemmatizing is very similar to stemming. The only difference is the end results are real words
# Lemmatizing is more useful than stemming
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("geese"))
print(lemmatizer.lemmatize("Geese"))
print()
print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better",pos="a"))
print(lemmatizer.lemmatize("best",pos="a"))
print()
#The default pos for lematize is "n"

# 9 Corpora
from nltk.corpus import gutenberg
from nltk.tokenize import sent_tokenize

sample = gutenberg.raw("bible-kjv.txt")
tok = sent_tokenize(sample)
print(tok[0:15])
print()

# 10 WordNet
# You can use wordnet to look up synonyms, antonyms, definition and context to words 
from nltk.corpus import wordnet
syns = wordnet.synsets("program")
#show different meaning of program
print(syns)
print()
print(syns[0].name())
print()
print(syns[0].lemmas()[0].name())
print()
# lemmas: 词源
#definition
print(syns[0].definition())
print()
#examples
print(syns[0].examples())
print()

synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
        for l in syn.lemmas():
                #print("l:", l)
                synonyms.append(l.name())
                if l.antonyms():
                        antonyms.append(l.antonyms()[0].name())
                        #print(l.antonyms())

print(synonyms)
print()
print(antonyms)
print()

#Word sematic similarity
w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("boat.n.01")
print(w1.wup_similarity(w2))
print()

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("car.n.01")
print(w1.wup_similarity(w2))
print()

w1 = wordnet.synset("ship.n.01")
w2 = wordnet.synset("cat.n.01")
print(w1.wup_similarity(w2))
print()

