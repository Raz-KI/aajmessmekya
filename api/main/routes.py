import datetime
from flask import Flask,render_template,redirect,url_for,request
from main import app,db,bcrypt
from main.forms import LoginForm
from main.models import Menu
from flask import flash

dateF=datetime.datetime.now()
dateT = datetime.datetime.now()
dateT = str(dateT.date())
dateF=dateT
dateT = dateT[-2:]
dateT = int(dateT)
dateT=1


@app.route('/')
def hello_world():
    with app.app_context():
        allItems = Menu.query.all()
    return render_template('home.html',allItems=allItems,dateF=dateF,dateT=dateT)

@app.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.uname.data=="Tausif" and form.password.data=="1234567890":
            return redirect(url_for('edit'))
    return render_template('login.html',title='Login',form=form)


@app.route('/edit',methods=['GET','POST','DELETE'])
def edit():
    
    if request.method=="POST":
        date=request.form['date']
        breakfast=request.form['breakfast']
        dinner=request.form['dinner']

        todo=Menu(date=date,breakfast=breakfast,dinner=dinner)
        with app.app_context():
            db.session.add(todo)
            db.session.commit()
        return redirect("/edit")
    with app.app_context():
        allItems = Menu.query.all()
    return render_template('edit.html',allItems=allItems)


# @app.route('/show')
# def products():
#     allItems = Menu.query.all()
#     print(allItems)
#     return render_template('home.html',allItems=allItems,dateT=dateT)

@app.route('/delete/<int:date>')
def delete(date):
    todo = Menu.query.filter_by(date=date).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/edit")

# def add():
#     breakfast=['eggs','puri','dhokala','khaman']
#     dinner=['roti','sabji','kela','amrud']
#     for i in range(len(dinner)):
#         Add = Menu(breakfast=breakfast[i],dinner=dinner[i])
#         with app.app_context():
#             db.session.add(Add)
#             db.session.commit()
@app.route('/menuview')
def viewmenu():
    with app.app_context():
        allItems = Menu.query.all()
    return render_template('menuview.html',allItems=allItems)

if __name__ == "__main__":
    app.run(debug=True) #Shows true error