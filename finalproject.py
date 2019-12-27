#
# Alex Doval
#
# Final Project
# The Goal of this final project was to input 3 textfiles: one acting as an original work and the last two as two samples
# Then this program uses an algorithm to determine which of the two samples is more likely to come from the author of the original work
#

import math

class TextModel:
    """ a blueprint for objects that model a body of text"""
    def __init__(self, model_name):
        """ This method constructs a new TextModel object by accepting a string
        model_name as a parameter and initializing the following three attributes
        """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.prepositions = {}
        
    def __repr__(self):
        """ This method eturns a string that includes the name of the model as
        well as the sizes of the dictionaries for each feature of the text."""
        s = 'text model name: ' + self.name + '\n'
        s += ' number of words: ' + str(len(self.words)) + '\n'
        s += ' number of word lengths: ' + str(len(self.word_lengths)) + '\n'
        s += ' number of stems: ' + str(len(self.stems)) +'\n'
        s += ' number of sentence lengths: ' + str(len(self.sentence_lengths)) + '\n'
        s += ' number of prepositions: ' + str(len(self.prepositions))
        return s

    def add_string(self, s):
        """ This method adds a string of text s to the model by augmenting
        the feature dictionaries defined in the constructor. """
        string = clean_text(s)
        word_list = string.split()
        for i in word_list:
            if i in self.words:
                self.words[i] += 1
            else:
                self.words[i] = 1
        length_word_list = []
        for j in word_list:
            length_word_list += [len(j)]
        for k in length_word_list:
            if k in self.word_lengths:
                self.word_lengths[k] += 1
            else:
                self.word_lengths[k] = 1
        for a in word_list:
            if stem(a) in self.stems:
                self.stems[stem(a)] += 1
            else:
                self.stems[stem(a)] = 1
        s = s.replace('?', '.')
        s = s.replace('!', '.')
        sentences = s.split('.')
        sentences = sentences[:-1]
        for d in sentences:
            length_of_sentence = len(d.split())
            if length_of_sentence in self.sentence_lengths:
                self.sentence_lengths[length_of_sentence] += 1
            else:
                self.sentence_lengths[length_of_sentence] = 1
        list_of_prepositions = ['of', 'with', 'at', 'from', 'into', 'to', 'in', 'during', 'including', 'until', 'aganist', 'among', 'throughout', 'despite', 'towards', 'upon', 'for', 'on', 'by', 'about', 'but', 'before', 'after', 'between']
        for r in word_list:
            if r in list_of_prepositions:
                if r in self.prepositions:
                    self.prepositions[r] += 1
                else:
                    self.prepositions[r] = 1

    def add_file(self, filename):
        """ This method adds all of the text in the file identified by filename
        to the model. """
        f = open(filename, 'r', encoding='utf8', errors='ignore')
        text = f.read()
        f.close()
        self.add_string(text)

    def save_model(self):
        """This method saves the TextModel object self by writing its various
        feature dictionaries to files."""
        file_words = self.name + '_' + 'words'
        f = open(file_words, 'w')
        f.write(str(self.words))
        f.close()
        file_word_lengths = self.name + '_' + 'word_lengths'
        f2 = open(file_word_lengths, 'w')
        f2.write(str(self.word_lengths))
        f2.close()
        file_stem = self.name + '_' + 'stem'
        f3 = open(file_stem, 'w')
        f3.write(str(self.stems))
        f3.close()
        file_sentence_lengths = self.name + '_' + 'sentence_lengths'
        f4 = open(file_sentence_lengths, 'w')
        f4.write(str(self.sentence_lengths))
        f4.close()
        file_prepositions = self.name + '_' + 'prepositions'
        f5 = open(file_prepositions, 'w')
        f5.write(str(self.prepositions))
        f5.close()
        
    def read_model(self):
        """ This method reads the stored dictionaries for the called TextModel object
        from their files and assigns them to the attributes of the called TextModel."""
        file_words = self.name + '_' + 'words'
        f = open(file_words, 'r')
        words_str = f.read()
        f.close()
        dict_words = dict(eval(words_str))
        self.words = dict_words
        file_word_lengths = self.name + '_' + 'word_lengths'
        f2 = open(file_word_lengths, 'r')
        word_lengths_str = f2.read()
        f2.close()
        dict_word_lengths = dict(eval(word_lengths_str))
        self.word_lengths = dict_word_lengths
        file_stems = self.name + '_' + 'stem'
        f3 = open(file_stems, 'r')
        stem_str = f3.read()
        f3.close()
        dict_stem = dict(eval(stem_str))
        self.stems = dict_stem
        file_sentence_lengths = self.name + '_' + 'sentence_lengths'
        f4 = open(file_sentence_lengths, 'r')
        sentence_lengths_str = f4.read()
        f4.close()
        dict_sentence_lengths = dict(eval(sentence_lengths_str))
        self.sentence_lengths = dict_sentence_lengths
        file_prepositions = self.name + '_' + 'prepositions'
        f5 = open(file_prepositions, 'r')
        prepositions_str = f5.read()
        f5.close()
        dict_prepositions = dict(eval(prepositions_str))
        self.prepositions = dict_prepositions

    def similarity_scores(self, other):
        """ This method computes and returns a list of log similarity scores measuring
        the similarity of self and other – one score for each type of feature """
        word_score = compare_dictionaries(other.words, self.words)
        word_lengths_score = compare_dictionaries(other.word_lengths, self.word_lengths)
        stems_score = compare_dictionaries(other.stems, self.stems)
        sentence_lengths_score = compare_dictionaries(other.sentence_lengths, self.sentence_lengths)
        prepositions_score = compare_dictionaries(other.prepositions, self.prepositions)
        list_of_scores = []
        list_of_scores += [word_score]
        list_of_scores += [word_lengths_score]
        list_of_scores += [stems_score]
        list_of_scores += [sentence_lengths_score]
        list_of_scores += [prepositions_score]
        return list_of_scores

    def classify(self, source1, source2):
        """ This method compares the called TextModel object (self) to two other “source” TextModel
            objects (source1 and source2) and determines which of these other TextModels is the more
            likely source of the called TextModel.
        """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print('scores for ' + source1.name + ': ' + str(scores1))
        print('scores for ' + source2.name + ': ' + str(scores2))
        sum_scores1 = sum(scores1)
        sum_scores2 = sum(scores2)
        if sum_scores1 > sum_scores2:
            print(self.name + ' is more likely to have come from ' + source1.name)
        else:
            print(self.name + ' is more likely to have come from ' + source2.name)

               
def clean_text(txt):
    """This method takes a string of text txt as a parameter and returns
        a list containing the words in txt after it has been “cleaned”. """
    s = txt
    s = s.replace('.', '')
    s = s.replace(',', '')
    s = s.replace('?', '')
    s = s.replace('!', '')
    s = s.replace(';', '')
    s = s.replace(':', '')
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace('"', '')
    s = s.replace("'", '')
    s = s.lower()
    return s

def stem(s):
    """This stem accepts a string as a parameter. The function should then
    return the stem of s.
    """
    if len(s) == 0:
        s = s
    elif s[-3:] == 'ing':
        if len(s) > 4:
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
        else:
            s = s[:-3]
    elif s[-3:] == 'est':
        if len(s) > 4:
            if s[-4] == s[-5]:
                s = s[:-4]
            else:
                s = s[:-3]
        else:
            s = s[:-3]
    elif s[-2:] == 'er':
        if len(s) > 3:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
        else:
            s = s[:-2]
    elif s[-3:] == 'ies':
        s = s[:-2]
    elif s[-1] == 's':
        s = s[:-1]
        s = stem(s)
    elif s[-2:] == 'es':
        s = s[:-2]
        s = stem(s)
    elif s[-2:] == 'ed':
        if len(s) > 3:
            if s[-3] == s[-4]:
                s = s[:-3]
            else:
                s = s[:-2]
        else:
            s = s[:-2]
    elif s[-4:] == 'tion':
        s = s[:-4]
    elif s[-1] == 'y':
        s = s[:-1] + 'i'
    elif s[-2:] == 'ie':
        s = s[:-2]
    elif s[-2:] == 'en':
        s = s[:-2]
    elif s[-3:] == 'ful':
        s = s[:-3]
    elif s[-4:] == 'ible':
        s = s[:-4]
    elif s[-4:] == 'able':
        s = s[:-4]
    elif s[-2:] == 'ic':
        s = s[:-2]
    elif s[-4:] == 'less':
        s = s[-4:]
    elif s[-4:] == 'ness':
        s = s[-4:]
    elif s[-4:] == 'ment':
        s = s[-4:]
    elif s[-5:] == 'ation':
        s = s[-5:]
    elif s[-4:] == 'tion':
        s = s[-4:]
    elif s[-3:] == 'ion':
        s = s[-3:]
    elif s[-3:] == 'ity':
        s = s[:-3]
    elif s[-2:] == 'ty':
        s = s[:-2]
    elif s[-5:] == 'ative':
        s = s[:-5]
    elif s[-5:] == 'itive':
        s = s[:-5]
    elif s[-3:] == 'ive':
        s = s[:-3]
    return s

def compare_dictionaries(d1, d2):
    """ This function take two feature dictionariesd1 and d2 as inputs, and it should
        compute and return their log similarity score. """
    score = 0
    total = 0
    for i in d1:
        total += d1[i]
    if total == 0:
        score = 0
    else:
        for i in d2:
            if i in d1:
                score += (math.log(d1[i]/total) * d2[i])
            else:
                score += (math.log(0.5 / total) * d2[i])
    return score

def test():
    """A test for the model"""
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')
    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')
    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    mystery.classify(source1, source2)


def run_tests():
    """A test comapring my writing style to the writing styles of Arthur Conan Doyle and Mark Twain"""
    source1 = TextModel('Arthur Conan Doyle')
    source1.add_file('Arthur_Conan_Doyle.txt')
    source2 = TextModel('Mark Twain')
    source2.add_file('Mark_Twain.txt')
    new1 = TextModel('Batman paper')
    new1.add_file('Batman_paper.txt')
    new1.classify(source1, source2)
    new2 = TextModel('watchmen paper')
    new2.add_file('watchmen_paper.txt')
    new2.classify(source1, source2)
    new3 = TextModel('comic book analysis')
    new3.add_file('comic_book_analysis.txt')
    new3.classify(source1, source2)
    new4 = TextModel('land transportation')
    new4.add_file('land_transportation.txt')
    new4.classify(source1, source2)

            
        
        
    
    
    
        
        
        
        
        
        
    
                
