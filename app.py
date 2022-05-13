from dis import disco
from json import JSONDecodeError
from flask import Flask, send_file, request, json, jsonify

JSON_PATH = "data.json"

def check_positive_number(input):
    try:
        value = int(input)
        if value <= 0:
            return { "error": "Please, enter correct number"}
        else:
            return value
    except ValueError:
        return { "error": "Please, enter correct number"}

def buy_put_response(product_id, request_data):
    try:
        json_request_data = json.loads(request_data)
        if type(json_request_data) != dict:
            return {"error": "Please, enter data in JSON format"}
        if "buy_amount" in json_request_data:
            buy_amount = check_positive_number(json_request_data["buy_amount"])
            with open(JSON_PATH) as json_file:
                data = json.load(json_file)
                product_by_id = ''
                for product in data:
                    if product["id"] == int(product_id):
                        product_by_id = product
                if not product_by_id:
                    return {"error": "No product by id"}
                else:
                    if product_by_id["current_amount"] >= int(buy_amount):
                        product_by_id["current_amount"] -= int(buy_amount)
                        product_by_id["last_sold"] = int(buy_amount)
                        product_by_id["total_sold"] += int(buy_amount)
                        with open(JSON_PATH, 'w') as json_file:
                            json.dump(data, json_file, indent=4, sort_keys=False)
                        return {
                            "success": 
                            f'You bought {buy_amount} of "{product_by_id["product"]}"'
                        }
                    else:
                        return {
                            "error": 
                            f'Not enough product "{product_by_id["product"]}" in the warehouse'
                        }
        else:
            return {"error": "No 'buy_amount' in request data"}
    except JSONDecodeError:
        return {"error": "Please, enter data in JSON format"}

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET', 'POST', 'PUT'])
def products():
    if request.method == 'GET':
        return send_file(JSON_PATH)
    else:
        return {"error": "Use GET request instead"}

@app.route('/buy/<int:product_id>', methods = ['GET', 'PATCH', 'POST', 'PUT'])
def product_by_id(product_id):
    if request.method == 'PATCH':
        return buy_put_response(product_id, request.data)
    else:
        return {"error": "Use PATCH request instead"}

if __name__ == '__main__':
    app.run(debug=True)