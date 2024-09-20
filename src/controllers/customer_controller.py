from flask import Blueprint, current_app, jsonify
from werkzeug.exceptions import BadRequest
from ..factory import get_customer_repository
from .auth import auth


customer_blueprint = Blueprint("customer_blueprint", __name__)

@customer_blueprint.route("/api/v1/customer/interactions/<customer_id>", methods=["GET"])
@auth.login_required
def get_customer_interactions(customer_id):
    """Return number of interactions for particular customer per channel

    Args:
        customer_id int: provide customer_id

    Returns:
        list: customer_id, number of interactions per channel
    """
    try:
        stats_repo = get_customer_repository(current_app.config)
        if customer_id.isdigit() and stats_repo.check_customer_exist(customer_id):
            rows = stats_repo.get_customer_interaction_count(customer_id)
            return jsonify({
                "data": {
                "customer_id": rows[0][0],
                "interactions": [{"channel": row[1], "count": row[2]} for row in rows]
                }
        })
        return jsonify({"message": "customer_Id not valid"}), 404
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500
