import nltk, re, pprint

# Determiner (The)      Adjective (Big)     Whatever (*)    Noun (Coin)
gram = r"""
     PermittedChunk:
     {<.*>+} #this line chunks everything
     }<VB|NN>+{ #it chinks sequence of DT and NN
     """


chinkingParser = nltk.RegexpParser(gram)

def process(doc):
     original = doc
     print("Original-->",doc)
     doc = nltk.sent_tokenize(doc)
     print("Sent-Tokenized-->",doc)
     doc = [nltk.word_tokenize(s) for s in doc]
     print("Word-Tokenized-->",doc)
     doc = [nltk.pos_tag(s) for s in doc]
     print("POS-Tagged-->",doc)
     for s in doc:
          tree = chinkingParser.parse(s)
          print("Chinked-->", tree)
          tree.draw()


sent = "A quick fox jumped over the brown fence of the old house."
process(sent)

sent = "A fox jumped over the fence of the house."
process(sent)



gram = r"""
     PermittedChunk:
     {<DT>?<JJ>*<NN><VBD>?} #this line chunks everything
     }<DT|JJ>+{ #it chinks JJ
     """

gram = r"""
     PermittedChunk:
     {<DT>?<JJ>*<NN><VBD>?} #this line chunks everything
     }<DT|JJ>+{ #it chinks JJ
     """