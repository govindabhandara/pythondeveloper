with open("aaa.txt")as f:
    word="dear"
    data=f.read()
    if (data.find(word)!=-1):
        print("found")
    else:
        print("not found")
