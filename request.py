import requests

def check_user_input(input):
    try:
        value = int(input)
        return value
    except ValueError:
        print("Please enter correct number")


BASE_URL = "http://127.0.0.1:5000/"

print("\nPlease, choose one of the options:")
print("1. Checking the status in the shop")
print("2. Buying products")
item_of_menu_input = input()
item_of_menu = check_user_input(item_of_menu_input)


if item_of_menu == 1:
    response = requests.get(BASE_URL)
    data = response.json()
    print()
    print("{:<4} {:<12} {:<5}".format("ID", "NAME", "QUANTITY"))
    for i in data:
        print("{:<4} {:<12} {:<5}".format(i["id"], i["product"], i["remaining_quantity"]))
    print()

elif item_of_menu == 2:
    response = requests.post(BASE_URL)
    data = response.text
    print(data)