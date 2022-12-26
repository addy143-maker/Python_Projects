from spellchecker import SpellChecker
corrector = SpellChecker()

word = input("Enter the word :- ")
if word in corrector :
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct spelling is ", correct_word)