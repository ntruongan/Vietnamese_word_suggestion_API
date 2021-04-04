# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 13:52:15 2021

@author: ntruo
"""

import glob
import re

def read_file():
    filenames = glob.glob('D:\IT\RESEARCH\large_project\how-i-met-your-mother-second-season_vietnamese\*.srt')
    list_seq = []
    for filename in filenames:
        for line1 in open(filename, encoding='utf-8'):
            if "-->" in line1:
                continue
            if line1 == "\n":
                continue
            if "Chuyển ngữ phụ đề bởi" in line1:
                continue
            if "\n" in line1:
                line1 = line1.split("\n")[0]
                if line1.isnumeric(): # check if line is number
                    continue
            line1 = re.sub('[-]', ' ', line1)
            line1 = line1.strip()
            print(line1)
            list_seq.append(line1)
    return list_seq

vie_seq = read_file()
#%%
print("number of sentence: %d" % len(vie_seq))

#%%

import pickle
pickle.dump(vie_seq, open("all_sequence.p","wb"))




