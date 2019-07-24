from pycrud import db , ma

class Province(db.Model):
    __tablename__ = "province"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60))
    status = db.Column(db.Boolean)

    def __init__(self, name, status):
        self.name = name
        self.status = status

class CountrySchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'status')
