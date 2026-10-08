app = Flask(__name__)
os.makedirs("uploads", exist_ok=True)
os.makedirs("templates", exist_ok=True)

current_user = {"username": None, "role": None}

@app.rouhira
    username = email.split("@")[0] if "@" in email else email
    username = username.lower()

    if username in USERS and USERS[username] == password:
        current_user["username"] = username
        current_user["role"] = ROLES[username]
        return jsonify({"success": True, "role": ROLES[username], "user": username})
    else:
        return jsonify({"success": False, "message": "Email ya Password galat hai!"})

@app.route("/upload", methods=["POST"])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file"}), 400
    file = request.files['file']
    filename = secure_filename(file.filename)

    # Cyber Security: Normal user Salary file nahi upload kar sakta
    if current_user["role"] and not check_role(current_user["role"], filename):
        return jsonify({"error": "ACCESS DENIED! Aap normal user ho, Salary files nahi dekh sakte."}), 403

    path = os.path.join("uploads", filename)
    file.save(path)
    encrypt_file(path)
    return jsonify({"success": True, "filename": filename})

@app.route("/ask", methods=["POST"])
def ask():
    q = request.json.get("question","")