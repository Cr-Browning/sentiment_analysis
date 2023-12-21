# -*- coding: utf-8 -*-
"""
Created on Fri Dec'  8 19:46:29 2023

@'author: Owner
"""


# Sentiment Analysis

def sentiment_analysis():
    words_value = 0
    neg_word_lst = []
    pos_word_lst = []
    neu_word_lst = []

    with open('positive_words.txt', "r") as p_file:
        pos_words = [word.strip() for word in p_file]
                

    with open('negative_words.txt', "r") as n_file:
        neg_words = [word.strip() for word in n_file]
        
    with open('keylog.txt', "r") as klog_file:
        klog_words = [word.strip() for word in klog_file]

    for words in klog_words:
        if words in neg_words:
            words_value -= 1
            neg_word_lst.append("x")
        elif words in pos_words:
            words_value += 1
            pos_word_lst.append("x")
        else:
            words_value += 0
            neu_word_lst.append("x")
        
    
    if words_value > 0:
        impact ='positive impact'
    elif words_value < 0 :
        impact = 'negative impact' 
    elif words_value == 0 :
        impact = 'no impact'
    print(impact)
    
    return impact, neg_word_lst, pos_word_lst, neu_word_lst


    
        

