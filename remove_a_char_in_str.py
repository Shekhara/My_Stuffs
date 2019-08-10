import sys
import readchar

str_in  = raw_input("Enter the string ")

char_in = raw_input("Enter the char ")

def removeCh(str_in,char_in):
    str_out = ""
    for ch in str_in:
        if ch == char_in:
            continue 
        else :
            str_out += ch 

    return str_out


res = removeCh(str_in,char_in)

print("The final string after removing char = ", res)

