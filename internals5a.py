from nltk.tokenize import sent_tokenize, word_tokenize
import nltk


nltk.download('punkt')


with open("C:/Users/kiran/Documents/data1.txt") as f:
    text = f.read()
print(text)


sent = sent_tokenize(text)
print("Number of sentences:", len(sent))

for i in range(len(sent)):
    print("\nSentence:", i + 1, "\n", sent[i])


word = word_tokenize(text)
print("\nTotal Words:", len(word))
print(word)
