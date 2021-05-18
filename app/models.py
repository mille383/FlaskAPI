from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String)
    location = db.Column(db.String)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        data = {
            'id': self.id,
            'fname': self.fname,
            'location': self.location
        }
        return data

    def from_dict(self, data):
        for attr in ['fname', 'location']:
            if attr in data:
                setattr(self, attr, data[attr])

    # def __repr__(self):
    #     return f'<Product: {self.name} @{self.price}>'