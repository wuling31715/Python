# _*_ coding: utf-8 _*_
import os, shutil, glob, uniout, sys

num = range(1, 100)
name = raw_input('What\'s your name? ')
with open('107.csv', 'w') as new:
    new.write('Hello  %s!\n' % (name))
    for i in num:
        new.writelines(str(i) + '\n')
