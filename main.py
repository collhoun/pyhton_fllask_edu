from flask import Flask, render_template

app=Flask(__name__)
lst=['meow','gaff','some']
@app.route('/')
def index():
    return render_template('index.html',title='Мяу')


@app.route('/about')
def about():
    return render_template('about.html',menu=lst)


if __name__=='__main__':
    app.run(debug=True)



