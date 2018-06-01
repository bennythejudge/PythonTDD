import unittest
from textlib import BodyOfText

class TestBodyOfText(unittest.TestCase):
    def test_empty_story(self):
        bot = BodyOfText("")
        self.assertEqual(0, bot.num_paragraphs())

    def test_single_paragraph(self):
        bot = BodyOfText("one single sentence\n")
        self.assertEqual(1, bot.num_paragraphs())

    def test_several_paragraphs(self):
        multi_line = """this is a multi line string with 3 paragraphs
        this is the second
        and this is the third
        """
        bot = BodyOfText(multi_line)
        self.assertEqual(3, bot.num_paragraphs())


    def test_paragraphs_method(self):
        multi_line = "this is a multi line string with 3 paragraphs\nthis is the second\nand this is the third"
        bot = BodyOfText(multi_line)
        self.assertEqual(3,len(bot.paragraphs()))
# Copyright 2015-2018 Aaron Maxwell. All rights reserved.
