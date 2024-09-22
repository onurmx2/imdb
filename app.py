from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/fetch_first_link')
def fetch_first_link():
    search_url = "https://www.google.com/search?q=Slingshot%20(2024)%20-%20izle"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(search_url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        first_link = soup.find('a')['href']  # İlk bağlantıyı al
        return jsonify({'first_link': first_link})
    else:
        return jsonify({'error': 'Failed to retrieve search results'}), 500

if __name__ == '__main__':
    app.run(debug=True)
