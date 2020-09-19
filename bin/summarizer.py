# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:13:14 2020

@author: hp
"""

import yaml
import numpy as np
class SummarizeDoc:
    
    def __init__(self):
        with open('../config/config.yml','r') as fl:
            self.config = yaml.load(fl)
        
    def loadDocs(self,filePath):
        with open(filePath,'r') as fl:
            text = fl.read()
        return text
    
    def splitSentences(self,text):
        """
        Split paragraph into an array of sentences
        
        Input:
            text: string
        Output:
            sentences: a list of string
        """
        sentences = text.split('.')
        return sentences
    
    def groupSentences(self,sentences):
        firstSent, restOfSent = sentences[0], sentences[1:]
        return firstSent, restOfSent
    
    def findSentLength(self,text):
        return text.split()
    
    def findSentLengthArray(self,sentences):
        return [self.findSentLength(sent) for sent in sentences]
    
    def findTopsentences(self,sentLegths,sentences,n):
        sortedIdx=np.argsort(sentLegths)
        topnIdx=sortedIdx[-n:]
        topnSentences=[sentences[i] for i in topnIdx]
        return topnSentences
    
        def preprocess(self,text):
        preprocessObj = PreprocessDoc()
        filteredText = preprocessObj.removeSpclChar(text)
        filteredText = preprocessObj.convertToLower(filteredText)
        return filteredText
    
    def findSummary(self):
        filePath=self.config['data_path']['train_data']
        text=self.loadDocs(filePath)
        sentences=self.splitSentences(text)
        firstSent, restOfSent = self.groupSentences(sentences)
        sentLengths=self.findSentLengthArray(restOfSent)
        topnSentences=self.findTopsentences(sentLegths, restOfSent, self.config['sentence_num'])
        allSentences = [firstSent] + topnSentences
        summary = ' '.join(allSentences)
        return summary


summarizeObj = SummarizeDoc()
