import os
import logging
from flask import Flask
from flask_cors import CORS
from config import Config
from .service import SearchService
from .routes import bp as routes_bp, init_routes

def create_app() -> Flask:
    log_level = os.getenv("LOG_LEVEL", "INFO")
    logging.basicConfig(level=getattr(logging, log_level.upper(), logging.INFO))
    logger = logging.getLogger(__name__)

    logger.info("File reading started")
    try:
        search_service = SearchService(Config.DATA_FILE)
        logger.info("File reading completed and data structures prepared")
    except Exception as e:
        logger.error(f"Error reading file: {e}")
        raise RuntimeError("Failed to initialize search service")

    app = Flask(__name__)
    app.config.from_object(Config)
    CORS(app)

    init_routes(search_service)
    app.register_blueprint(routes_bp)

    logger.info("Configuration server completed")

    return app
