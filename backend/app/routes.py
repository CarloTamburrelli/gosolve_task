from flask import Blueprint, jsonify

from flask import Response
from .service import SearchService
from dataclasses import asdict
import logging

bp = Blueprint('routes', __name__)
logger = logging.getLogger(__name__)

search_service = None                                                                   

def init_routes(service: SearchService):
    global search_service
    search_service = service

@bp.route("/endpoint/<int:number>", methods=["GET"])
def search(number) -> tuple[Response, int]:
    try:
        result: SearchResult = search_service.search(number)
    except TypeError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        logger.exception("Internal error while looking up value: %s", e)
        return jsonify({"error": "Internal error while looking up value"}), 500

    if result is not None:
        return jsonify(asdict(result)), 200

    return jsonify({"error": "Value not found"}), 404