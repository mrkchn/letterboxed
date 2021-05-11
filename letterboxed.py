import sys
import timeit

class LetterBox():
  def __init__(self, top, left, bottom, right, word_list):
    self.word_list = word_list
    self.box = [top, left, bottom, right]
    self.letter_list = set([letter for side in self.box for letter in side])
    self.compatible_words = self.get_words()
    self.pruned_words = self.prune_words()
    self.solutions = self.find_solution()
  
  def len_set(self, word):
    return len(set(word))

  def get_words(self):
    compatible_words = []
    for word in self.word_list:
      if set(word) & self.letter_list == set(word):
        compatible_words.append(word)
    return compatible_words

  def prune_words(self):
    pruned_words = []
    for word in self.compatible_words:
      flag = True
      for i in range(0, len(word)-1):
        pair = set(word[i:i+2])
        if any([(pair & side) == pair for side in self.box]):
          flag = False
      if flag:
        pruned_words.append(word)
    return sorted(pruned_words, key=self.len_set, reverse=True)

  def find_solution(self):
    solutions = []
    for i in range(0, len(self.pruned_words)):
      first_word = self.pruned_words[i]
      for j in range(i, len(self.pruned_words)):
        second_word = self.pruned_words[j]
        if (set(first_word) | set(second_word)) == self.letter_list:
          if first_word[0] == second_word[-1]:
            solutions.append([second_word, first_word])
          elif first_word[-1] == second_word[0]:
            solutions.append([first_word, second_word])
    return solutions

def main(argv):
    starttime = timeit.default_timer()
    with open('/home/mark/github/word_list.txt', 'r') as f:
        word_list = f.read().split("\n") 
    if len(argv) < 4:
#        box = LetterBox({'i','c','b'},{'o','s','r'},{'m','t','g'},{'a','u','h'}, word_list=word_list)
        box = LetterBox({'z','b','a'},{'v','e','i'},{'d','u','t'},{'n','l','o'}, word_list=word_list)
    else:
        box = LetterBox(set(argv[0]), set(argv[1]), set(argv[2]), set(argv[3]), word_list=word_list)
    for sol in box.solutions:
        print("{}, {}\n".format(sol[0],sol[1]))
    print(len(box.solutions))
    print("The time difference is :", timeit.default_timer() - starttime)
if __name__ == "__main__":
    main(sys.argv[1:])
    
#import requests
#resp = requests.get('http://www.math.sjsu.edu/~foster/dictionary.txt').text