#!/usr/bin/env python3

import markovify
import os

BLOG_DIR='../crawler/blog-posts'

def generate_post():
    text = ''
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

    # body
    sentences = []
    for i in range(10):
        sentence = text_model.make_sentence()
        if sentence is not None:
            sentences.append(sentence)

    body = ' '.join(sentences)
    return title, body

if __name__ == '__main__':
    title, body = generate_post()
    post = '{}\n\n{}'.format(title, body)
    print(post)
