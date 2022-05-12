import requests, sys

BASE_URL = "http://127.0.0.1:5000/"
BUY_PATH = "buy/"

def check_is_number(input):
    try:
        value = int(input)
        return value
    except ValueError:
        print("Please, enter correct number")
        sys.exit()

def print_menu():
    print("Please, choose one of the options:")
    menu = [
        "1. Checking the status in the shop",
        "2. Buying products"
    ]
    for menu_item in menu:
        print(menu_item)
    item_of_menu_input = input("Your selection: ")
    print(item_of_menu_input)
    item_of_menu = check_is_number(item_of_menu_input)
    if item_of_menu > len(menu):
        print(f"\nPlease enter number from 1 to {len(menu)}")
    return item_of_menu

def print_data(data):
    if "error" in data:
        return print(data)
    else:
        table_format = "{:<4} {:<12} {:<5}"
        print(table_format.format("ID", "NAME", "QUANTITY"))
        table = ''
        if type(data) == dict:
            table += table_format.format(data["id"], data["product"], 
                                            data["remaining_quantity"]) + "\n"
        elif type(data) == list:
            for i in data:
                table += table_format.format(i["id"], i["product"], 
                                            i["remaining_quantity"]) + "\n"
        return print(table)

def request(selection):
    if selection == 1:
        response = requests.get(BASE_URL)
        data = response.json()
        print()
        print_data(data)
        print()
    elif selection == 2:
        product_id = input("\nEnter id of product: ")
        check_is_number(product_id)
        full_url = BASE_URL + BUY_PATH + product_id
        response = requests.post(full_url)
        data = response.json()
        print_data(data)


def main():
    selection = print_menu()
    while True:
        request(selection)
        selection = print_menu()

if __name__ == '__main__':
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print('\nInterrupted by user')
        sys.exit()