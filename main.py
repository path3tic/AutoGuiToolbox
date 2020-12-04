import pyautogui

def print_hi(name):

    print(f'Hi, {name}')
    pyautogui.alert('This is the message to display.')

if __name__ == '__main__':
    print_hi('PyCharm')

