from flask import Blueprint, current_app, jsonify
from werkzeug.exceptions import BadRequest
from ..factory import get_statistics_repository
from .auth import auth


stats_blueprint = Blueprint("stats_blueprint", __name__)

@stats_blueprint.route("/api/v1/stats/<table_name>", methods=["GET"])
@auth.login_required
def table_count(table_name):
    """Return the number of rows present in the table

    Args:
        table_name string: provide table name

    Returns:
        int: number of rows in the table
    """
    try:
        stats_repo = get_statistics_repository(current_app.config)
        if stats_repo.check_table_name(table_name):
            row = stats_repo.get_number_of_rows(table_name)
            return jsonify({"message": "Number of Rows", "rows": row}), 200
        return jsonify({"message": "Table not found"}), 404
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500



@stats_blueprint.route("/api/v1/stats/get_interactions/<choose_classifiers>", methods=["GET"])
@auth.login_required
def get_interactions(choose_classifiers):
    stats_repo = get_statistics_repository(current_app.config)
    if stats_repo.check_table_name(choose_classifiers):
        row = stats_repo.get_interaction_count(choose_classifiers)
        return jsonify({"message": f"{choose_classifiers}", "rows": row}), 200
    return jsonify({"message": f"Classfiers {choose_classifiers} not found"}), 404
