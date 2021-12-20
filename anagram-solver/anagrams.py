#! /usr/bin/env python3
from itertools import permutations, combinations
from english_words import english_words_lower_alpha_set
from english_words import english_words_alpha_set
import string
from collections import defaultdict
import argparse
import editdistance

class Anagrams:
    '''Takes in an English string as input and returns a list of anagrams'''

    def __init__(self, no_proper_nouns = False, correct_spelling = False):
        self.no_proper_nouns = no_proper_nouns
        self.correct_spelling = correct_spelling
        self.common_dict = [eng_word.lower() for eng_word in english_words_alpha_set if eng_word[0].islower()]
        self.all_dict = english_words_lower_alpha_set

    def longest_common_prefix(self, s, t):
        '''Finds length of LCP'''
        lcp_len = 0
        while(lcp_len <= min(len(s),len(t)) and s[:lcp_len]==t[:lcp_len]):
            lcp_len += 1
        return lcp_len-1

    def find_correct_spelling(self, word):
        '''Corrects spelling of word using edit distance from words in given dictionary'''
        required_dict = self.common_dict if self.no_proper_nouns else self.all_dict
        if word in required_dict:
            return word
        edit_distances = [(candidate, editdistance.eval(candidate, word)) for candidate in required_dict]
        min_edit_distance = min(edit_distances, key = lambda x: x[1])[1]
        best_candidates = [candidate for candidate, ed in [p for p in edit_distances if p[1]==min_edit_distance]]
        compare_lcp = [(candidate, self.longest_common_prefix(candidate, word)) for candidate in best_candidates]
        max_lcp_candidate = max(compare_lcp, key = lambda x: x[1])[0]
        return max_lcp_candidate

    def preprocess(self, word):
        '''Removing punctuation and spaces, lowercasing'''
        word = word.lower().strip().replace(" ", "")
        for punct in string.punctuation:
            word = word.replace(punct, "")

        if self.correct_spelling:
            word = self.find_correct_spelling(word)

        return word

    def anagrammer(self, word):
        '''Returns list of anagrams of ``word'' including self'''
        anagram_list = list()
        required_dict = self.common_dict if self.no_proper_nouns else self.all_dict
        for perm in map("".join, permutations(word)):

            if perm in required_dict and perm not in anagram_list:
                # print(perm)
                anagram_list.append(perm)

        return anagram_list

    def anagram_driver(self, word, min_length = None):
        '''Returns anagrams'''
        word = self.preprocess(word)

        anagrams_by_length = defaultdict(lambda: list())
        if not min_length:
            min_length = len(word)
        for length in range(min_length, len(word)+1):
            for subword in map("".join, combinations(word, length)):
                grams = self.anagrammer(subword)
                if grams:
                    anagrams_by_length[length].append(grams)
        return word, anagrams_by_length

    def accept_input(self):
        '''Takes input and calls anagram_driver'''
        print("ENTER WORDS TO BE ANAGRAMMED IN THE FOLLOWING FORMAT:\
        ``WORD'' ``MIN_LENGTH_OF_ANAGRAM''(OPTIONAL)")
        print("ENTER ``QUIT'' TO QUIT\n")
        while True:
            entry = input()
            if entry.lower()=="quit":
                break
            entry = entry.strip().split()
            word = entry[0].strip()
            if len(entry)==2:
                min_length = int(entry[1].strip())
            else:
                min_length = len(word)
            correct_word, solution = self.anagram_driver(word, min_length = min_length)
            if word != correct_word:
                print(f"FINDING ANAGRAMS FOR: {correct_word}")
            for key, anagrams in solution.items():
                print(f"ANAGRAMS OF LENGTH {key}:")
                for comb in anagrams:
                    print(", ".join(comb))
            print("\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description = "Anagram Solver!")
    parser.add_argument("--no_proper_nouns", "-p", action="store_true", \
                        help = "If you would like to avoid proper nouns\
                        in the anagram list. If correct_spelling is set to True,\
                        proper nouns will also not be considered as corrections.")
    parser.add_argument("--correct_spelling", "-c", action="store_true", \
                        help = "Correct spelling mistakes in input!")

    args = parser.parse_args()

    anagram = Anagrams(args.no_proper_nouns, args.correct_spelling)
    anagram.accept_input()
