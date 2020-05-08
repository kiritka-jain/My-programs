if __name__ == '__main__':
    s = input()
    if 0<len(s)<1000:
        print(any(elem.isalnum() for elem in s))
        print(any(elem.isalpha() for elem in s))
        print(any(elem.isdigit() for elem in s))
        print(any(elem.islower() for elem in s))
        print(any(elem.isupper() for elem in s))

