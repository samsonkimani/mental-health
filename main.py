from flask import Blueprint, redirect, request

main = Blueprint('main', __name__)

def register_user(first_name, last_name, email, role, password):
    try:
        new_user = User(first_name=first_name, last_name=last_name, email=email, role=role, password=password)
        storage.new(new_user)
        storage.save()
        return True
    except Exception as e:
        print(f"Registration error: {e}")
        return False

@main.route('/register', methods=['POST'])
def register():
    first_name = request.form.get('fname')
    last_name = request.form.get('lname')
    email = request.form.get('email')
    role = request.form.get('role')
    password = request.form.get('password')

    if register_user(first_name, last_name, email, role, password):
        return redirect('/product_page')
    else:
        return redirect('/')
