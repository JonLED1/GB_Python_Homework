import text

def main_menu() -> int:
    print(text.main_menu)
    while True:
        choice = input(text.input_choice)
        if choice.isdigit() and 0 < int(choice) < 9:
            return int(choice)

def print_book(pb):
    if pb:
        for n in pb:
            print(n)
    else:
        print_message(text.error_) 
        
def print_message(mesage):
    print (mesage)
        
