
#initieating
if __name__ == '__main__':
    print(f"{__name__} is currently running as a script")
    import module1

    #main code
    f = open('../data/testdoc.txt')
    corpus = f.read()
    f.close()
    normalizer = module1.textnormalization()

    normalized_text = normalizer.normalize_text(corpus)


    #output
    print(normalizer.bag_of_words(normalized_text))