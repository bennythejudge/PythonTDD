class BodyOfText:
    def __init__(self, text):
        self.text = text
    def num_paragraphs(self):
        if self.text == "":
           return 0
        return self.text.count('\n')
    def paragraphs(self):
        return self.text.split('\n')
# Copyright 2015-2018 Aaron Maxwell. All rights reserved.