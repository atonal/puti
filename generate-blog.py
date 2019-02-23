#!/usr/bin/env python3

import markovify

# Get raw text as string.
with open("./masterblog.txt") as f:
    text = f.read()

# Build the model.
text_model = markovify.Text(text)

# Print five randomly-generated sentences
for i in range(5):
    sentence = text_model.make_sentence()
    if sentence is not None:
        print(sentence)

# # Print three randomly-generated sentences of no more than 140 characters
# for i in range(3):
#     print(text_model.make_short_sentence(140))
