import akinator
import webbrowser
import time

aki = akinator.Akinator()

q = aki.start_game()

if __name__=='__main__':        
    while aki.progression <= 80:
        a = input(q + "\n\t")
        if a == "b":
            try:
                q = aki.back()
            except akinator.CantGoBackAnyFurther as e:
                print(e)
                continue
        else:
            try:
                q = aki.answer(a)
            except akinator.InvalidAnswerError as e:
                print(e)
                continue
    aki.win()

    correct = input(f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?\n\t")

    if correct.lower() == "yes" or correct.lower() == "y":
        print("Yay\n")
        print("\nOpening picture in 4 seconds...\n")
        time.sleep(4)
        webbrowser.open(aki.first_guess['absolute_picture_path'])
    else:
        print("Oof\n")