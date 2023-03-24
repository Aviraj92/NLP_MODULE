
#this module contains the basic nlp algorithems for operation.

def sentence_segmentation(file):
    #initiating
    file = open(file)

    #processing
    sentences = file.readlines()
    file.close()

    #return value
    return sentences

def convert_to_commoncase(sentences):

    #initiating
    lower_sentences = []

    #processing
    for i in sentences:
        lower_sentences.append(i.lower())

    #return value
    return lower_sentences


def tokenize(sentences):
    # initiating code prerequisits
    special_to_remove = ['!','"','#','$','%','&','\'','(',')','*','+',',','‑','.','/',':','<','=','>','?','\\','{','[',']','}','%','^',';']
    filtered_tokens = []

    #processing
    tokens = sentences.split()

    for i in tokens:
        for j in i:
            if j in special_to_remove:
                i = i.replace(j,"")
        filtered_tokens.append(i)

    #return value
    return filtered_tokens

def stopword_removal(Tokens):

    #accessing txt files
    f = open('../data/stopwords.txt')
    stopwords = str(f.read())
    f.close()

    #creating list of stopwords
    stopwords = stopwords.split()
    filtered_tokens = []

   #processing
    for i in Tokens:
        if i not in stopwords:
            filtered_tokens.append(i)


    #return value
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


def stemming(filtered_tokens):

    #initializing
    returnlist = []
    from nltk.stem import PorterStemmer

    #processing
    ps = PorterStemmer()
    for w in filtered_tokens:
        returnlist.append(ps.stem(w))

    #return value
    return (returnlist)

def lematization(filtered_tokens):

    #initializing
    return_list = []
    import nltk
    from nltk.stem import WordNetLemmatizer
    # Download the required nltk resources (if not already downloaded)
    nltk.download('punkt', quiet=True)
    nltk.download('wordnet', quiet=True)
    # Create a lemmatizer object
    lemmatizer = WordNetLemmatizer()

    #processing
    lemmatized_words = [lemmatizer.lemmatize(word) for word in filtered_tokens]

    #return values
    return lemmatized_words

def bag_of_words(data):

    #initializing
    vocavolary = []
    frequencies = []

    #processing
    for i in data:
        if i not in vocavolary:
            vocavolary.append(i)
            frequencies.append(1)
        else:
            frequencies[vocavolary.index(i)] += 1

    return_dict = dict(zip(vocavolary,frequencies))


    #return value
    return return_dict


