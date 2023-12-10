import winsound
import termcolor

def TextToBeep(key: dict, text: str, duration: int) -> None:
    print(termcolor.colored('Playing The Sound...', 'red'))
    for i in text:
        try:
            winsound.Beep(key[i], duration)
        except Exception as ex:
            pass

def make_key(frequency: list) -> dict:
    key = {}
    alphabets = 'abcdefghijklmnopqrstuvwxyz '

    for i in range(len(alphabets)):
        key.update({f'{alphabets[i]}': frequency[i]})

    return key

def main():
    HelpMsg = termcolor.colored('''
=======================
        Help Menu
=======================

[1] Text to Sound:
    Convert text to a sequence of beeps, generating sound based on the input text.
    You will be prompted to enter the text, and the program will play the corresponding sound.

[2] Sound to Text (Coming Soon):
    This feature is currently under development and will be available in future updates.

[3] Help:
    Display this help message to understand how to use the program and its features.

[4] Exit:
    Close the program. You will be asked to confirm your decision before exiting.

=======================
     How to Use
=======================

1. Choose an option from the menu by entering the corresponding number.

2. Follow the on-screen instructions for each option.

3. Explore different functionalities and enjoy the program!

Note: Ensure your system's sound is turned on to hear the beeps.

Made by - Swadheen Mishra
>>=ByteClub=<<
''', 'cyan')


    Logo = '''

                      :::!~!!!!!:.
                  .xUHWH!! !!?M88WHX:.
                .X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:
             :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!
               !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~
            :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :
#"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~
.~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!               Made by - Swadheen Mishra
$R@i.~~ !     :   ~$$$$$B$$en:``                      >>=ByteClub=<<
?MXT@Wx.~    :     ~"##*$$$$M~
'''


    print(termcolor.colored(Logo, 'green'))
    print(termcolor.colored('[1] Text to sound.', 'blue'))
    print(termcolor.colored('[2] Sound to text.', 'blue'))
    print(termcolor.colored('[3] Help.', 'blue'))
    print(termcolor.colored('[4] Exit.', 'blue'))

    while True:
        UserOption = input(termcolor.colored('->', 'blue'))

        if UserOption == '1':
            text = input(termcolor.colored('[+] Enter the text: ', 'blue')).lower()

            frequencyList = [642, 1356, 1468, 2623, 2591, 1329, 2902, 1225, 970, 132, 298, 2716, 1935,
                        1183, 1439, 1915, 1778, 1874, 1217, 1594, 2446, 1082, 611, 1358, 2866, 681, 2500]
            duration = 300
        
            key = make_key(frequencyList)
            TextToBeep(key, text, duration)

        elif UserOption == '2':
            print(termcolor.colored('[-] Coming soon...', 'yellow'))
        elif UserOption == '3':
            print(HelpMsg)
        elif UserOption == '4':
            ExitAns = input(termcolor.colored('Are you sure? [Y/N]: ', 'red')).lower()

            if ExitAns == 'y':
                break
        else:
            print(termcolor.colored('Enter a valid option!', 'red'))

if __name__ == '__main__':
    main()