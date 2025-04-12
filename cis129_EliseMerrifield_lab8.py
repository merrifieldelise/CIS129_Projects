def is_palindrome(string):
    # Normalize the string to ignore case
    normalized_string = string.lower()

    # Use a stack to store characters
    stack = []

    for char in normalized_string:
        stack.append(char)

    # Reconstruct the string by popping from the stack
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()

    # Check if the normalized string is equal to the reversed string
    if normalized_string == reversed_string:
        print("True")
        return True
    else:
        print("False")
        return False


# Example usage
is_palindrome("Racecar")  # Output: True
is_palindrome("hello")  # Output: False