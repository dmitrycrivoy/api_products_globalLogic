import requests, sys

CRED = '\033[91m'
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
        if status in data:
            return print(data)
    table_format = "{:<4} {:<12} {:<5}"
    print(table_format.format("ID", "NAME", "QUANTITY"))
    table = ''
    if type(data) == dict:
        table += table_format.format(data["id"], data["product"], 
                                     data["quantity"]) + "\n"
    elif type(data) == list:
        for i in data:
            table += table_format.format(i["id"], i["product"], 
                                         i["quantity"]) + "\n"
    return print(table)

def request(selection):
    if selection == 1:
        response = requests.get(BASE_URL)
        data = response.json()
        print()
        print_data(data)
    elif selection == 2:
        product_id = input("\nEnter id of product: ")
        check_positive_number(product_id)
        buy_product_amount = input("\nEnter an amount of the " 
                                   + "product you want to buy: ")
        check_positive_number(buy_product_amount)

        buy_url = BASE_URL + BUY_PATH
        request_data = {
            "product_id": product_id,
            "buy_amount": f"{buy_product_amount}"
        }
        # headers = {'Content-Type': 'application/json'}
        # response = requests.post(buy_url, headers=headers, json=request_data)
        response = requests.post(buy_url, json=request_data)
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