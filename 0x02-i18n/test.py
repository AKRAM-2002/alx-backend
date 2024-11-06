from flask import Flask, jsonify, request
app = Flask(__name__)

posts = [
    {
        "id": 1,
        "translations": [
            {
                "title": "Title in English",
                "description": "Description in English",
                "locale": "en"
            },
            {
                "title": "Title in Spanish",
                "description": "Description in Spanish",
                "locale": "es"
            },
            {
                "title": "Title in French",
                "description": "Description in French",
                "locale": "fr"
            },
        ]
    }
]

@app.route('/')
def index():
    # Get the first two characters of the Accept-Language header or default to 'en'
    lang = request.headers.get("Accept-Language", 'es')[:2]
    
    # Apply translation to each post using the translate function
    translated_posts = list(map(lambda post: translate(post, lang), posts))
    
    return jsonify(translated_posts)

def translate(post, lang):
    # Find the translation matching the given language (or fallback to 'en' if not found)
    translation = next(t for t in post['translations'] if t['locale'] == lang)
    
    
    if translation:  # If translation exists
            return {
                "id": post['id'],
                "title": translation['title'],
                "description": translation['description']
            }
    else:  # Fallback to default language (English)
        return {
            "id": post['id'],
            "title": post['translations'][0]['title'],
            "description": post['translations'][0]['description']
        }

app.run(debug=True,port=5000)
