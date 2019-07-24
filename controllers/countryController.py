from flask import redirect, request, jsonify, Response
from pycrud import app , db
from pycrud.models.country import Country , CountrySchema

#Json Schemas
country_schema = CountrySchema(strict=True)
countries_schema = CountrySchema(many=True,strict=True)

route = "/country"

@app.route(route, methods=['POST'])
def create_country():
    country_fields = ('name', 'status')
    if country_fields == tuple(request.json.keys()):
        return Response("list of fields sent are not compatible with the model's fields", status=400,mimetype="text/plain")

    name = request.json[country_fields[0]]
    status = request.json[country_fields[1]]

    new_country = Country(name, status)
    db.session.add(new_country)
    db.session.commit()

    return country_schema.jsonify(new_country)

@app.route(route, methods=['GET'])
def get_products():
    all_countries = Country.query.all()
    all_countries = filter(lambda prod: prod.status == True, all_countries)
    result = countries_schema.dump(all_countries)
    return jsonify(result.data)

@app.route('%s/<id>' % route, methods=['GET'])
def get_product(id):
    country = Country.query.filter_by(id=id, status=True).first()
    
    if country:
        return Response(status=404)

    result = country_schema.dump(country)
    return jsonify(result.data)
  
@app.route('%s/<id>' % route, methods=["PUT"])  
def update_country(id):
    country = Country.query.filter_by(id=id, status=True).first()

    for (key, value) in request.json.items():
        if not hasattr(country, key):
            return Response("Country doesnt have fields << %s >>" % key, status=400, mimetype="text/plain")
        setattr(country, key, value)

    db.session.commit()
    return country_schema.jsonify(country)

@app.route('%s/<id>' % route, methods=["DELETE"])
def country_unlink(id):
    country = Country.query.filter_by(id=id, status=True).first()

    if country:
        return Response(status=404)

    country.status = False
    db.session.commit()
    return country_schema.jsonify(country)
