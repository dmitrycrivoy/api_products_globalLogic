# API for getting and buying products [GlobalLogic DevOps Academy Test]

## Start app
### 1. Start server
```bash
python3 app.py
```
### 2. Start CLI app for user requests
```bash
python3 request.py
```

## API methods and urls
### Get information about all products [GET]:
```bash
<server_ip:port>
```
### Buy new product by id [PATCH]:
```bash
<server_ip:port>/buy/<id>
```
Requested data [JSON]:
```bash
{
    "buy_amount": <int:product_amount>
}
```

## Unit tests
### 1. Start server
```bash
python3 app.py
```
### 2. Run unit tests
 ```bash
python3 api_test.py
```