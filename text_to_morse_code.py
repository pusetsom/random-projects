#A python program that converts text and or numbers to morse code.
def convert_to_morse(message):
    # Define a dictionary to store the Morse code for each letter
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
        'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
        'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
        '3': '...--', '4': '....-', '5': '.....', '6': '-....',
        '7': '--...', '8': '---..', '9': '----.'
    }
    
    # Split the input string into a list of words
    words = message.split()
    result = []
    
    # Loop over each word and convert it to Morse code
    for word in words:
        morse_word = []
        for char in word:
            if char.upper() in morse_code:
                morse_word.append(morse_code[char.upper()])
            else:
                morse_word.append(char)
        result.append(' '.join(morse_word))
    
    # Return the result as a string, with each word separated by a space
    return '/ '.join(result)

# Get the input from the user
input_message = input("Enter a message: ")

# Convert the input to Morse code
output_message = convert_to_morse(input_message)

# Print the result
print("Morse code:", output_message)
