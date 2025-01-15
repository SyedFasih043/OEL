def longest_palindrome(word):
                                      # Create a dictionary to count the frequency of each character in the word
    char_count = {}

                                                # Loop through each character in the word
    for char in word:
                                                # Increase the count if the character is already in the dictionary
        if char in char_count:
            char_count[char] += 1
                                                # Otherwise, set the count to 1
        else:
            char_count[char] = 1

    palindrome_length = 0
    odd_found = False                           # To track if we found any characters with an odd count

                                                # Loop through the character counts
    for count in char_count.values():
                                                # Add the even part of the count to the palindrome length
        palindrome_length += (count // 2) * 2

                                                # If there's an odd count, we can use one of those characters in the middle of the palindrome
        if count % 2 == 1:
            odd_found = True

                                                # If we found an odd character count, we can add 1 to the palindrome length for the middle character
    if odd_found:
        palindrome_length += 1

    return palindrome_length

            #Testing
print(longest_palindrome("civic"))
print(longest_palindrome("MADAM"))
