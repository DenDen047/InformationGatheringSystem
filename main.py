#!/usr/bin/python
# -*- coding: utf-8 -*-
# -*- coding: cp932 -*-

import sys
import tweepy
from tweepy import  Stream, TweepError
import logging
import urllib
# import urllib2
from datetime import datetime as dt


# === Classify Text Type ===
# To classify input text data into text types(ex. URL, ProgrammingLangage...)
def classifyTextType(inputData):
	if inputData.count('http') and inputData.count('://'):
		print 'This data is URL.'
	else:
		print 'I dont know this data type.'
	return


def userInput(message):
	print message,
	data = raw_input(" -> ")
	return data


# === MAIN ===
def main():
	data = userInput("Please, type of something")
	classifyTextType(data)


if __name__ == "__main__":
  main()