from flask import Flask, redirect, request, render_template, url_for


app = Flask(  # Create a flask app
    __name__,
    template_folder='templates',  # Name of html file folder
    static_folder='static'  # Name of directory for static files
)

# Your code should be below
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/products1')
def product():
    return render_template('product1.html')

#@app.route('/product/2')
#def product2():
  # return render_template('product1.html',name = "football shoes",price = "90")

#@app.route('/product/3')
#def product3():
 #  return render_template('product1.html',name = "shoes",price = "90")


@app.route('/cart')
def cart():
    return render_template('cart.html')




# Your code should be above

if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
