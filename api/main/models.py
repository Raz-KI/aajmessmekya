from main import db

class Menu(db.Model):
    date = db.Column(db.Integer, primary_key=True)
    breakfast = db.Column(db.String(20))
    dinner = db.Column(db.String(20))

    def __repr__(self):
        return f"Menu('{self.date}','{self.breakfast}','{self.dinner}')"


