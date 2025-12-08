chatting = "yes"

while chatting == "yes":
    print("Hello! I am AI Bot. What's your name? : ")

    name = input()

    print(f"Nice to meet you, {name}!")

    print("How are you feeling today? (good/bad) : ")
    mood = input().lower()

        
    if mood == "good":
        print("I'm glad to hear that!Doing hobbies can make you feel good. What are some of your hobbies?")
        hobbies = input()
    elif mood == "bad":
        print("I'm sorry to hear that. Hope things get better soon. Maybe doing some hobbies will cheer you up. What are some of your hobbies?")
        hobbies = input()
    else:
        print("I see. Sometimes it's hard to put feelings into words. What are some of your hobbies?")
        hobbies = input()
        
    
    print ("Doing things that you enjoy such as: " + hobbies + " is good for you!")

    chatting = input("Would you like to keep chatting(yes/no)?").lower()

print(f"It was nice chatting with you {name}. Goodbye!")