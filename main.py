from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    shoes = [
        {"name":"Boyii Classic Sneakers", "price":"₦28,000", "image":"https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=400"},
        {"name":"Boyii Running Max", "price":"₦32,000", "image":"https://images.unsplash.com/photo-1606107557195-0e29a4b5b4aa?w=400"},
        {"name":"Boyii Leather Loafers", "price":"₦35,000", "image":"https://images.unsplash.com/photo-1614252369475-531eba835eb1?w=400"},
        {"name":"Boyii Street High", "price":"₦30,000", "image":"https://images.unsplash.com/photo-1551107696-a4b0c5a0d9a2?w=400"},
        {"name":"Boyii Premium Slides", "price":"₦18,000", "image":"https://images.unsplash.com/photo-1603808033192-082d6919d3e1?w=400"},
        {"name":"Boyii Formal Oxford", "price":"₦40,000", "image":"https://images.unsplash.com/photo-1533867617858-e7b97e060509?w=400"},
    ]
    return render_template('index.html', shoes=shoes)

if __name__ == '__main__':
    app.run()
