from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World!'

''' will display integers from 1 to that number '''
@app.route('/<int:number>')
def display_ints(number):
    int_list = list(range(1, number+1)) #O(n)
    return (' '.join(map(str,int_list))) #join() and map() are O(n)

''' will display only odd numbers in that range '''
@app.route('/<int:number>/odd')
def display_odd_ints(number):
    return (' '.join(map(str, [i for i in range(1, number) if i % 2 != 0])))

''' will display only even numbers in that range '''
@app.route('/<int:number>/even')
def display_even_ints(number):
    return (' '.join(map(str, [i for i in range(1, number) if i % 2 == 0])))
 
''' will display only prime numbers in that range '''
@app.route('/<int:number>/prime')
def display_prime_ints(number):
    return (' '.join(map(str, [i for i in range(2, number + 1) if all(i%j != 0 for j in range(2, int(i ** 0.5) + 1))])))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')