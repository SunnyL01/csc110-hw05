"""
Name: Sunny Li
Peers: (add any collaborators)
References: (anything you checked to solve this)
"""

def get_letter():
    """Asks the user for a single uppercase letter (A, B, C) until valid and returns it."""
    while True:
        text = input("Give an single uppercase letter: ")
        # Check the length first (a single character is required).
        if len(text) != 1:
            print("Error: it needs to be a single character.")
            continue
        
        # Check if the character is one of A, B, or C.
        if text != "A" and text != "B" and text != "C":
            print("Error: You provided the wrong character.")
            continue
        return text


def get_digit():
    """Asks the user for a single digit (1,2, or 3) until valid and returns it."""
    while True:
        text = input("Give an single number character: ")
        
        # Check if the input is composed only digit.
        if not text.isdigit():
            print("Error: your input should be only digits.")
            continue
        
        # Check if the input is one of 1,2, or 3.
        if text != "1" and text != "2" and text != "3":
            print("Error: a single digit needs to be in [1,3].")
            continue
        return text


def check_pattern(letter, digit, lst):
    """Prints each word where the letter appears before the digit."""
    print("Strings with the pattern:")
    
    for word in lst:
        # Find the first index of the letter using a nested loop.
        letter_idx = -1
        for i in range(len(word)):
            if word[i] == letter:
                letter_idx = i
                break
        
        # Find the first index of the digit using a nested loop.
        digit_idx = -1
        for j in range(len(word)):
            if word[j] == digit:
                digit_idx = j
                break
        
        # Only print if both were found and letter comes before digit.
        if letter_idx != -1 and digit_idx != -1 and letter_idx < digit_idx:
            print(word, end = " ")
            
    # Always finish the line (gives just a newline when no matches).
    print()


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------
    
    # A loop that get a letter, get a digit, check the pattern, then ask to report.
    while True:
        letter = get_letter()
        digit = get_digit()
        check_pattern(letter,digit,st_list)
        
        # Ask the user if they want to try again.
        answer = input("Try Again? (y/n): ")
        if answer != "y":
            break

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()