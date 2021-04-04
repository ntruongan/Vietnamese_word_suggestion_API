# -*- coding: utf-8 -*-
"""
Created on Wed Mar 31 14:24:26 2021

@author: ntruo
"""
import glob
import codecs
filenames = glob.glob('D:\IT\RESEARCH\large_project\how-i-met-your-mother-second-season_vietnamese\pre\*.srt')


for i, filename in enumerate(filenames):
    sourceFile = codecs.open(filename, "r", "utf-16-le")
    targetFile = codecs.open("converted_%s.srt" % i, "w", "utf-8")
    contents = sourceFile.read()
    targetFile.write(contents)
    sourceFile.close()
    targetFile.close()