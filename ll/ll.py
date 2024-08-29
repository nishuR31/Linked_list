
from random import *  # randint ka use karenge for random values
from colorama import *


class node:
    def __init__(self, data):
        self.data = data  # ismae main value hoga
        self.next = None  # ismae address hoga next value ka jiska link banega


class linkedList:
    def __init__(self):
        self.head = None  # ye hoga None but point karega starting ko,isko ni hilana  hai

    def display(self):
        try:
            if self.head is None:  # agar head none yahi list empty
                print(f"\n\n {Fore.YELLOW}List is empty{Fore.RESET}")
                return
            current = self.head  # agar entries hai to ek pointer lelo
            print("\n")
            while current:  # jab tak data hai tab tak  print hoag and current ka value next wala address pe jayega
                print(f"{Fore.LIGHTMAGENTA_EX}{current.data}{Fore.RESET}",
                      end=f"{Fore.GREEN}=>{Fore.RESET}")
                current = current.next
            print(f"{Fore.GREEN}None")
        except Exception as e:
            print(
                f"\n\n{Fore.LIGHTRED_EX}Error occured:{Fore.LIGHTRED_EX}{Fore.LIGHTMAGENTA_EX}{e}{Fore.RESET}")
            ask = input(f"\n{Fore.BLUE}Wanna to try again? [y]=> {Fore.RESET}")
            if ask == "y":
                self.display()

    def insertFirst(self):
        while True:
            try:
                data = int(
                    input(f"\n{Fore.BLUE}enter data to insert=> {Fore.RESET}"))
                newNode = node(data)  # naya node with data
                newNode.next = self.head  # node ke address mae none
                self.head = newNode  # head karega node ke value ko refer
                print(
                    f"\n{Fore.LIGHTMAGENTA_EX}{data}{Fore.RESET} inserted in first place.")
                break
            except Exception as e:
                print(
                    f"\n{Fore.LIGHTRED_EX}Error occured:{Fore.LIGHTMAGENTA_EX}{e}{Fore.RESET}")
                ask = input(
                    f"\n{Fore.BLUE}want to try again? [y]=> {Fore.RESET}")
                if ask != "y":
                    break

    def insertLast(self):
        while True:
            try:
                data = int(
                    input(f"\n{Fore.BLUE}enter data to insert=> {Fore.RESET}"))
                newNode = node(data)  # node bana liya with data
                if self.head is None:  # agar list khali
                    newNode.next = self.head  # head yani none ka value node address pe
                    self.head = newNode  # head ka value node ka data
                    print(
                        f"\n{Fore.LIGHTMAGENTA_EX}{data}{Fore.RESET} inserted is first place as no data is present.{Fore.RESET}")
                    break
                current = self.head  # agar data hai to current naam ka pointer lelo
                while current.next:  # jab tak pointer none ni hota yani second last node pe janke rukega loop
                    current = current.next
                # second last ka next address yani last element ka address ,usko new node ka address dekar link bana diya
                current.next = newNode
                print(
                    f"\n{Fore.LIGHTMAGENTA_EX}{data}{Fore.RESET} inserted in last place.{Fore.RESET}")
                break
            except Exception as e:
                print(
                    f"\n{Fore.LIGHTRED_EX}Error occured:{Fore.LIGHTMAGENTA_EX}{e}{Fore.RESET}")
                ask = input(
                    f"\n{Fore.BLUE}want to try again? [y]=> {Fore.RESET}")
                if ask != "y":
                    break

    def insertRandom(self):
        while True:
            try:
                data = int(
                    input(f"\n{Fore.BLUE}enter data to insert=> {Fore.RESET}"))
                newNode = node(data)  # naya node banaya with data
                if self.head is None:  # agar node khali to new node ka address none and head point karega new node ko
                    newNode.next = self.head
                    self.head = newNode
                    print(
                        f"\n{Fore.LIGHTMAGENTA_EX}{data} {Fore.RESET}inserted in random place.{Fore.RESET}")
                    break
                current = self.head  # agar data hai to current pointer banalo
                lenght = 0  # ye lenght store karne ke liye hai
                while current:  # jab tak value hai
                    lenght += 1  # tak tab ye plus hoga aur humko number of values dega ie lenght of whole list
                    # current ko aage wale address pe move karte raho,if none to loop se bahar
                    current = current.next
                # randint se random exclusive number le liya [start,end]
                position = randint(0, lenght)
                # agar 0 hai to wahi new node ke address pe none fir head point to new node
                if position == 0 and self.head.next is None:
                    newNode.next = self.head  # or newNode.next=self.head.data
                    self.head = newNode
                    print(
                        f"\n{Fore.LIGHTMAGENTA_EX}{data}{Fore.RESET} inserted at index {Fore.LIGHTMAGENTA_EX}{position}{Fore.RESET}")
                    break
                else:
                    current = self.head  # agar dusra position hai toh current ka value reset to 1st node
                    # 0 se lekar wo position ho jayega extra to position -1 to reach index of that node
                    for i in range(position-1):
                        # current ko aake barhaya gaya                     previousnode-----x------->laternode
                        current = current.next
                    # current ka jo nexr address hai wo dal diya newnode mae   <-----newnode--->laternode]
                    newNode.next = current.next
                    current.next = newNode  # jo current address tha usmae new node ka address
                    print(
                        f"\n{Fore.LIGHTMAGENTA_EX}{data} {Fore.RESET}inserted at index {Fore.LIGHTMAGENTA_EX}{position}{Fore.RESET}")
                    break
            except Exception as e:
                print(
                    f"\n{Fore.LIGHTRED_EX}Error occured:{Fore.LIGHTMAGENTA_EX}{e}{Fore.RESET}")
                ask = input(
                    f"\n{Fore.BLUE}want to try again? [y]=> {Fore.RESET}")
                if ask != "y":
                    break

    def delFirst(self):
        while True:
            try:
                if self.head is None:
                    print(f"\n{Fore.YELLOW}list is empty{Fore.RESET}")
                    break
                remItem = self.head.data
                self.head = self.head.next
                print(
                    f"\n{Fore.LIGHTMAGENTA_EX}{remItem} removed from first{Fore.RESET}")
                break
            except Exception as e:
                print(
                    f"\n{Fore.LIGHTRED_EX}Error occured:{Fore.LIGHTMAGENTA_EX}{e}{Fore.RESET}")
                ask = input(f"\nwant to try again? [y]=> {Fore.RESET}")
                if ask != "y":
                    break

    def delLast(self):
        while True:
            try:
                if self.head is None:
                    print(f"\n{Fore.YELLOW}list is empty{Fore.RESET}")
                    break
                current = self.head
                if self.head.next is None:
                    remItem = self.head.data
                    self.head = None
                    print(
                        f"\n{Fore.LIGHTMAGENTA_EX}{remItem}{Fore.RESET} removed from start as it\'s the only data{Fore.RESET}")
                    break
                current = self.head
                while current.next.next:
                    current = current.next
                remItem = current.next.data
                current.next = None
                print(
                    f"\n{Fore.LIGHTMAGENTA_EX}{remItem} removed from last{Fore.RESET}")
                break
            except Exception as e:
                print(
                    f"\n{Fore.LIGHTRED_EX}Error occured:{Fore.LIGHTMAGENTA_EX}{e}{Fore.RESET}")
                ask = input(f"\nwant to try again? [y]=> {Fore.RESET}")
                if ask != "y":
                    break

    def delRandom(self):
        while True:
            try:
                if self.head is None:
                    print(f"\n{Fore.YELLOW}list is empty{Fore.RESET}")
                    break

                lenght = 0
                current = self.head
                while current:
                    lenght += 1
                    current = current.next

                position = randint(0, lenght-1)
                if position == 0:
                    remItem = self.head.data
                    self.head = self.head.next
                    print(
                        f"\n{Fore.LIGHTMAGENTA_EX}{remItem}{Fore.RESET} removed from start as it\'s the only data{Fore.RESET}")
                    break
                current = self.head
                for i in range(position-1):
                    current = current.next
                remItem = current.next.data
                current.next = current.next.next
                # current.next.next=None
                print(
                    f"\n{Fore.LIGHTMAGENTA_EX}{remItem}{Fore.RESET} is deleted from random position")
                break
            except Exception as e:
                print(
                    f"\n{Fore.LIGHTRED_EX}Error occured:{Fore.LIGHTMAGENTA_EX}{e}{Fore.RESET}")
                ask = input(
                    f"\{Fore.BLUE}nwant to try again? [y]=> {Fore.RESET}")
                if ask != "y":
                    break

    def search(self):
        while True:
            try:
                if self.head is None:
                    print(f"\n{Fore.YELLOW}list is empty{Fore.RESET}")
                    break
                element = int(
                    input(f"{Fore.BLUE}enter data to search=> {Fore.RESET}"))
                current = self.head
                flag = False
                position = 0
                while current:

                    if current.data == element:
                        flag = True
                        break
                    position += 1
                    current = current.next
                if flag:
                    print(
                        f"\n{Fore.LIGHTMAGENTA_EX}{element} found at index {Fore.LIGHTMAGENTA_EX}{position}{Fore.RESET}")
                    break
            except Exception as e:
                print(
                    f"\n{Fore.LIGHTRED_EX}Error occured:{Fore.LIGHTMAGENTA_EX}{e}{Fore.RESET}")
                ask = input(
                    f"\n{Fore.BLUE}want to try again? [y]=> {Fore.RESET}")
                if ask != "y":
                    break


def menu():
    ll = linkedList()
    while True:
        try:
            insert = int(input(
                f"\n{Fore.LIGHTCYAN_EX}1:{Fore.LIGHTYELLOW_EX}insert at begining\n{Fore.LIGHTCYAN_EX}2:{Fore.LIGHTYELLOW_EX}insert at end\n{Fore.LIGHTCYAN_EX}3:{Fore.LIGHTYELLOW_EX}insert at random\n{Fore.LIGHTCYAN_EX}4:{Fore.LIGHTYELLOW_EX}delete from start\n{Fore.LIGHTCYAN_EX}5:{Fore.LIGHTYELLOW_EX}delete from last\n{Fore.LIGHTCYAN_EX}6:{Fore.LIGHTYELLOW_EX}delete randomly\n{Fore.LIGHTCYAN_EX}7:{Fore.LIGHTYELLOW_EX}display\n{Fore.LIGHTCYAN_EX}8:{Fore.LIGHTYELLOW_EX}search\n{Fore.LIGHTCYAN_EX}0:{Fore.LIGHTYELLOW_EX}exit\n{Fore.LIGHTMAGENTA_EX}enter your choice=> {Fore.RESET}"))
            if insert == 1:
                ll.insertFirst()
            elif insert == 2:
                ll.insertLast()
            elif insert == 3:
                ll.insertRandom()
            elif insert == 4:
                ll.delFirst()
            elif insert == 5:
                ll.delLast()
            elif insert == 6:
                ll.delRandom()
            elif insert == 7:
                ll.display()
            elif insert == 8:
                ll.search()
            elif insert == 0:
                print(f"\n{Fore.LIGHTMAGENTA_EX}Exiting..{Fore.RESET}")
                exit()
            else:
                print(f"\n{Fore.YELLOW}Please enter correct value.{Fore.RESET}")
                continue
        except Exception as e:
            print(
                f"\n{Fore.LIGHTRED_EX}Error occured:{Fore.LIGHTMAGENTA_EX}{e}{Fore.RESET}")
            ask = input(f"\n{Fore.BLUE}want to try again? [y]=> {Fore.RESET}")
            if ask != "y":
                break


menu()
