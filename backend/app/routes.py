from flask import Blueprint, jsonify

from flask import Response
from .service import SearchService
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
        index = search_service.search(number)
    except Exception as e:
        logger.exception("Internal error while looking up value: %s", e)
        return jsonify({"error": "Internal error while looking up value"}), 500

    if index is not None:
        logger.info("Found index %d with value %d", index, number )
        return jsonify({"index": index}), 200
    logger.warning("Index not found with value %d", number )
    return jsonify({"error": "error message"}), 404