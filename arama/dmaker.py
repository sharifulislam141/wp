text = input("Enter text: ")
words = text.split()
for word in words:
    dork = f"wordpress uncategorized/hello-world {word} site:in"
    print(dork)
    with open('dorklist.txt','a') as f:
        f.write(dork+"\n")
        