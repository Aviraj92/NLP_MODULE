# this module contains the basic nlp algorithems for operation  OOPs.


class textnormalization():

    def __init__(self):
        pass

    def sentence_segmentation(self, corpus):
        # initiating
        self.corpus = corpus.replace('\n','_')

        #processing
        self.corpus = self.corpus.replace(" ", "_")
        self.corpus = self.corpus.replace('.', " ")
        self.corpus = self.corpus.replace('_', " ")
        self.sentences = self.corpus.split()



        # return value
        return self.sentences

    def convert_to_commoncase(self, sentences):

        # initiating
        lower_sentences = []

        # processing
        for i in sentences:
            lower_sentences.append(i.lower())

        # return value
        return lower_sentences

    def tokenize(self, sentences):
        # initiating code prerequisits
        special_to_remove = ['!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '‑', '.', '/', ':', '<', '=',
                             '>', '?', '\\', '{', '[', ']', '}', '%', '^', ';']
        filtered_tokens = []

        # processing
        tokens = sentences.split()

        for i in tokens:
            for j in i:
                if j in special_to_remove:
                    i = i.replace(j, "")
            filtered_tokens.append(i)

        # return value
        return filtered_tokens

    def stopword_removal(self, Tokens):

        # accessing txt files
        f = open('../data/stopwords.txt')
        stopwords = str(f.read())
        f.close()

        # creating list of stopwords
        stopwords = stopwords.split()
        filtered_tokens = []

        # processing
        for i in Tokens:
            if i not in stopwords:
                filtered_tokens.append(i)

        # return value
        return filtered_tokens

    '''
    def stemming(filtered_tokens):

        #initiating
        stems = []
        f = open('suffixes.txt')
        suffixes = str(f.read())
        suffixes = suffixes.split()
        f.close()


        #processing

        for i in filtered_tokens:
            for j in suffixes:
                if not 1 + int(i.find(j)):
                    stems.append(i.replace(j, ""))




        #return value
        return stems'''

    def stemming(self, filtered_tokens):

        # initializing
        returnlist = []
        from nltk.stem import PorterStemmer

        # processing
        ps = PorterStemmer()
        for w in filtered_tokens:
            returnlist.append(ps.stem(w))

        # return value
        return returnlist

    def lematization(self,filtered_tokens):

        # initializing
        return_list = []
        import nltk
        from nltk.stem import WordNetLemmatizer
        # Download the required nltk resources (if not already downloaded)
        nltk.download('punkt', quiet=True)
        nltk.download('wordnet', quiet=True)
        # Create a lemmatizer object
        lemmatizer = WordNetLemmatizer()

        # processing
        self.lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]

        # return values
        return self.lemmatized_words

    def normalize_text(self,sentence,mode='s'):

        #initializing
        self.sentence = sentence

        #processing
        if mode == 's':
            self.normalized_text = self.stemming(self.stopword_removal(self.convert_to_commoncase(self.tokenize(self.sentence))))

        elif mode == 'l':
            self.normalized_text = self.lematization(self.stopword_removal(self.convert_to_commoncase(self.tokenize(self.sentence))))

        #return Value
        return self.normalized_text

    def bag_of_words(self,data):
        # initializing
        self.data = data
        self.vocavolary = []
        self.frequencies = []

        # processing
        for i in self.data:
            if i not in self.vocavolary:
                self.vocavolary.append(i)
                self.frequencies.append(1)
            else:
                self.frequencies[self.vocavolary.index(i)] += 1

        self.return_dict = dict(zip(self.vocavolary, self.frequencies))

        # return value
        return self.return_dict

class Calculations():
    def __init__(self):
        pass
'''
    def calculate_idf(self,doc_list):
        self.doc_list = doc_list
        import math
        self.idf_dict = {}
        N = len(self.doc_list)

        self.idf_dict = dict.fromkeys(self.doc_list[0].keys(), 0)
        for doc in self.doc_list:
            for word, val in doc.items():
                if val > 0:
                    self.idf_dict[word] += 1

        for word, val in self.idf_dict.items():
            self.idf_dict[word] = math.log(N / float(val))

        return self.idf_dict

    def TFIDF(self,idf,tf):
        self.idf = idf
        self.tf = tf
        self.tfidf = []

        pos_flag = 0
        for i in tf:
            try:
                self.tfidf.append(int(self.tf)+)

'''
class sentiment_analysis():
    def __init__(self):
        pass

class virtual_assistant():
    def __init__(self):
        pass

class text_summarization():
    def __init__(self):
        pass

