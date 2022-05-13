import requests, sys

CRED = '\033[91m'
CGREEN = '\033[92m'
CEND = '\033[0m'

BASE_URL = "http://127.0.0.1:5000/"
BUY_PATH = "buy"

menu = [
    "1. Checking the status in the shop",
    "2. Buying products",
    "3. Exit"
]

def check_positive_number(input):
    try:
        value = int(input)
        if value <= 0:
            print("\n" + CRED + "Please, enter correct number" + CEND)
            return
        else:
            return value
    except ValueError:
        print("\n" + CRED + "Please, enter correct number" + CEND)
        return

def print_menu():
    print("\nPlease, choose one of the options:")
    for menu_item in menu:
        print(menu_item)

def select_menu_item():
    item_of_menu_input = input("Your selection: ")
    item_of_menu = check_positive_number(item_of_menu_input)
    if item_of_menu == None:
        return
    elif item_of_menu > len(menu):
        print(f"\n{CRED}Please enter number from 1 to {len(menu)}{CEND}")
    return item_of_menu

def print_data(data):
    for status in ["success", "error"]:
        if status in data and status == "error":
            return print(f"{CRED}{data['error']}{CEND}")
        if status in data and status == "success":
            return print(f"{CGREEN}{data['success']}{CEND}")
    table_format = "{:<4} {:<12} {:<5}"
    print(table_format.format("ID", "NAME", "QUANTITY"))
    table = ''
    if type(data) == dict:
        table += table_format.format(data["id"], data["product"], 
                                     data["current_amount"]) \
                                     + "\n"
    elif type(data) == list:
        for i in data:
            table += table_format.format(i["id"], i["product"], 
                                         i["current_amount"]) \
                                         + "\n"
    return print(table)

def request(selection):
    if selection == 1:
        response = requests.get(BASE_URL)
        data = response.json()
        print()
        print_data(data)
    elif selection == 2:
        product_id_input = input("\nEnter id of the product: ")
        product_id = check_positive_number(product_id_input)
        if product_id == None:
            return
        buy_product_amount_input = input("\nEnter an amount of the " 
                                   + "product you want to buy: ")
        buy_product_amount = check_positive_number(buy_product_amount_input)
        if buy_product_amount == None:
            return

        buy_url = BASE_URL + BUY_PATH + f"/{product_id}"
        request_data = {
            "buy_amount": f"{buy_product_amount}"
        }
        response = requests.patch(buy_url, json=request_data)
        data = response.json()
        print_data(data)


def main():
    print_menu()
    selection = select_menu_item()
    while selection != 3:
        request(selection)
        print_menu()
        selection = select_menu_item()

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('\nInterrupted by user')
        sys.exit()