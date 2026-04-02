from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000/"   # Django API


@app.route('/')
def home():
    notes = requests.get(API_URL).json()
    return render_template('index.html', notes=notes)


@app.route('/add', methods=['POST'])
def add():
    text = request.form.get('note')
    requests.post(API_URL, json={"text": text})
    return redirect('/')


# ✅ ADD THIS (DELETE)
@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    requests.delete(f"{API_URL}delete/{id}/")
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)