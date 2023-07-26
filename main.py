from flask import Flask, render_template, request, redirect, url_for

import requests

app = Flask(__name__)

# Lista de personas
personaList = [{"nombre": "Juan", "apellido": "Perez", "edad": 25},
            {"nombre": "Ana", "apellido": "Gomez", "edad": 30},
            {"nombre": "Carlos", "apellido": "Lopez", "edad": 45}]

#Declarar el API KEY generado de wso2 api manager desde la aplicacion
API_KEY = 'eyJ4NXQiOiJPREUzWTJaaE1UQmpNRE00WlRCbU1qQXlZemxpWVRJMllqUmhZVFpsT0dJeVptVXhOV0UzWVE9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbkBjYXJib24uc3VwZXIiLCJhcHBsaWNhdGlvbiI6eyJvd25lciI6ImFkbWluIiwidGllclF1b3RhVHlwZSI6bnVsbCwidGllciI6IlVubGltaXRlZCIsIm5hbWUiOiJhcHAtYWxleCIsImlkIjo1LCJ1dWlkIjoiYzViZGFiZjAtNzM5ZS00Zjg4LTg1Y2ItNTg4NGJhMzVjNTFiIn0sImlzcyI6Imh0dHBzOlwvXC91dHBsd3NvMi50azo0NDNcL2FwaW1cL29hdXRoMlwvdG9rZW4iLCJ0aWVySW5mbyI6eyJVbmxpbWl0ZWQiOnsidGllclF1b3RhVHlwZSI6InJlcXVlc3RDb3VudCIsImdyYXBoUUxNYXhDb21wbGV4aXR5IjowLCJncmFwaFFMTWF4RGVwdGgiOjAsInN0b3BPblF1b3RhUmVhY2giOnRydWUsInNwaWtlQXJyZXN0TGltaXQiOjAsInNwaWtlQXJyZXN0VW5pdCI6bnVsbH19LCJrZXl0eXBlIjoiU0FOREJPWCIsInN1YnNjcmliZWRBUElzIjpbeyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlV0cGxDbGllbnRlIiwiY29udGV4dCI6IlwvQXBpQ2xpZW50ZVwvMS4wIiwicHVibGlzaGVyIjoiYWRtaW4iLCJ2ZXJzaW9uIjoiMS4wIiwic3Vic2NyaXB0aW9uVGllciI6IlVubGltaXRlZCJ9LHsic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciIsIm5hbWUiOiJVdHBsQ2xpZW50ZSIsImNvbnRleHQiOiJcL0FwaUNsaWVudGVcLzIuMCIsInB1Ymxpc2hlciI6ImFkbWluIiwidmVyc2lvbiI6IjIuMCIsInN1YnNjcmlwdGlvblRpZXIiOiJVbmxpbWl0ZWQifSx7InN1YnNjcmliZXJUZW5hbnREb21haW4iOiJjYXJib24uc3VwZXIiLCJuYW1lIjoiVXRwbFBlcnNvbmFzIiwiY29udGV4dCI6IlwvYXBpcGVyc29uYVwvMy4wIiwicHVibGlzaGVyIjoiYWRtaW4iLCJ2ZXJzaW9uIjoiMy4wIiwic3Vic2NyaXB0aW9uVGllciI6IlVubGltaXRlZCJ9XSwidG9rZW5fdHlwZSI6ImFwaUtleSIsImlhdCI6MTY5MDMzNzg0NywianRpIjoiNzI4MTc5NjYtNzhmMy00ZTNlLWE2NzAtMGI0MDkyYWEwNmZhIn0=.r_KtQR_bsPAgBY1bZG-xhFtkAITJfY7N2QNv3Fk-pvJjkd4eBdgKF5OtAwWRw7O_IirH6W-99yhll55-Bs3YJnigg7PvRojxFwk3UXGOyq7amqhSU1fFlJESmsS5s5cCJVv2F31nfVsMK6wUM9dwnj5byEyRFjhU0OSifOp487RCfSA37DU9gJTHRJubrqHSPBVix6LibY0i3kBU9ncT1duDl_Sf-BFUrrX7981sttLyBURpHHToPqSFdNS0-FnzM2ve8rh8TvtFoGWzSVvTLnbZmr_H1AsjjhZnaw-hA-637Ji5ldOxga37rsFARI7MsZDPE8Haodzf1y1c9qC-uw=='

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
#Este metodo permite obtener personas
@app.route('/personas')
def personas():
    headers = {'apikey': API_KEY}
    response = requests.get('https://utplwso2.tk/apipersona/3.0/personas', headers=headers)
    print(response)
    return render_template('personas.html', personas=response.json())

#Este metodo permite eliminar una persona
@app.route('/personas/delete/<idpersona>')
def delete_personas(idpersona):
    headers = {'apikey': API_KEY}
    response = requests.delete('https://utplwso2.tk/apipersona/3.0/personas/'+idpersona, headers=headers)
    print(response)
    return redirect(url_for('personas'))

#Este metodo permite agregar una persona al api
@app.route('/personas', methods=['POST'])
def add():
    print("llego por aqui a guardar")
    nombre = request.form.get('nombre')
    identificacion = request.form.get('identificacion')
    edad = int(request.form.get('edad'))
    ciudad = request.form.get('ciudad')


    person_data = {"nombre": nombre, "edad": edad, "ciudad": ciudad, "identificacion": identificacion}

    headers = {'apikey': API_KEY}
    responseHabitacionesS = requests.post('https://utplwso2.tk/apipersona/3.0/personas', json=person_data, headers=headers)

    return redirect(url_for('personas'))

#Este metodo permite cargar los clientes desde el api
@app.route('/clientes')
def clientes():
    headers = {'apikey': API_KEY}
    response = requests.get('https://utplwso2.tk/ApiCliente/2.0/cliente', headers=headers)
    print(response.json())
    return render_template('clientes.html', clientes=response.json())

#Este metodo permite agregar una cliente al api
@app.route('/clientes', methods=['POST'])
def addCliente():
    print("llego por aqui a guardar un cliente")
    ciudad = request.form.get('ciudad')
    cantidad = int(request.form.get('cantidad')) 

    cliente_data = { "ciudad": ciudad, "cantPro": cantidad}
    
    headers = {'apikey': API_KEY}
    responseCliente = requests.post('https://utplwso2.tk/ApiCliente/2.0/cliente', json=cliente_data, headers=headers)

    return redirect(url_for('clientes'))


if __name__ == '__main__':
    app.run(debug=True)