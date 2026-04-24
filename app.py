import requests

def space():
        print("")

def get_joke(j_type):
        response = requests.get(f"https://v2.jokeapi.dev/joke/{j_type}")
        if response.status_code != 200:
                print("Error fetching data!")
        data = response.json()
        print(data)
        return {
                "type": data["category"],
                "1/2": data['type'],
                "question": data["setup"] or data["joke"],
                "answer": data["delivery"]
        }
found = False
while found == False:
        if found == False:
                space()
                user_type = input("Choose 1 of these joke types: Programming, Misc, Dark, Spooky, Christmas, or Pun (Case sensitive: Upper) ")
                if user_type == "Programming" or "Misc" or "Dark" or "Spooky" or "Christmas" or "Pun":
                        found = True
                else:        
                        print("This type does not exist")


joke_data = get_joke(user_type)
space()
if joke_data["1/2"] == "single":
        print("This is a single part joke:")
        space()
        print(joke_data["question"], joke_data["answer"])
else:
        print("This is a two-part joke:")
        space()
        print("Take your best guess as to what the answer could be...")
        guess = input(f"{joke_data['question']} ")
        if guess == joke_data['answer']:
                print("How did you know...?")
        else:
                print("Ah you suck! This was the answer:")
                print(joke_data['answer'])
space()
