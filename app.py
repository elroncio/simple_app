from flask import Flask  
app = Flask(__name__) 

@app.route('/')   
def main():
    return 'Hello from the DO080 Course!'

@app.route('/whoami')
def whoami():
    return 'This is Extraordy! Visit us at www.extraordy.com!'

if __name__ == '__main__':  # Script executed directly?
    app.run(host="0.0.0.0", port=8080, debug=True,use_reloader=True)  # Launch built-in web server and run this Flask webapp
