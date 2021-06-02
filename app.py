from flask import Flask  

app = Flask(__name__)   

@app.route('/')
def home():  
	return "hello world";
@app.route('/index')
def index():
	return "this is index page"
@app.route('/contact/< நண்பர் ')
def contact(value):
	print(val)
	return value,val
	

if __name__ =='__main__':
	val=input("Entr the number:") 
	app.run(debug = True)
