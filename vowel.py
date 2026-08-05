text = input ("Enter a paragraph:")
character= len(text)
space = text.count(" ")
word=len(text.split())
vowels = "aeiouAEIOU"
vowel_count = 0

for char in text:
    if char in vowels:
        vowel_count += 1

#display results
print("==========text analysis========")
print("character:",character)
print("Total words:",word)
print("Total of spaces:", space)
print("Total of vowels:", vowel_count) 
#demostraiting indexing
if len(text)>0:
    print("/n first chracter(indexing):",text[0])
    print("/n last chracter(indexing):",text[-1])

print("/n first 10 chracter(slicing):",text[:10])
print("/n last 10 chracter(slicing):",text[-10:])



