from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from datetime import timedelta

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key"  # змініть на свій секретний ключ
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(hours=1)

jwt = JWTManager(app)

# Проста "база" авто (список словників)
cars = [
    {"id": 1, "make": "Toyota", "model": "Camry", "year": 2018, "price": 20000, "mileage": 30000},
    {"id": 2, "make": "Honda", "model": "Accord", "year": 2020, "price": 25000, "mileage": 20000},
    {"id": 3, "make": "Ford", "model": "Mustang", "year": 2016, "price": 27000, "mileage": 40000},
    {"id": 4, "make": "Tesla", "model": "Model 3", "year": 2021, "price": 45000, "mileage": 10000},
    {"id": 5, "make": "BMW", "model": "X5", "year": 2019, "price": 40000, "mileage": 25000},
    {"id": 6, "make": "Audi", "model": "A4", "year": 2017, "price": 35000, "mileage": 30000},
    # додайте ще авто за потребою
]

# Прості користувачі для аутентифікації
users = {
    "admin": "admin",  # username: password
    "user1": "pass1"
}

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify(msg="Bad username or password"), 401

@app.route("/search", methods=["GET"])
@jwt_required()
def search_cars():
    sort_by = request.args.get("sort_by", "price")
    limit = request.args.get("limit", 5, type=int)

    if sort_by not in ["price", "year", "mileage"]:
        return jsonify(msg="Invalid sort_by parameter"), 400

    sorted_cars = sorted(cars, key=lambda x: x[sort_by])
    limited_cars = sorted_cars[:limit]

    return jsonify(limited_cars)

if __name__ == "__main__":
    app.run(port=8080, debug=True)
