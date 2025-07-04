#Write a program to input any alphabet and check whether it is vowel or consonant.
alpha = input("Enter the char: ")

if(alpha in "aeiou" or alpha in "AEIOU"):
#if(alpha == 'a' or alpha == 'e' or alpha == 'i' or alpha == 'o' or alpha == 'u'):
    print("Vowel")
else:
    print("Consonant")
    
