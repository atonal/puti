#!/usr/bin/env python3

import markovify
import os
import random

BLOG_DIR='../crawler/blog-posts'
TITLE_MAX_LEN=80

BLOG_SIZES = [
        {
            'sentences': [1, 2],
            'paragraphs': [1, 2]
            },
        {
            'sentences': [2, 3],
            'paragraphs': [2, 3]
            },
        {
            'sentences': [2, 4],
            'paragraphs': [2, 4]
            },
        {
            'sentences': [2, 5],
            'paragraphs': [3, 6]
            }
        ]

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

    size = random.choice(BLOG_SIZES)

    num_of_paragraphs = random.randrange(size['paragraphs'][0], size['paragraphs'][1]+1)
    paragraphs = []
    # body
    for i in range(num_of_paragraphs):
        num_of_sentences = random.randrange(size['sentences'][0], size['sentences'][1]+1)
        sentences = generate_sentences(text_model, num_of_sentences)
        paragraphs.append(' '.join(sentences))

    return title, paragraphs

if __name__ == '__main__':
    title, paragraphs = generate_post()
    body = '\n\n'.join(paragraphs)
    post = '{}\n\n{}'.format(title, body)
    print(post)
