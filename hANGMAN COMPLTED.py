    from random import randint

    word_list = ["DOG", "CAT", "PIG", "ANT", "KEY", "EYE", "LIP", "BUS", "MAP", "ELF", "COW", "BAT", "HAT", "BED",
                 "ICE"]

    clue_list = ["i am a pet that has four legs,you might hear me barking",
                 "this is a feline whose lives can reach nine",
                 "this provides meat that you would eat and this is what gives you bacon",
                 "this is a type of insects with antennae on it's head and can be fire or red",
                 "to open a door you can knock or use this item to unlock",
                 "i am closed at night and give you sight",
                 "i have no voice and yet i speak to you,i tell all things in the world that people do",
                 "this vehicle makes frequent stops amd the ones you take to school are yellow",
                 "it can help you to find a route so that you don't get lost and go on",
                 "i am a little helper who makes your gift from santa clause",
                 "milk is what they make and give us a juicy steak",
                 "they are often found just hanging out upside down inside a cave",
                 "a chef's tall one is white ,i might be a beanie or a beret that's flat",
                 "when it gets dark every night,it's on me people sleeping",
                 "i float on the top of the water and am as cold as can be"]

    def placer(letter, founded, chosen_word):
        if letter in chosen_word:
            if letter == chosen_word[0] and founded == "":
                print(letter, dash, dash)
                founded = founded + letter
            elif letter == chosen_word[1] and founded == "":
                print(dash, letter, dash)
                founded = founded + letter
            elif letter == chosen_word[2] and founded == "":
                print(dash, dash, letter)
                founded = founded + letter
            elif letter == chosen_word[0] and founded == chosen_word[1]:
                print(letter, founded, dash)
                founded = founded + letter
            elif letter == chosen_word[0] and founded == chosen_word[2]:
                print(letter, dash, founded)
                founded = founded + letter
            elif letter == chosen_word[1] and founded == chosen_word[2]:
                print(dash, letter, founded)
                founded = founded + letter
            elif letter == chosen_word[1] and founded == chosen_word[0]:
                print(founded, letter, dash)
                founded = founded + letter
            elif letter == chosen_word[2] and founded == chosen_word[1]:
                print(dash, founded, letter)
                founded = founded + letter
            elif letter == chosen_word[2] and founded == chosen_word[0]:
                print(founded, dash, letter)
                founded = founded + letter
            elif letter == chosen_word[0] and founded == chosen_word[1] + chosen_word[2] or chosen_word[2] + \
                    chosen_word[1]:
                print(chosen_word)
                print("you won")
                satisfy=True
            elif letter == chosen_word[1] and founded == chosen_word[0] + chosen_word[2] or chosen_word[2] + \
                    chosen_word[0]:
                print(chosen_word)
                print("you won")
                satisfy= True
            elif letter == chosen_word[2] and founded == chosen_word[0] + chosen_word[1] or chosen_word[1] + \
                    chosen_word[0]:
                print(chosen_word)
                print("you won")
                satisfy = True

    def check(n):
        if n == 3:
            print("you lost")
        else:
            print("you won")

    num = randint(0, 14)
    chosen_word = word_list[num]
    dash = "_"
    founded = ""
    print("the clue is :")
    print(clue_list[num])
    nu = 0
    satisfy = False

    while satisfy== False and nu < 3:
        inp = input("enter a letter:")
        inp1 = inp.upper()
        if inp1 in chosen_word and inp1 not in founded:
            placer(inp1, founded, chosen_word)
            founded += inp1
        elif inp1 in chosen_word and inp1 in founded:
            print("already guessed")
            nu += 1
        else:
            print("wrong")
            nu += 1

    check(nu)

