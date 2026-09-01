def main():
    groceries = ['Apples', 'Oranges', 'Bananas','Grapes', 'Lemons']
   
    myList = []
    myList.append('Chips')

    print(groceries[0:])

    newG = groceries[1:3]
    print(newG)

    #adding
    groceries.append('Chips')
    groceries.append('Cookies')
    groceries.append('Candy')
    groceries.append('Soda')
    
    groceries.insert(3,'cookies')
    print(groceries)

    x = groceries.pop()
    print(x)
    print(groceries)
 
 
    #mutable
    groceries[2] = 'ZZZZZZ'

    print(groceries)

    finalGroc = tuple(groceries)
    print(finalGroc)
    finalGroc[1] = 'zzzzz'
    print(finalGroc)

    
main()