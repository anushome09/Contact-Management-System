from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form.get('email', None)
        category = request.form.get('category', 'Uncategorized')
        
        # Calling the add function
        from utils.crud import add_contact  as db_add_contact
        db_add_contact(name=name, phone=phone, email=email, category=category)
        
        return redirect(url_for('home'))    
    return render_template('add_contact.html')

if __name__ == "__main__":
    app.run(debug=True)