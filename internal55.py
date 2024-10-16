from nltk.tokenize import sent_tokenize
#import nltk
from nltk.tokenize import word_tokenize
#nltk.download('punkt_tab')
f=open("C:/Users/kiran/Documents/data1.txt")
text=f.read()
print(text)

sent = sent_tokenize(text)
print("Number of sentences:", len(sent))

for i in range(len(sent)):
    print("\nSentence:", i + 1, "\n", sent[i])
    word = word_tokenize(text)
print("\nTotal Words:", len(word))
print(word)
