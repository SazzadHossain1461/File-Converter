from flask import Flask, request, send_file, render_template, jsonify
from PIL import Image
import io
import os
from pathlib import Path

# Use the absolute path of the directory containing this script.
# This ensures Flask can find the HTML files regardless of the current working directory.
BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
app = Flask(__name__, template_folder=BASE_DIR)

# ---------- Serve Pages ----------
# You already had these two, which were correct!
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/jpgtopng')
def jpgtopng_page():
    return render_template('jpgtopng.html')

@app.route('/pngtojpg')
def pngtojpg_page():
    return render_template('pngtojpg.html')

# --- ADDED MISSING PAGE ROUTES ---
# Added these routes to serve your other HTML pages
@app.route('/webptopng')
def webptopng_page():
    return render_template('webptopng.html')

@app.route('/bmptopng')
def bmptopng_page():
    return render_template('bmptopng.html')

@app.route('/pngtopdf')
def pngtopdf_page():
    return render_template('pngtopdf.html')

# ---------- API: JPG → PNG ----------
# This function was correct!
@app.route('/api/jpgtopng', methods=['POST'])
def api_jpgtopng():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    
    try:
        img = Image.open(image_file).convert("RGBA")
    except Exception as e:
        return jsonify({'error': f'Invalid image file: {e}'}), 400

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    return send_file(
        buf,
        mimetype='image/png',
        as_attachment=True,
        download_name=image_file.filename.rsplit('.', 1)[0] + '.png'
    )

# ---------- API: PNG → JPG ----------
# This function was correct!
@app.route('/api/pngtojpg', methods=['POST'])
def api_pngtojpg():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    
    try:
        # Open as RGBA first to handle transparency, then convert to RGB
        img = Image.open(image_file).convert('RGBA')
        
        # Create a white background
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, (0, 0), img) # Paste image on top, using alpha channel as mask
        
        img = background
    except Exception as e:
        return jsonify({'error': f'Invalid image file: {e}'}), 400

    buf = io.BytesIO()
    img.save(buf, format='JPEG', quality=95)
    buf.seek(0)

    return send_file(
        buf,
        mimetype='image/jpeg',
        as_attachment=True,
        download_name=image_file.filename.rsplit('.', 1)[0] + '.jpg'
    )

# --- ADDED MISSING API ROUTES ---

# ---------- API: WEBP → PNG ----------
@app.route('/api/webptopng', methods=['POST'])
def api_webptopng():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    
    try:
        img = Image.open(image_file).convert("RGBA")
    except Exception as e:
        return jsonify({'error': f'Invalid image file: {e}'}), 400

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    return send_file(
        buf,
        mimetype='image/png',
        as_attachment=True,
        download_name=image_file.filename.rsplit('.', 1)[0] + '.png'
    )

# ---------- API: BMP → PNG ----------
@app.route('/api/bmptopng', methods=['POST'])
def api_bmptopng():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    
    try:
        img = Image.open(image_file).convert("RGBA")
    except Exception as e:
        return jsonify({'error': f'Invalid image file: {e}'}), 400

    buf = io.BytesIO()
    img.save(buf, format='PNG')
    buf.seek(0)

    return send_file(
        buf,
        mimetype='image/png',
        as_attachment=True,
        download_name=image_file.filename.rsplit('.', 1)[0] + '.png'
    )

# ---------- API: PNG → PDF ----------
@app.route('/api/pngtopdf', methods=['POST'])
def api_pngtopdf():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    
    try:
        # Convert to 'RGB' because PDF doesn't handle PNG transparency directly
        img = Image.open(image_file).convert('RGB')
    except Exception as e:
        return jsonify({'error': f'Invalid image file: {e}'}), 400

    buf = io.BytesIO()
    img.save(buf, format='PDF', resolution=100.0)
    buf.seek(0)

    return send_file(
        buf,
        mimetype='application/pdf',
        as_attachment=True,
        download_name=image_file.filename.rsplit('.', 1)[0] + '.pdf'
    )

if __name__ == '__main__':
    # Make sure to run on 0.0.0.0 to be accessible
    app.run(host='0.0.0.0', port=5000, debug=True)
