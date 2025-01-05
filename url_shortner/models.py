import datetime
from pymongo import MongoClient
from bson import ObjectId  # Import ObjectId to handle it properly

client = MongoClient('mongodb://localhost:27017/')
db = client['url_shortner']
urls_collection = db['urls']

def create_url(original_url, short_code):
    """Insert a new URL document into the database."""
    url_data = {
        "url": original_url,
        "shortCode": short_code,
        "createdAt": datetime.datetime.now(),
        "updatedAt": datetime.datetime.now(),
        "accessCount": 0
    }
    result = urls_collection.insert_one(url_data)
    # Convert ObjectId to string
    url_data["_id"] = str(result.inserted_id)
    return url_data

def get_url_short_code(short_code):
    """Retrieve a URL document by its short code."""
    url_data = urls_collection.find_one({"shortCode": short_code})
    if url_data:
        # Convert ObjectId to string
        url_data["_id"] = str(url_data["_id"])
    return url_data

def update_url(short_code, new_url):
    """Update a URL document by its short code."""
    updated_url = urls_collection.find_one_and_update(
        {"shortCode": short_code},
        {"$set": {"url": new_url, "updatedAt": datetime.datetime.now()}},
        return_document=True
    )
    if updated_url:
        # Convert ObjectId to string
        updated_url["_id"] = str(updated_url["_id"])
    return updated_url

def delete_url(short_code):
    """Delete a URL document by its short code."""
    return urls_collection.delete_one({"shortCode": short_code}).deleted_count

def increment_access_count(short_code):
    """Increment access count for a short code URL."""
    urls_collection.update_one(
        {"shortCode": short_code},
        {"$inc": {"accessCount": 1}}
    )

def get_url_statistics(short_code):
    """Retrieve statistics for a short code."""
    stats = urls_collection.find_one(
        {"shortCode": short_code},
        {"_id": 0}  # Exclude _id field from statistics
    )
    return stats
