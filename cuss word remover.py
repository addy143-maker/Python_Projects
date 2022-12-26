from better_profanity import profanity
text = input("Enter the text with cuss word : ")
censored = profanity.censor(text)
print(censored)