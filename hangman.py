import random

print("hello change")


def hide_word(word):
    word_len = len(word) - 1
    index1 = random.randint(0, word_len)
    index2 = random.randint(0, word_len)
    word = list(word)
    word[index1] = '*'
    word[index2] = '*'

    final_word = ''
    for i in word:
        final_word += i

    return final_word

def execute():
    while True: 
        random_fruit = random.choices(words)[0]
        
        final_word = hide_word(random_fruit)
        print(f'\n{final_word} \nguess the word:', end='')
        guess = input()
        if guess == random_fruit:
            print('weldone!')
            break
        else:
            print('try again')

if __name__ == "__main__":
    print('''guess the B fruit type it out here''')

    words = ['banana', 'Bilberry', 'Blackberry', 'Blackcurrant', 'Black sapote', 'Blueberry', 'Boysenberry', 'Breadfruit']
    execute()





