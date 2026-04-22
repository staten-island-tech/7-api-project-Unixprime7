import requests

def get_joke(j_type):
        response = requests.get(f"https://v2.jokeapi.dev/joke/{j_type}")
        if response.status_code != 200:
                print("Error fetching data!")
        data = response.json()
        return {
                "type": data["category"],
                "1/2": data['type'],
                "question": data["setup"],
                "answer": data["delivery"]
        }
found = False
while found == False:
        user_type = input("Choose 1 of these joke types: Programming, Misc, Dark, Spooky, Christmas, or Pun (Case sensitive: Upper) ")
        if user_type != "Programming" or "Misc" or "Dark" or "Spooky" or "Christmas" or "Pun":
                print("This type does not exist")
        else:
                break

joke_data = get_joke(user_type)

print(joke_data["question"], joke_data["answer"])
