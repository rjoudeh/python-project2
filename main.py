import os

from flask import Flask, request, jsonify
from flask_api_cache import ApiCache
from sqlalchemy import and_

from db import get_db_session
from user import User

app = Flask(__name__)


@app.route("/", methods=['GET'])
def index():
    return "Hello there, use /users endpoint"


@app.route("/users", methods=['GET'])
@ApiCache(expired_time=50)
def users():
    args = request.args
    max_per_page = 50
    age = args.get("age", "", type=str)
    name = args.get("name", "", type=str)
    page = args.get("page", default=1, type=int)
    per_page = args.get("per_page", default=10, type=int)

    if per_page > max_per_page:
        per_page = max_per_page

    session = get_db_session()
    query = session.query(User)

    queries = []

    if age:
        queries.append(User.age == age)
    if name:
        queries.append(User.name.like(f'{name}%'))

    if len(queries) > 0:
        query = query.filter(and_(*queries))

    response = jsonify(query.offset((page - 1) * per_page).limit(per_page).all())
    response.cache_control.max_age = 500
    return response


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
