from flask import redirect, request, jsonify
from pycrud import app , db
from pycrud.models.country import Country , CountrySchema

#Json Schemas
country_schema = CountrySchema(strict=True)
countries_schema = CountrySchema(many=True,strict=True)

@app.route('/country', methods=['POST'])
def create_country():
    name = request.json['name']
    status = request.json['status']

    new_country = Country(name, status)


    db.session.add(new_country)
    db.session.commit()

    return country_schema.jsonify(new_country)

@app.route('/country', methods=['GET'])
def get_products():
  all_products = Country.query.all()
  result = countries_schema.dump(all_products)
  return jsonify(result.data)

@app.route('/country/<id>', methods=['GET'])
def get_product(id):
  product = Country.query.get(id)
  result = country_schema.dump(product)
  return jsonify(result.data)