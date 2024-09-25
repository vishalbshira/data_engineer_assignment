from flask import Blueprint, current_app, jsonify
from werkzeug.exceptions import BadRequest
from ..factory import get_repository_factory
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
        repository_factory = get_repository_factory(current_app.config)
        stats_repo = repository_factory.create_statistics_repository()
        if stats_repo.check_table_name(table_name):
            row = stats_repo.get_number_of_rows(table_name)
            return jsonify({"message": "Number of Rows", "rows": row}), 200
        return jsonify({"message": "Table not found"}), 404
    except BadRequest as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": "Internal Server Error"}), 500
