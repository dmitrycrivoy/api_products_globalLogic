from flask import Flask, send_file, request, json

app = Flask(__name__)

app.config['DEBUG'] = True

@app.route('/', methods = ['GET', 'POST'])
def products():
    if request.method == 'GET':
        return send_file('data.json')
    if request.method == 'POST':
        return "POST RESPONSE"

@app.route('/<product_id>', methods = ['GET', 'POST'])
def product_by_id(product_id):
    if request.method == 'GET':
        with open("data.json") as json_file:
            data = json.load(json_file)
            for product in data:
                if product["id"] == product_id:
                    return product
    if request.method == 'POST':
        return "POST RESPONSE"

if __name__ == '__main__':
    app.run(debug=True)