from flask import Flask , render_template , request , jsonify

app = Flask(__name__)

@app.route('/', methods = ['GET' , 'POST'] )
def home_page():
    return render_template('index.html')

@app.route('/math',methods = ['POST'])
def math_operation():
    if (request.method == 'POST'):
        ops = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        if(ops == 'add'):
            res = num1+num2
            result = 'the sum of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)

        if(ops == 'substract'):
            res = num1-num2
            result = 'the substract of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)

        if(ops == 'divide'):
            res = num1/num2
            result = 'the divide of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)

        if(ops == 'multiply'):
            res = num1*num2
            result = 'the multiply of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)

        if(ops == 'log'):
            res = num1/num2
            result = 'the log of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)

        if(ops == 'modulo'):
            res = num1%num2
            result = 'the modulo of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)


        return render_template('result.html', result = result)

## data pass through postman 

@app.route('/postman_data',methods = ['POST'])
def math_operation1():
    if (request.method == 'POST'):
        ops = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])
        if(ops == 'add'):
            res = num1+num2
            result = 'the sum of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)

        if(ops == 'substract'):
            res = num1-num2
            result = 'the substract of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)

        if(ops == 'divide'):
            res = num1/num2
            result = 'the divide of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)

        if(ops == 'multiply'):
            res = num1*num2
            result = 'the multiply of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)

        if(ops == 'log'):
            res = num1/num2
            result = 'the log of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)

        if(ops == 'modulo'):
            res = num1%num2
            result = 'the modulo of   ' +str(num1) + ' and ' + str(num2) + ' is ' +str(res)


        return jsonify(result)





if __name__=="__main__":
    app.run(host="0.0.0.0")
