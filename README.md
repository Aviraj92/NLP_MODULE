# NLP_MODULE

This open source library is designed to provide an easy-to-use set of tools for Natural Language Processing tasks. It includes a range of algorithms and functions organized into classes to help streamline NLP projects.

The library consists of several files, including:

Module 1: This module contains the primary NLP and machine learning algorithms and functions organized into classes.

nlp_algorithms: This module contains the same algorithms and functions but in an unorganized manner for debugging purposes.

"main.py": This is the main script of the library that demonstrates the usage of all the functions integrated into the modules.

"example.py": This file contains a demo project showcasing the implementation of the NLP algorithms provided in the library.

In addition to the code files, the library also includes a "data" folder containing text files required for some of the NLP algorithms. These files include "stopwords.txt", which contains commonly used stop words in the English language. You can add additional stop words according to your needs and the requirements of your model. The "suffixes.txt" file contains a list of commonly used suffixes in the English language, and you can add more as per your requirements. The "lemmas_xl.xlsx" and "words_219k.xlsx" files contain words and their corresponding lemmas.



The primary class in this version of the library is the "textnormalization" class, which contains several NLP methods:

"sentence_segmentation('corpus')": This method takes a corpus in string format as an argument and returns a python list of segmented sentences.

"convert_to_commoncase(segmented_sentences)": This method accepts a python list containing segmented sentences as an argument and returns a python list of sentences converted to lowercase.

"tokenize(segmented_sentences)": This method takes a list of segmented sentences and returns the tokens of the same.

"stopword_removal(tokens)": This method takes a list of tokens as an argument, removes stop words (as mentioned in "stopwords.txt"), and returns a filtered list of tokens.

"stemming(filtered_tokens)": This method takes a python list of filtered tokens as an argument, reduces them to their base form, and returns a list of stemmed tokens.

"lemmatization(filtered_tokens)": This method takes a list of filtered tokens as an argument and returns a list of lemmas for the same. However, this method is under development and may not work efficiently or even give rise to issues.

"normalize_text(corpus)": This method takes a sentence as input and applies a combination of these normalization methods to it based on the input mode. By default, it is set to 's' which applies stemming, but if you wish to lemmatize the tokens, you can write "object.normalize_text(corpus,mode='l')".

"bag_of_words(normalized_text)": This method takes the normalized text in the form of a python list as an argument and returns a vocabulary along with frequency for calculating TF, IDF, or TFIDF.
The other classes in the library include:



"sentiment_analysis": This class contains methods related to sentiment analysis.
"virtual_assistant": This class contains methods related to virtual assistants.
"text_summarization": This class contains methods related to text summarization.
Please note that these classes are currently under development, but can be used for future expansion and implementation of NLP algorithms.

Finally, the "nlp_algorithms.py" module contains all the NLP functions in an unorganized way. It can be used for debugging purposes or for quick implementation of NLP algorithms.




There are several possible errors that can occur when working with this module:

FileNotFoundError: This error can occur if the file path provided for input is incorrect or if the file does not exist. To resolve this, ensure that the correct file path is specified, and the file exists.

TypeError: This error can occur if the input parameter passed to a method is of the wrong type. To resolve this, ensure that the correct data type is passed to the method.

AttributeError: This error can occur if a method is called on an object that does not have the method defined. To resolve this, ensure that the correct object is used when calling the method.

ModuleNotFoundError: This error can occur if the required NLTK module is not installed. To resolve this, install the NLTK module using pip.

IndexError: This error can occur if the index used to access a list is out of range. To resolve this, ensure that the index used is within the range of the list.

ValueError: This error can occur if the input parameter passed to a method is not in the correct format. To resolve this, ensure that the correct format is used.

SyntaxError: This error can occur if there is a syntax error in the Python code. To resolve this, check the code for any syntax errors and correct them.

KeyError: This error can occur if a key used to access a dictionary does not exist. To resolve this, ensure that the key used exists in the dictionary.

To avoid these errors, make sure to carefully read the documentation and follow the instructions provided. Additionally, use appropriate error handling techniques such as try-except blocks to handle any errors that may occur.


For any bugs, queries, or feature requests, please contact me at aviraj.saha@outlook.com.
