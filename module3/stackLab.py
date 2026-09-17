import pythonds3

def main():
    s = pythonds3.Stack()
    s.push('Hello')
    s.push('World')
    
    print(s.pop())  # Output: World
    print(s.pop())  # Output: Hello

    
main()