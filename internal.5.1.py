from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
f=open("C:/Users/kiran/Desktop/data.txt")
text=f.read()
print(text)
w=sent_tokenize(text)
print("Number of sentences:",len(w))
for i in range(len(w)):
    print("\nSentence:",i+1,"\n",w[i])
    word=word_tokenize(text)
print("\nTotal Words:",len(word))
print(word)
