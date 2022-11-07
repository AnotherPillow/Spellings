import gtts
import os
import random
import time

if not os.path.exists('audio'):
    os.makedirs('audio')

with open("words.txt", "r") as f:
    text = f.read()
    words = text.split("\n")
    f.close()
random.shuffle(words)

oldcwd = os.getcwd()
correct_words = 0
wrong_words = 0

VLC_PATH = "C:\\Program Files\\VideoLAN\\VLC\\"


for word in words:
    tts = gtts.gTTS(f'How do you spell {word}?', lang="en")
    tts.save(f"audio/{word}.mp3")
    word_path = os.path.join(os.getcwd(), "audio", f"{word}.mp3")

    os.chdir(VLC_PATH)
    os.system("vlc.exe " + word_path + " vlc://quit")
    os.chdir(oldcwd)
    time.sleep(1.5)
    guess = input("How do you spell that word? ")
    if guess == word:
        print("Correct!")
        correct_words += 1
    else:
        print("Wrong!")
        print(f"The correct spelling is {word}")
        wrong_words += 1
    os.remove(word_path)

print(f"You got {correct_words} words correct and {wrong_words} words wrong")


'''
tts = gtts.gTTS("Hello world")
tts.save("hello.mp3")
#define hello path as working directory
hello_path = os.path.join(os.getcwd(), "hello.mp3")

os.chdir("C:\\Program Files\\VideoLAN\\VLC")
os.system("vlc.exe " + hello_path + " vlc://quit")
'''