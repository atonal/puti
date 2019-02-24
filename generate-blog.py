#!/usr/bin/env python3

import markovify
import os

text = ''

BLOG_DIR='crawler/blog-posts'

for file in os.listdir(BLOG_DIR):
    if file.endswith(".txt"):
        with open(os.path.join(BLOG_DIR, file)) as f:
            text += f.read()
            text += '\n\n'

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
