import os
from ..perspective import Perspective, allowed
import random
import string
import unittest

api_key = os.environ.get("API_KEY")

def generate_text():
    paragraph = []
    sentences = random.randrange(3,6)+1
    for x in range(sentences):
        words = random.randrange(2,10)+1
        sentence = []
        for y in range(words):
            characters = random.randrange(0,10)+1
            word = ""
            for z in range(characters):
                word += random.choice(string.ascii_uppercase + string.ascii_lowercase)
            sentence.append(word)
        paragraph.append(" ".join(sentence) + ".")
    return " ".join(paragraph)

class PerspectiveTests(unittest.TestCase):
    p = Perspective(api_key)

    def test_invalid_test(self):
        with self.assertRaises(ValueError):
            self.p.score(generate_text(),tests="NOT_A_TEST")

    def test_invalid_test_type(self):
        with self.assertRaises(ValueError):
            self.p.score(generate_text(), texts=0)

    def test_comment(self):
        for x in range(10):
            test = random.choice(allowed)
            comment = self.p.score(generate_text(),tests=test)
            self.assertTrue(0 <= comment[test].score <= 1)
            for attr in comment[test].spans:
                self.assertTrue(0 <= attr.score <= 1)
                self.assertTrue(str(attr) in comment)

if __name__ == '__main__':
    if __package__ is None:
        from os import sys, path
        sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
    unittest.main()