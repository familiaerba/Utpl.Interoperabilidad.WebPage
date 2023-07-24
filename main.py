from flask import Flask, render_template, request, redirect, url_for

import requests

app = Flask(__name__)

# Lista de personas
personaList = [{"nombre": "Juan", "apellido": "Perez", "edad": 25},
            {"nombre": "Ana", "apellido": "Gomez", "edad": 30},
            {"nombre": "Carlos", "apellido": "Lopez", "edad": 45}]

#Declarar el API KEY generado de wso2 api manager desde la aplicacion
API_KEY = 'eyJ4NXQiOiJPREUzWTJaaE1UQmpNRE00WlRCbU1qQXlZemxpWVRJMllqUmhZVFpsT0dJeVptVXhOV0UzWVE9PSIsImtpZCI6ImdhdGV3YXlfY2VydGlmaWNhdGVfYWxpYXMiLCJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJhZG1pbkBjYXJib24uc3VwZXIiLCJhcHBsaWNhdGlvbiI6eyJvd25lciI6ImFkbWluIiwidGllclF1b3RhVHlwZSI6bnVsbCwidGllciI6IlVubGltaXRlZCIsIm5hbWUiOiJhcHAtYWxleCIsImlkIjo1LCJ1dWlkIjoiYzViZGFiZjAtNzM5ZS00Zjg4LTg1Y2ItNTg4NGJhMzVjNTFiIn0sImlzcyI6Imh0dHBzOlwvXC91dHBsd3NvMi50azo0NDNcL2FwaW1cL29hdXRoMlwvdG9rZW4iLCJ0aWVySW5mbyI6eyJVbmxpbWl0ZWQiOnsidGllclF1b3RhVHlwZSI6InJlcXVlc3RDb3VudCIsImdyYXBoUUxNYXhDb21wbGV4aXR5IjowLCJncmFwaFFMTWF4RGVwdGgiOjAsInN0b3BPblF1b3RhUmVhY2giOnRydWUsInNwaWtlQXJyZXN0TGltaXQiOjAsInNwaWtlQXJyZXN0VW5pdCI6bnVsbH19LCJrZXl0eXBlIjoiU0FOREJPWCIsInN1YnNjcmliZWRBUElzIjpbeyJzdWJzY3JpYmVyVGVuYW50RG9tYWluIjoiY2FyYm9uLnN1cGVyIiwibmFtZSI6IlV0cGxDbGllbnRlIiwiY29udGV4dCI6IlwvQXBpQ2xpZW50ZVwvMS4wIiwicHVibGlzaGVyIjoiYWRtaW4iLCJ2ZXJzaW9uIjoiMS4wIiwic3Vic2NyaXB0aW9uVGllciI6IlVubGltaXRlZCJ9LHsic3Vic2NyaWJlclRlbmFudERvbWFpbiI6ImNhcmJvbi5zdXBlciIsIm5hbWUiOiJVdHBsQ2xpZW50ZSIsImNvbnRleHQiOiJcL0FwaUNsaWVudGVcLzIuMCIsInB1Ymxpc2hlciI6ImFkbWluIiwidmVyc2lvbiI6IjIuMCIsInN1YnNjcmlwdGlvblRpZXIiOiJVbmxpbWl0ZWQifV0sInRva2VuX3R5cGUiOiJhcGlLZXkiLCJpYXQiOjE2ODk5ODY3MzAsImp0aSI6Ijg5MDc0MGVhLTQzMmQtNDk0MS1hNzlhLTE0MWY2MzI3YzQzMyJ9.FJVRpVwvh-mkE44fOynLX9NSmyRpAFxqi02F8cwEyDqBkD3rmM1XFlm9vYKBzZatcquNZzxoGAbSTF-2z4i-OrvFcc0ps1jrs1Y-rE6w3a9S1tVinaZAp8eiGZBePWAkwy_c_r-KYziHk1_qJesEUnAbVEy3pmop1LllpxlF2hXpG_UyoW4-rF80X-ErbA5ROC9RAIZQeFumirBWCNRwjGtslq1qicErOHJFaA31hbF6SSCl6BiKGN1n-4vK1QUtTpMVBxsYOGZQjhBRWsOyX_cUvSqtFpt4z35nVuGMRVtPlFvPDruF-sluq3OR2K0m7ITuTuY3-Ql8bQsojaTthg=='

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/personas')
def personas():
    return render_template('personas.html', personas=personaList)

@app.route('/personas', methods=['POST'])
def add():
    print("llego por aqui a guardar")
    nombre = request.form.get('nombre')
    identificacion = request.form.get('identificacion')
    edad = int(request.form.get('edad'))


person_data = {"nombre": nombre, "edad": edad, "ciudad": ciudad, "identificacion": identificacion}
   
   headers = {'apikey': API_KEY}
    responseHabitacionesS = requests.post('https://utplwso2.tk/ApiCliente/2.0/cliente', json=person_data, headers=headers)
    return redirect(url_for('cliente'))


@app.route('/clientes')
def clientes():
    headers = {'apikey': API_KEY}
    response = requests.get('https://utplwso2.tk/ApiCliente/2.0/cliente', headers=headers)
    print(response)
    return render_template('clientes.html', clientes=response.json())

if __name__ == '__main__':
    app.run(debug=True)