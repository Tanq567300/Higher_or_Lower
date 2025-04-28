import game_data as gd
import art as a
import random as r
print(f"{a.logo} \nWelcome to Higher or Lower!")
score=0
while True:
    compare = r.choices(gd.data, k=2)
    compare_A= compare[0]
    compare_B= compare[1]
    if compare_A['follower_count'] > compare_B['follower_count']:
        answer=compare_A
    elif compare_B['follower_count'] > compare_A['follower_count']:
        answer=compare_B
        print(f"Compare A: {compare_A['name']} ,a {compare_A['description']}, from {compare_A['country']}. \n {a.vs} \nAgainst B: {compare_B['name']} ,a {compare_B['description']}, from {compare_B['country']}.")
        user= input("Enter A or B: ").lower()
        if user == 'a' and compare_A==answer:
         
            score+=1
            print(f"correct, your score is {score}.")
            answer= compare_A
            continue
        elif user == 'b' and compare_B==answer:
          
            score+=1
            print(f"correct, your score is {score}.")
            answer= compare_B
        else:
        
            print(a.logo)
            print(f"Game Over \n Your score {score}")
            break


