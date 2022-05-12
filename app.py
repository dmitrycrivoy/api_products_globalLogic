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

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET', 'POST'])
def products():
    if request.method == 'GET':
        return send_file(JSON_PATH)
    if request.method == 'POST':
        return {"error": "Use GET request instead"}

@app.route('/buy', methods = ['GET', 'POST'])
def product_by_id():
    if request.method == 'GET':
        return {"error": "Use POST request instead"}
    if request.method == 'POST':
        product_id = check_positive_number(request.json["product_id"])
        buy_amount = check_positive_number(request.json["buy_amount"])
        with open(JSON_PATH) as json_file:
            data = json.load(json_file)
            product_by_id = ''
            for product in data:
                if product["id"] == int(product_id):
                    product_by_id = product
            if not product_by_id:
                return {"error": "No product by id"}
            else:
                if product_by_id["quantity"] >= int(buy_amount):
                    product_by_id["quantity"] -= int(buy_amount)
                    with open(JSON_PATH, 'w') as json_file:
                        json.dump(data, json_file, indent=4)
                    return {
                        "success": 
                        f'you bought {buy_amount} of "{product_by_id["product"]}"'
                    }
                else:
                    return {
                        "error": 
                        f'Not enough product \""{product_by_id["product"]}"\" in the warehouse'
                    }

if __name__ == '__main__':
    app.run(debug=True)