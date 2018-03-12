import os
import re

txt_no=['1','2']

for tocheck in txt_no :
    pybank_txt = os.path.join('raw_data', 'paragraph_' + tocheck+".txt")
    with open(pybank_txt, 'r') as txtFile:
        words=[]
        lines=[]
        letters=[]
        total_revenue=0
        txtReader = txtFile.read()
       
        
        #for row in txtReader:
        words=re.split(r'\s',txtReader)   
        word_len=len(words)
        lines=re.split(r'\s*[!?.]\s',txtReader)
        line_len=len(lines)
        letters=len(re.split(r'\S',txtReader))
        avg_letter=letters/word_len
        avg_sen=word_len/line_len

    print("Paragraph analysis")
    print("("+str(pybank_txt)+")")
    print("------------------")
    print("Approx word count"+str(word_len))
    print("Approx sentence count"+str(line_len))
    #print("lenght letter"+str(letters))
    print("Average letter count"+str(avg_letter))
    print("Average Sentence count"+str(avg_sen))
    print("------------------")