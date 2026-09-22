from pythonds import Stack

def tagChecker(html): 
    s = Stack() 
    valid = True 
    tokens = html.split()
    # print(tokens)

    for t in tokens:
        if t.startswith("<") and not t.startswith("</"):
            s.push(t)
        elif t.startswith("</"):
            if s.isEmpty():
                print("Error: No matching opening tag for", t)
                return False
            else:
                openingTag = s.pop()
                if openingTag[1:] != t[2:]:
                    print("Error: Mismatched tags:", openingTag, "and", t)
                    return False

    if not s.isEmpty():
        print("Error: Unclosed tags:", s.items)
        return False

    return True

def main():
    htmlString = '''
    <html>
        <head>
            <title> </title>
        </head>
        <body>
            <h1> </h1>
            <p> This is a sample paragraph. </p>
            <div>
                 <p> Another paragraph inside a div. </p>
            </div>
        </body>
    </html>
    '''
    v = tagChecker(htmlString)
    if v:
        print("The HTML tags are properly nested and matched.")
    else:
        print("The HTML tags are not properly nested or matched.")

if __name__ == "__main__":
    main()

