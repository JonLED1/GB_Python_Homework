import view, text
path = 'C:/Git/GB_Python_Homework/Homework_9/phone.txt'


def open_pb():
    file_base = open(path, "r", encoding="utf-8")
    data = file_base.readlines()
    file_base.close()
    return data

def search_contact(pb):
    find_date = input()
    search_list = []
    for n in pb:
        if find_date in n:
            search_list.append(n)
    return search_list

def change_cont(pb):
    find_date = input()
    if find_date == "":
        return text.error_
    for n in range(len(pb)):
        if find_date in pb[n]:
            view.print_message(text.find_contact(pb[n]))
            ch_date = input(view.text.new_date_text)
            return [ch_date, n]
        else:
            view.print_message(text.error_)
            return text.error_


def del_contact(pb):
    find_date = input()
    for n in range(len(pb)):
        if find_date in pb[n]:
            view.print_message(text.del_contact(pb[n]))
            if input() == "1":
                return n
    view.print_message(text.error_)
    return text.error_

def add_contact(pb):
    new_contact = input()
    if new_contact == "":
        view.print_message(text.error_)
        return text.error_
    return new_contact
         
def save_pb(pb):
    file_base = open(path, "w", encoding="utf-8")
    for n in pb:
        file_base.write(n)
    file_base.close()