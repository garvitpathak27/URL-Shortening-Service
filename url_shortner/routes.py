from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from models import create_url, get_url_short_code, update_url, delete_url, increment_access_count, get_url_statistics
from utils import generate_random_code

routes = Blueprint('routes', __name__)

@routes.route('/')
def home():
    return render_template('index.html')  # Serve the frontend HTML

@routes.route('/shorten', methods=['POST'])
def shorten_url():
    """Endpoint to create a shortened URL."""
    data = request.form  # Handle form data from frontend (not JSON)
    original_url = data.get('url')  # Get URL from the form input
    if not original_url:
        return jsonify({"error": "URL is required"}), 400

    short_code = generate_random_code()
    url_data = create_url(original_url, short_code)

    # Construct the full short URL to be returned
    short_url = f"http://127.0.0.1:5000/{short_code}"

    # Return the response with the original URL and the shortened URL
    url_data['short_url'] = short_url
    return jsonify(url_data), 201

@routes.route('/<short_code>', methods=['GET'])
def redirect_to_url(short_code):
    """Redirect user to the original URL for the short code."""
    url_data = get_url_short_code(short_code)
    if not url_data:
        return jsonify({"error": "Short URL not found"}), 404

    increment_access_count(short_code)
    return redirect(url_data['url'])  # Redirect to the original URL

@routes.route('/shorten/<short_code>', methods=['PUT'])
def update_short_url(short_code):
    """Update an existing short URL."""
    data = request.json
    new_url = data.get('url')
    if not new_url:
        return jsonify({"error": "URL is required"}), 400

    updated_url = update_url(short_code, new_url)
    if not updated_url:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify(updated_url), 200

@routes.route('/shorten/<short_code>', methods=['DELETE'])
def delete_short_url(short_code):
    """Delete a short URL."""
    deleted_count = delete_url(short_code)
    if deleted_count == 0:
        return jsonify({"error": "Short URL not found"}), 404

    return '', 204

@routes.route('/shorten/<short_code>/stats', methods=['GET'])
def url_statistics(short_code):
    """Get statistics for a short URL."""
    stats = get_url_statistics(short_code)
    if not stats:
        return jsonify({"error": "Short URL not found"}), 404

    return jsonify(stats), 200
