from flask import Flask, request, jsonify
from typing import List

index_range = __import__('0-simple_helper_function').index_range

app = Flask(__name__)

# Mock data: imagine these are product records from a database
products = [{"id": i, "name": f"Product {i}"} for i in range(1, 101)]  # 100 products

@app.route("/products", methods=["GET"])
def get_products():
    # Get the page and page size from query parameters (default to 1 and 10)
    page = int(request.args.get("page", 2))
    page_size = int(request.args.get("page_size", 10))

    # Calculate the start and end indices
    start, end = index_range(page, page_size)
    
    # Slice the products data to return only the required subset
    paginated_products = products[start:end]

    return jsonify({
        "page": page,
        "page_size": page_size,
        "data": paginated_products,
        "total_products": len(products)
    })

if __name__ == "__main__":
    app.run()
