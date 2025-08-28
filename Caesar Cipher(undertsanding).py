
# import string
# alphabets= list(string.ascii_lowercase)
             
              #ORRRRRR


alphabets=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

user_choice=input("Type encode/e for Encryption ORRR Type decode/d for Decryption:\n").lower()      
text =input(f"Enter the text you want to {user_choice}:\n").lower()
shift=int(input("Type the shift number: "))

#ENCRYPTION :

def encrypt(original_text,shift_amount):
    cipher_text=""   
                                       #empty string as of now---> to accumulate shifted positions
    for trace in original_text:
        shifted_position=(alphabets.index(trace) +shift_amount )%26     #h=7---->shift=7+2=9
                                                            #-->whole(added) of modulo 26
        cipher_text+= alphabets[shifted_position]       # each gets 

    return cipher_text

encrypted_text=encrypt(text,shift)
print(f"Here is the encoded result:{encrypted_text}")


#DECRYPTION

def decrypt(cipher_text,shift_amount):
    plain_text=""

    for letter in cipher_text:
        shifted_position= (alphabets.index(letter)-shift_amount)%26
        plain_text+= alphabets[shifted_position]

    return plain_text

decrypted_result= decrypt(encrypted_text,shift)
print(f"Here is the decoded result: {decrypted_result}")


if user_choice==encrypt|e
    print(f"Here is the encoded result:{encrypted_text}")
elif user_choice==decrypt|d:
    print(f"Here is the decoded result: {decrypted_result}")
else:
    print("An invalid choice. Please try again")
        