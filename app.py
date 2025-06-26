from flask import Flask
from flask_bootstrap import Bootstrap5
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Create app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/estimates'
app.config['ALLOWED_EXTENSIONS'] = {'pdf', 'png', 'jpg', 'jpeg', 'docx'}
app.secret_key = os.getenv("SECRET_KEY", "dev")

# Extensions
bootstrap = Bootstrap5(app)

# Register Blueprints
from blueprints.main.routes import main_bp
from blueprints.estimate.routes import estimate_bp

app.register_blueprint(main_bp)
app.register_blueprint(estimate_bp)

if __name__ == '__main__':
    app.run(debug=True)
