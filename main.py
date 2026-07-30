import random

def play_game():
    print("========================================")
    print("  مرحباً بك في لعبة تخمين الأرقام!  ")
    print("========================================")
    
    # اختيار رقم عشوائي بين 1 و 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("لقد اخترت رقماً بين 1 و 100. هل يمكنك تخمينه؟")
    
    while True:
        try:
            guess = int(input("ادخل تخمينك: "))
            attempts += 1
            
            if guess < secret_number:
                print("الرقم صغير جداً! جرب رقماً أكبر.")
            elif guess > secret_number:
                print("الرقم كبير جداً! جرب رقماً أصغر.")
            else:
                print(f" مبروك! لقد فزت واكتشفت الرقم الصحيح ({secret_number}) في {attempts} محاولات.")
                break
        except ValueError:
            print("الرجاء إدخال رقم صحيح فقط!")

if name == "main":
    play_game()
