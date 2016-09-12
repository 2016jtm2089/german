
import sys
str1 = sys.argv[1]      #command line for taking string input


wordList1 = str1.split(None)  #converting string to list
#print wordList1




freqD2 = {}
for word2 in wordList1:
        freqD2[word2] = freqD2.get(word2, 0) + 1    #creating dictionary with keys as words and frequency as values
        
count=0
for w in sorted(freqD2, key=freqD2.get, reverse=True):  #loop for printing top 3 frequent words in the sorted dictionary BY VALUES
  print w, freqD2[w]
  count+=1
  if count > 2:
   break



u= raw_input("enter word to be searched: ")       # searching for word in the string
print "%-10s %d" % (u, freqD2[u])





