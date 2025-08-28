print("""
 ██████  █████  ███████ ███████  █████  ██████       ██████ ██ ██████  ██   ██ ███████ ██████  
██      ██   ██ ██      ██      ██   ██ ██   ██     ██      ██ ██   ██ ██   ██ ██      ██   ██ 
██      ███████ █████   ███████ ███████ ██████      ██      ██ ██████  ███████ █████   ██████  
██      ██   ██ ██           ██ ██   ██ ██   ██     ██      ██ ██      ██   ██ ██      ██   ██ 
 ██████ ██   ██ ███████ ███████ ██   ██ ██   ██      ██████ ██ ██      ██   ██ ███████ ██   ██ 
                                                                                               
                                                                                               
                                                                                               """)
import string
alphabets= list(string.ascii_lowercase)

def caesar(original_text,shift_amount,encode_or_decode):
    output_text="" 


    if encode_or_decode=="decode" or encode_or_decode=="d":
        shift_amount*=-1
        # the shift gets multiplied by - sign:hence goes in backward direction
        #and should be outside for loop bcz inside its for whole encryption and here the shift value gets changed
    for letter in original_text:
        
        if letter in alphabets:             #if letters in original text
            shifted_position= (alphabets.index(letter)+ shift_amount)%26
            output_text+= alphabets[shifted_position]

        else:
            output_text+=letter
                    #if non-alphabet characters (like spaces or punctuation)


    return output_text

should_continue=True

while should_continue:
    user_choice=input("Type encode/e for Encryption ORRR Type decode/d for Decryption:\n").lower()      
    text =input(f"Enter the text you want to {user_choice}:\n").lower()
    shift=int(input("Type the shift number: "))
    
    result=caesar(original_text=text, shift_amount=shift, encode_or_decode=user_choice)
    print(f"Here is the {user_choice}d result= {result}")
#calls the function and prints result everytime we do. So it should be in the loop itself
    
    restart=input('Type "yes" if you want to continue else type "no": ')
    if restart=="no":
        should_continue=False
        print("Thanyou!!")







        
    

