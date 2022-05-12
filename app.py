from flask import Flask, send_file, request, json

JSON_PATH = "data.json"

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/', methods = ['GET', 'POST'])
def products():
    if request.method == 'GET':
        return send_file(JSON_PATH)
    if request.method == 'POST':
        return "POST RESPONSE"

@app.route('/buy/<product_id>', methods = ['GET', 'POST'])
def product_by_id(product_id):
    # if request.method == 'GET':
        # with open(JSON_PATH) as json_file:
        #     data = json.load(json_file)
        #     for product in data:
        #         if product["id"] == product_id:
        #             return product
    if request.method == 'POST':
        with open(JSON_PATH) as json_file:
            data = json.load(json_file)
            product_by_id = ''
            for product in data:
                if product["id"] == int(product_id):
                    product_by_id = product
            if not product_by_id:
                return {"error": "No product by this id"}
            else:
                return product_by_id

if __name__ == '__main__':
    app.run(debug=True)