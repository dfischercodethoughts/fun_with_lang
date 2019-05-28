import threading
import sys

global debug

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
#takes a letter and returns a string array with input letter followed by all letters of alphabet
def letter_lengthen(letterin):
    to_ret = list()
    for i in alphabet:
        to_ret.append(letterin + i)
    return to_ret;


def letter_combinator(size):
    #takes a total length of word, and prints out all combinations of letters with size
    #one, then with size two, etc
    to_ret = alphabet

    for i in range(size-1):
        
        #print(to_ret)
        templist = []

        for char_seq in to_ret:
            
            temp = letter_lengthen(char_seq)
            for chars in temp:
                templist.append(chars)

        for chars in templist:
            to_ret.append(chars)
                
    if (debug):
        print(to_ret)
        
    return to_ret

    
    
if __name__ == "__main__":
    debug = True
    print("welcome; processing your input.")
    if len(sys.argv) < 3 and len(sys.argv) > 1:
        if debug:
            print("it seems you've entered: ")
            print(sys.argv)
            print("I will find all combinations of letters up to length: ")
            print(sys.argv[1])
        print("processing...")
        to_print = letter_combinator(int(sys.argv[1]))
        #for toP in to_print:
        #    print(toP)

