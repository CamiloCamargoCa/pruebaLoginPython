from flask import Flask, render_template
from flask import request
from Cifrado import CifrarCadena
import pymongo
from urllib.parse import quote_plus
import requests


app = Flask(__name__)



@app.route('/login',methods=['GET'])
def formulario():
    return render_template('formulario.html',error=0)



@app.route('/login',methods=['POST'])
def login():
	email = request.form['email']
	password = request.form['password']
	password_cifrado = CifrarCadena(password)
	# print("cifrado",str(password_cifrado.CifrarCaracter()))
	# print('Hola ' + email + ' ' + password_cifrado)

	username = quote_plus('camilo')
	password = quote_plus('sena1234')
	cluster = 'atlascluster.bcdvmcy.mongodb.net'
	authSource = 'admin'
	authMechanism = 'SCRAM-SHA-1'
	uri = 'mongodb+srv://' + username + ':' + password + '@' + cluster + '/?authSource=' + authSource + '&authMechanism=' + authMechanism
	client = pymongo.MongoClient(uri)
	try:
	    client.admin.command('ping')
	    print("Pinged your deployment. You successfully connected to MongoDB!")
	    result = client["importaciones"]["usuari"].find({"correo":email, "clave": str(password_cifrado.CifrarCaracter())})
	    print(result)

	    for i in result:
	    	# return str(i)
	    	return render_template("vista.html",usuario=i, error=0)


	except Exception as e:
		print(e)


	# return 'Usuario no autenticado ' + email + ' ' + str(password_cifrado.CifrarCaracter())
	return render_template("formulario.html",error=1)



@app.route('/consultarimportaciones',methods=['POST'])
def consultarimportaciones():
	# return render_template('formulario.html',error=0)
	return consultarApi()



def consultarApi():
	url = "https://ags.esri.co/arcgis/rest/services/DatosAbiertos/IMPORTACIONES_EXPORTACIONES_2012_2014_DPTO/MapServer/0/query?where=1%3D1&outFields=*&outSR=4326&f=json"
	data = requests.get(url)
	datainfo = data.json()
	# print(datainfo.features)
	for u, value in datainfo['features']:
		print(value)
		# print(u)



	return datainfo





if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8081, debug=True)
