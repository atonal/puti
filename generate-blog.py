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

# title
title = text_model.make_short_sentence(80)
while not title:
    title = text_model.make_short_sentence(80)
print(title)

print('\n')

# body
for i in range(10):
    sentence = text_model.make_sentence()
    if sentence is not None:
        print(sentence, end=' ')

print('\n')
