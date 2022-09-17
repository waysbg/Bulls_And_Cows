from sys import exit
import random

while True:
    want_to_play = str(input("Command: 'End' terminates a started game!     Do you want to play Bulls & Cows? (y/n): "))
    if want_to_play == 'y':
        different_generated_digits = False
        while different_generated_digits == False:
            generated_number = str(random.randrange(1111, 10000))
            different_generated_digits = generated_number[0] not in generated_number[1:] and \
                                         generated_number[1] not in (generated_number[:1] + generated_number[2:]) and \
                                         generated_number[2] not in (generated_number[:2] + generated_number[3:]) and \
                                         generated_number[3] not in generated_number[:3]
            if different_generated_digits:

                print()
                # print(generated_number)      # Tester during game generation

                won_game = False
                given_guesses = 0
                guessed_number = '____'
                while guessed_number != generated_number:
                    bulls_count = 0
                    cows_count = 0
                    if given_guesses == 0:
                        print(f'{given_guesses}.{guessed_number}. - {bulls_count}b {cows_count}c', end='')
                    guessed_number = str(input('                                                     Four Different Digits: '))
                    if guessed_number == 'End':
                        exit()
                    elif guessed_number.isnumeric() == False or len(guessed_number) != 4:
                        print('                                                     Enter four different digits number: ')
                        continue
                    else:
                        given_guesses += 1
                        for count in range(0,4):
                            if guessed_number[count] == generated_number[count]:
                                bulls_count += 1
                            else:
                                if guessed_number[count] in generated_number:
                                    cows_count += 1
                        print(f'{given_guesses}.{guessed_number}. - {bulls_count}b {cows_count}c', end='')
                if given_guesses == 1:
                    print(f' ------ You won the game in {given_guesses} move!\n')
                else:
                    print(f' ------ You won the game in {given_guesses} moves!\n')
    else:
        break