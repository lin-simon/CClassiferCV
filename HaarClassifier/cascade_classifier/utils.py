import os

def gen_neg():
    with open ('neg.txt','w') as f:
        for filename in os.listdir('negative'):
            f.write('negative/' + filename + '\n')