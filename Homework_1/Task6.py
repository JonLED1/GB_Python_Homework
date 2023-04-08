ticket = input("Введите номер билета: ")
if len(ticket)!=6:
    print ("Это не билет!!!")
    exit()
summ_1 = int(ticket[0])+int(ticket[1])+int(ticket[2])
summ_2 = int(ticket[3])+int(ticket[4])+int(ticket[5])
if summ_1==summ_2:
    print (f"YES!!! Билет номер {ticket} счастливый!")
else:
    print (f"NO!!! Билет номер {ticket} не счастливый!")
