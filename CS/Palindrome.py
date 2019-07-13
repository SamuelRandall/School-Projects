def palindrome():
    s = input("Enter a name: ")
    for char in s:
        if char == s[len(s) - (s.index(char) + 1)]:
            pass
        else:
            print("Your name is not a palindrome.")
            return False
    print("Your name is a palindrome!")
    return True


palindrome()

