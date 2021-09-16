from flask import Flask, request, jsonify

user_list = list()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Flask Crud'


@app.route("/create", methods=['POST'])
def create():
    user_data = request.get_json()
    if len(user_list) == 0:
        user_list.append(user_data)
    else:
        user_id = user_data['userID']
        is_number_have_in_list = True
        for user in user_list:
            if user['userID'] == user_id:
                is_number_have_in_list = False
                return jsonify(message=str(user_id) + " numbered user already exists")
            if is_number_have_in_list:
                user_list.append(user_data)
            return jsonify(result=user_list)


@app.route("/getByUserId/<int:user_id>", methods=['GET'])
def get_by_user_id(user_id: int):
    for user in user_list:
        print(user)
        if user['userID'] == user_id:
            return jsonify(result=user)
    return jsonify(message=str(user_id) + " not found.")


@app.route("/update", methods=['PUT'])
def update():
    user_data_for_update = request.get_json()
    if len(user_list) == 0:
        return jsonify(message="List is empty. For update, you should enter a new user.")
    else:
        user_id = user_data_for_update['userID']
        index = 0
        for user in user_list:
            print(user_id)
            if user['userID'] == user_id:
                user['userName'] = user_data_for_update['userName']
                user['userLastName'] = user_data_for_update['userLastName']
                user_list[index] = user
                break
            index += 1
        return jsonify(result=user_list)


@app.route("/delete/<int:user_id>")
def delete(user_id: int):
    index = 0
    for user in user_list:
        print(user)
        if user['userID'] == user_id:
            user_list.pop(index)
            return jsonify(result=user_list)
        index += 1
    return jsonify(message=str(user_id) + " not found")


@app.route("/users")
def users():
    return jsonify(users=user_list)


if __name__ == '__main__':
    app.run()
