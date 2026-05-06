from flask import Flask, render_template

app = Flask(__name__)

# Data usaha (Bisa dikembangkan ke database nantinya)
business_info = {
    "name": "TeenVibe Media",
    "description": "Platform kreatif pembuatan konten video edukatif dan blog inspiratif khusus untuk generasi muda.",
    "services": [
        {"title": "Video Editing", "desc": "Edit video cinematic untuk TikTok & YouTube."},
        {"title": "Blogging", "desc": "Penulisan artikel tren remaja terkini."},
        {"title": "Script Writing", "desc": "Pembuatan naskah konten yang engaging."}
    ]
}

@app.route('/')
def index():
    return render_template('index.html', info=business_info)

@app.route('/portfolio')
def portfolio():
    return "Halaman Portfolio (Segera Hadir)"

if __name__ == '__main__':
    app.run(debug=True)
