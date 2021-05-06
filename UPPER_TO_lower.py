print("enter your character")
a=input() #take_input
if len(a)==1:
    if a>='a' and a<='z':
        ch=ord(a) #convert_to_the_ascii_value_of_the_element
        ch=ch-32 #convert_to_UPPERCASE
        ch=chr(ch) #convert_to_character
        print("your upper case letter is",ch)
    elif a>='A' and a<='Z':
        ch=ord(a)
        ch=ch+32
        ch=chr(ch)
        print("your lower case letter is", ch)
    else:
        print("fot")
else:
    print("wrong_input")
