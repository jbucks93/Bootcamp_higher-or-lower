from game_data import data
from HL_art import logo, vs
import random



def get_celebrity(data):
    score = 0
    still_correct = True
    while still_correct:
        celebrities = random.choices(data, k = 2)
        # Celebrity A
        a_celeb = celebrities[0]
        a_name = a_celeb["name"]
        a_info = a_celeb["description"]
        a_home = a_celeb["country"]
        a_followers = int(a_celeb["follower_count"])
        
        #Celebrity B
        b_celeb = celebrities[1]
        b_name = b_celeb["name"]
        b_info = b_celeb["description"]
        b_home = b_celeb["country"]
        b_followers = int(b_celeb["follower_count"])

        print(f"Compare A: {a_name}, a {a_info}, from {a_home}.")
        print(vs)
        print(f"Against B: {b_name}, a {b_info}, from {b_home}.")

        answer = input("who was more followers? type 'A' or 'B': ").lower()

        if (answer == 'a' and a_followers > b_followers) or (answer == 'b' and b_followers > a_followers):
            print("Correct!")
            score += 1
        else:
            print("Incorrect, Game Over")
            still_correct = False
    print(score)





get_celebrity(data)