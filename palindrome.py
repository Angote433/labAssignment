# Assignment 1 - Palindrome checker
 
def is_palindrome(text):
    # ignore spaces and letter case
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
 
 
user_input = input("Enter a string: ")
 
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')