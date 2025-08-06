
print("Hello! I am AI chatbot. Tell me your name?")
name = input()

print(f"Nice to meet you, {name}!")

while True:
    
    print("How are you feeling today? (good/bad/Normal)")
    mood = input().lower()

    if mood == "good":
        print("I'm glad to hear that!")
    elif mood == "bad":
        print("I'm sorry to hear that.")
    elif mood == "normal":
        print("Got it. Sometimes 'normal' is just right.")
    else:
        print("I see. No worry sometimes it's hard to put feelings into words.")

   
    print("What is one thing you like to do in your free time?")
    hobby = input()
    print(f"That's really a good hobby! {hobby} is a great way to spend time.")
    print("Do you have any favorite books or movies?")
    favorites = input()
    print(f"Great! {favorites} sounds interesting.")
    print("Would you like to keep chatting? (yes/exit)")
    choice = input().lower()
    # Check if the user wants to exit the chat
    if choice == "exit":
        print(f"It was nice chatting with you, {name}. Goodbye!")
        break
