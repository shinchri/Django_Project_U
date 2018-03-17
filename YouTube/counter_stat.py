from collections import Counter

text = "In this exercise, the idea is to write a paragraph that would be a random passage from a story. " \
    "An effective paragraph is one that has unity (it isn’t a hodgepodge of things), " \
    "focus (everything in the paragraph stacks up to the whatever-it-is the paragraph is about), " \
       "and coherence (the content follows smoothly). For this exercise, the paragraph should be quick " \
    "to read--say, not be more than 100 words long."

words = text.split()

counter = Counter(words)
top_three = counter.most_common(3)
print(top_three)
