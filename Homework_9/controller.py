import text
import view
import model

def start():
    pb = model.open_pb()
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                view.print_book(pb)
            case 2:
                view.print_message(text.find_text)
                data = model.search_contact(pb)
                view.print_book(data)
            case 3:
                view.print_message(text.change_text)
                data = model.change_cont(pb)
                if data != text.error_:
                    pb[data[1]] = data[0]
                
            case 4:
                view.print_message(text.del_text)
                data = model.del_contact(pb)
                if data != text.error_:
                    pb.pop(data)
            case 5:
                view.print_message(text.add_contact_text)
                data = model.add_contact(pb)
                if data != text.error_:
                    pb.append(data+"\n")
            case 6:
                model.save_pb(pb)
                view.print_message(text.exit_save_text)
                break
            case 7:
                view.print_message(text.exit_text)
                break
