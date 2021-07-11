from flask import Flask, render_template
app = Flask(__name__)


#1. render three blue boxes
@app.route('/play')
def make_three_boxes(boxes = 3):
    return render_template('index.html', boxes = boxes)

# 2. render boxes from integer input
@app.route('/play/<int:x>')
def make_x_boxes(x):
    if x > 0 and x < 40:
        for j in range (1, x):
            boxes = int(x)
            boxes += x 
            return render_template('index.html', boxes = boxes)

# 3. render boxes with int and color input
@app.route('/play/<int:x>/<color>')
def make_color_boxes(x, color):
    if x > 0 and x < 100:
        for j in range (1, x):
            boxes = int(x)
            boxes += x 
            return render_template('index.html', boxes = boxes, classname = "switch", color = str(color))

if __name__=="__main__":
    app.run(debug=True)




# return 


