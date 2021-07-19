# -*- coding: utf-8 -*-
"""
load_fasta()

This function reads a FASTA format sequence file, checking if the file exists, and if it contains a valid sequence.
It returns a string containing the sequence in the acgt form, folded to lower case.
In case of any error, it will ask again for the right file name.
"""
def load_fasta():

    sequenceImported = False
    #creating file object
    while not sequenceImported:
        fileName = input('Enter filename(or its address if it is in another folder): ')
        while True:
            try:
                sequenceFile = open(fileName,'r')
                break
            #DEBUG
            except IOError:
                print ('\nUnable to open the file! Be sure that the filename and address are correct and that the file exists\n')
                fileName = input('Enter filename(or its address if it is in another folder): ')

        # loading sequence from the file
        sequence = '' #initialised sequence string

        while True: #accumulate sequence line by line
            line = sequenceFile.readline()
            if line == '':
                break
            elif '>' in line:
                continue
            else:
                sequence += line.strip().lower()
        sequenceFile.close()
        sequence = sequence.replace('u','t')

        # checking for mistakes in the sequence imported

        bases = ['a','c','g','t']

        if sequence=='': #checking if it is empty
            print('File is empty!\nTry another file\n\n')

        else: #checking if it is a valid sequence
            for i in range(0,len(sequence)):
                if sequence[i] not in bases:
                    print('There is an error in the sequence, check the file and try again')
                    break
                else:
                    sequenceImported = True

    print('\nSequence correctly imported.\n\n')
    return (sequence)
##############################################################

"""
translate(seq,k)

This function translates the input sequence string in protein and returns its string
"""
def translate(seq, k, codonTable):
    protein=''
    for i in range(k, len(seq), 3):
        codon=seq[i:i+3]
        if len(codon)<3:
            break
        else:
            protein += codonTable[codon]
    return protein

##############################################################

"""
complementary(seq)

This function translates the input sequence string in its complementary and returns its string
"""
def complementary(seq):
    compStrand=''
    for i in range(0, len(seq)):
        if seq[i]=='a':
            compStrand+='t'
        elif seq[i]== 't':
            compStrand+='a'
        elif seq[i]=='c':
            compStrand+='g'
        elif seq[i]=='g':
            compStrand+='c'
    compStrand = compStrand[::-1]
    return compStrand

##############################################################

### defining arrange function

def arrange(frame, symChoice):
    arrangedFrame = ''
    if symChoice in['a','A']:
        for i in range(0, len(frame), 3):
            if frame[i:i+3] == 'Phe':
                arrangedFrame += 'F'
            elif frame[i:i+3] == 'Tyr':
                arrangedFrame += 'Y'
            elif frame[i:i+3] == 'Gln':
                arrangedFrame += 'Q'
            elif frame[i:i+3] == 'Asn':
                arrangedFrame += 'N'
            elif frame[i:i+3] == 'Lys':
                arrangedFrame += 'K'
            elif frame[i:i+3] == 'Asp':
                arrangedFrame += 'D'
            elif frame[i:i+3] == 'Glu':
                arrangedFrame += 'E'
            elif frame[i:i+3] == 'Trp':
                arrangedFrame += 'W'
            elif frame[i:i+3] == 'Arg':
                arrangedFrame += 'R'
            else:
                arrangedFrame += frame[i]
            arrangedFrame += '  '
    else:
        arrangedFrame = frame
    return arrangedFrame

###############################################################
def frameout(sequence, compsequence, arrf1, arrf2, arrf3, arrf4, arrf5, arrf6):
  ### location output, choice

    outChoice = input('\nWhere would you like the output to be printed?\n1. Console\n2. Create external file\n3. Both\nEnter your choice: ')
    while outChoice not in ['1','2','3']:
        outChoice = input('\nInsert 1, 2 or 3...\nWhere would you like the output to be printed?\n1. Console\n2. Create external file\n3. Both\nEnter your choice: ')

    ### which frame to print, choice

    frameNumbers = []

    frameChoice = input('\nWhat do you want to print?\n1. All 6 reading frames\n2. Specific reading frame ')
    while frameChoice not in ['1','2']:
        frameChoice = input('\nInsert 1 or 2...\nWhat do you want to print?\n1. All 6 reading frames\n2. Specific reading frame ')

    ### which frames to print, choice
    if frameChoice == '2':
        number = ''
        while (number != '0'):
            number = input('\nInsert frame number (0 to confirm): ')
            if number in frameNumbers or number not in ['0','1','2','3','4','5','6']:
                print('Invalid choice (enter Frame n. between 1-6) or check frame is not already printed')
            elif number != '0':
                    frameNumbers.append(number)
    else:
        frameNumbers = ['1','2','3','4','5','6']

    ### printing, external file

    if outChoice in ['2','3']:
            fileName = input('\nEnter output filename (if already existing it will be overwritten): ')
            fileName += '.txt'
            open(fileName, 'w').close()
            outputFile=open(fileName,'a')
            i = 0
            while i<len(sequence):
                if '1' in frameNumbers:
                    outputFile.write ('%s%s' % (arrf1[i:i+60], '\tF1\n'))
                if '2' in frameNumbers:
                    outputFile.write ('%s%s%s' % (' ', arrf2[i:i+60], '\tF2\n'))
                if '3' in frameNumbers:
                    outputFile.write ('%s%s%s' % ('  ', arrf3[i:i+60], '\tF3\n'))
                outputFile.write ('%s%s' % (sequence[i:i+60], '\n'))
                outputFile.write ('----:----|----:----|----:----|----:----|----:----|----:----|\n')
                outputFile.write ('%s%s' % (compsequence[i:i+60], '\n'))
                if '4' in frameNumbers:
                    outputFile.write ('%s%s' % (arrf4[i:i+60], '\tF4\n'))
                if '5' in frameNumbers:
                    outputFile.write ('%s%s%s' % (' ', arrf5[i:i+60], '\tF5\n'))
                if '6' in frameNumbers:
                    outputFile.write ('%s%s%s' % ('  ', arrf6[i:i+60], '\tF6\n'))
                outputFile.write ('__________________________________________________________________\n\n')
                i += 60
            outputFile.close()

    ### printing, console

    if outChoice in ['1','3']:
        i = 0
        while i<len(sequence):
            if '1' in frameNumbers:
                print(('%s%s' % (arrf1[i:i+60], '\tF1')))
            if '2' in frameNumbers:
                print(('%s%s%s' % (' ', arrf2[i:i+60], '\tF2')))
            if '3' in frameNumbers:
                print(('%s%s%s' % ('  ', arrf3[i:i+60], '\tF3')))
            print(sequence[i:i+60])
            print('----:----|----:----|----:----|----:----|----:----|----:----|')
            print(compsequence[i:i+60])
            if '4' in frameNumbers:
                print(('%s%s' % (arrf4[i:i+60], '\tF4')))
            if '5' in frameNumbers:
                print(('%s%s%s' % (' ', arrf5[i:i+60], '\tF5')))
            if '6' in frameNumbers:
                print(('%s%s%s' % ('  ', arrf6[i:i+60], '\tF6')))
            print ('__________________________________________________________________\n')
            i += 60

################################################################
def orfs(sequence, compsequence, f1, f2, f3, f4, f5, f6):

    orfs = []

    nestORFChoice = input('\nHow do you want your ORFs?\n1. Clean ORFs without nested genes, ie no multiple Met in between\n2. All ORFs, ie a new ORF is established each time Met and its correspective STOP codon is found ')
    while nestORFChoice not in ['1','2']:
        nestORFChoice = input('\nInsert 1 or 2...\nHow do you want your ORFs?\n1. Clean ORFs without nested genes, ie no multiple Met in between\n2. All ORFs, ie a new ORF is established each time Met and its correspective STOP codon is found ')

    frames = {f1:'f1',f2:'f2',f3:'f3',f4:'f4',f5:'f5',f6:'f6'}
    n = 0 #increases when ORFs are found

    def findORFs(frame, n): ###ORFs are then printed and put into a dictionary for comparison
        frameName = frames[frame]
        k=0
        j=frame.find('Met', k)
        while k<len(frame) and j!=-1:
            for i in range((j+3), len(frame), 3):
                if frame[i:i+3] == '***':
                    n += 1
                    print(('%d%s%s%s%s%s%d%s%d'   % (n, ': ', frame[j:i], '. Found in reading frame ',frameName, ', from base ', j, ', to base ', i)))
                    print ('\n')
                    orfs.append(frame[j:i])
                    break
                elif i == (len(frame)-3):
                    n += 1
                    print(('%d%s%s%s%s%s%d%s%d'   % (n, ': ', frame[j:i+3], '. Found in reading frame ',frameName, ', from base ', j, ', to base ', i+3)))
                    print ('\n')
                    orfs.append(frame[j:i+3])
            if nestORFChoice == '2':
                k = j+3
            else:
                k = i+3
            j = frame.find('Met', k)
        return n

    print ('\n\nORFs:\n')
    n = findORFs(f1,n)
    n = findORFs(f2,n)
    n = findORFs(f3,n)
    n = findORFs(f4,n)
    n = findORFs(f5,n)
    n = findORFs(f6,n)

    if len(orfs) == 0:
        print('0 ORFs found')
    else:
        largestORF = max(orfs, key=len)
        for elem in frames:
            if elem.find(largestORF) != -1:
                print(('%s%s%s%d%s%d' % ('Largest ORF found in ', frames[elem], ' from base ', elem.find(largestORF), ' to base ', elem.find(largestORF)+len(largestORF))))
                if frames[elem] == 'f1':
                    nucleotideSequence = sequence[elem.find(largestORF):elem.find(largestORF)+len(largestORF)]

                elif frames[elem] == 'f2':
                    nucleotideSequence = sequence[elem.find(largestORF)+1:elem.find(largestORF)+len(largestORF)+1]
                elif frames[elem] == 'f3':
                    nucleotideSequence = sequence[elem.find(largestORF)+2:elem.find(largestORF)+len(largestORF)+2]
                elif frames[elem] == 'f4':
                    nucleotideSequence = compsequence[elem.find(largestORF):elem.find(largestORF)+len(largestORF)]
                elif frames[elem] == 'f5':
                    nucleotideSequence = compsequence[elem.find(largestORF)+1:elem.find(largestORF)+len(largestORF)+1]
                elif frames[elem] == 'f6':
                    nucleotideSequence = compsequence[elem.find(largestORF)+2:elem.find(largestORF)+len(largestORF)+2]
                break

        print(nucleotideSequence)

        LargestORFcodons = {}
        for i in range(0, len(nucleotideSequence), 3):
            codon = nucleotideSequence[i:i+3]
            if codon in LargestORFcodons:
                LargestORFcodons[codon] += 1
            else:
                LargestORFcodons[codon] = 1
        print ('usage statistics, ie codon frequency: \n')
        for elem in LargestORFcodons:
            print(('%s%s%d' % (elem, ': ',LargestORFcodons[elem])))
