"""
http://tinyurl.com/z54w9cb
"""



musicians = ['billy corgan', 'com truise', 'perry ferrel']

places = [(1,2), (3,4), (5,6)]

attributes = {"height": "5'11", "favorite color": "red", "favorite author": "tolkien"}

def ama():
    print("What's my height: ")
    height = attributes["height"]
    print("What's my fav color: ")
    color = attributes["favorite color"]
    print("What's my fav author: ")
    author = attributes["favorite author"]
    return height, color, author 

result = ama()
print(result)
    
musician_dct = {musicians[0]: ["tonight, tonight", "hummer", "today"],
                musicians[1]: ["ether", "sundried"],
                musicians[2]: ["ocean size", "jane says"]}

print(musician_dct)