# Hangman
import random
hangman = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
      |
      |
      |
      |
=========''']

word_list = ["ardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
#print(f"pssst, the solution is {chosen_word}")

word_length = len(chosen_word)

lives = 6
    
display = ["_"] * word_length
print(display)

end_game = False

while not end_game: 
    
    print("Guess a letter: ")
    guess_letter = input().lower()

    for position in range(word_length):     # بيقولك هنا كرر عدد المحاولات بنفس عدد احرف الكلمة 
        letter = chosen_word[position]      # هنا بيعرف المتغير  letter بموقع احرف الكلمة بين range  اللي فيه
        if letter == guess_letter:              
            display[position] = letter      # هنا بيحط قيمة الحرف لو صح في المكان بتاعها

    if guess_letter not in chosen_word:
        lives -= 1
        print(f"Wrong guess, you lost a life. {lives}")
        print(hangman[int(lives)])
        if lives == 0:
            print("You lose!") 
            end_game = True
    print(display)
    if '_' not in display :
        end_game = True                     # هنا لازم نعطي  while  قيمة نهائية عشان متباش لانهائية
        print("You win!")