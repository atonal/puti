#!/usr/bin/env python3

import markovify
import os

BLOG_DIR='../crawler/blog-posts'
TITLE_MAX_LEN=80

def generate_title(text_model):
    title = text_model.make_short_sentence(TITLE_MAX_LEN)
    while not title:
        title = text_model.make_short_sentence(TITLE_MAX_LEN)
    return title

def generate_sentences(text_model, num):
    sentences = []
    for i in range(num):
        sentence = text_model.make_sentence()
        while not sentence:
            sentence = text_model.make_sentence()
        sentences.append(sentence)
    return sentences

def generate_post():
    text = ''
    for file in os.listdir(BLOG_DIR):
        if file.endswith(".txt"):
            with open(os.path.join(BLOG_DIR, file)) as f:
                text += f.read()
                text += '\n\n'

    # Build the model.
    text_model = markovify.Text(text)

    title = generate_title(text_model)

    # body
    sentences = generate_sentences(text_model, 5)

    body = ' '.join(sentences)
    return title, body

if __name__ == '__main__':
    title, body = generate_post()
    post = '{}\n\n{}'.format(title, body)
    print(post)
