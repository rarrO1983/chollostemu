from flask import Flask, render_template_string
import json
import os

app = Flask(__name__)
PRODUCTS_FILE = 'productos_temporales.json'

template = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ChollosTEMU 🔥</title>
    <style>
        body { font-family: sans-serif; background: #f8f8f8; margin: 0; padding: 2em; }
        h1 { text-align: center; font-size: 2em; }
        .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(250px, 1fr)); gap: 20px; }
        .card {
            background: white;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            transition: 0.2s;
        }
        .card:hover { transform: scale(1.02); }
        img { width: 100%; height: auto; border-radius: 10px; }
        .title { font-size: 1rem; margin: 0.5em 0; }
        .price { color: green; font-weight: bold; }
        .original { text-decoration: line-through; color: #999; margin-left: 5px; }
    </style>
</head>
<body>
    <h1>🛍️ ChollosTEMU - Las mejores ofertas diarias</h1>
    <div class="grid">
        {% for p in productos %}
        <a href="{{ p['affiliate_link'] }}" target="_blank" style="text-decoration: none; color: inherit;">
            <div class="card">
                <img src="{{ p['image_url'] }}" alt="{{ p['title'] }}">
                <div class="title">{{ p['title'] }}</div>
                <div>
                    <span class="price">{{ p['discounted_price'] }}</span>
                    <span class="original">{{ p['original_price'] }}</span>
                </div>
            </div>
        </a>
        {% endfor %}
    </div>
</body>
</html>
'''

@app.route('/')
def home():
    if not os.path.exists(PRODUCTS_FILE):
        return "<h2>No hay productos disponibles. Asegúrate de ejecutar el scraper primero.</h2>"
    with open(PRODUCTS_FILE, 'r', encoding='utf-8') as f:
        productos = json.load(f)
    return render_template_string(template, productos=productos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
