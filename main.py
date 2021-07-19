# -*- coding: utf-8 -*-

import utils
import codonDict

sequence = utils.load_fasta()
compsequence = utils.complementary(sequence)

#frames
f1 = utils.translate(sequence, 0, codonDict.codonTable)
f2 = utils.translate(sequence, 1, codonDict.codonTable)
f3 = utils.translate(sequence, 2, codonDict.codonTable)
f4 = utils.translate(compsequence, 0, codonDict.codonTable)
f5 = utils.translate(compsequence, 1, codonDict.codonTable)
f6 = utils.translate(compsequence, 2, codonDict.codonTable)

### amino acid type of notation, choice

symChoice = input('What kind of amino acid notation would you like?\nA. 1-letter\nB. 3-letter\nEnter your choice: ')
while symChoice not in ['a','b','A','B']:
    symChoice = input('\nInsert A or B...\nWhat kind of notation would you like?\A. 1-letter\B. 3-letter\nEnter your choice: ')

arrf1 = utils.arrange(f1, symChoice)
arrf2 = utils.arrange(f2, symChoice)
arrf3 = utils.arrange(f3, symChoice)
arrf4 = utils.arrange(f4, symChoice)[::-1]
arrf5 = utils.arrange(f5, symChoice)[::-1]
arrf6 = utils.arrange(f6, symChoice)[::-1] #frames arranged to be printed

utils.frameout(sequence, compsequence, arrf1, arrf2, arrf3, arrf4, arrf5, arrf6)

utils.orfs(sequence, compsequence, f1, f2, f3, f4, f5, f6)
