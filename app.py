import random
import time
from flask import Flask, render_template, request, jsonify
import feedparser

app = Flask(__name__)

# RSS Feeds
NEWS_FEEDS = {
    "BBC News": "http://feeds.bbci.co.uk/news/rss.xml",
    "CNN": "http://rss.cnn.com/rss/edition.rss",
    "Reuters": "https://www.reutersagency.com/feed/?best-topics=top-news&post_type=best",
    "The New York Times": "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
}

# Category List
CATEGORIES = ["Politics", "Business", "Technology", "Sports", "Health", "Entertainment", "World"]

# Function to fetch RSS feeds with random category assignment (demo purpose)
def get_feeds():
    all_articles = []
    for source, url in NEWS_FEEDS.items():
        feed = feedparser.parse(url)
        for entry in feed.entries[:10]:  # Fetch latest 10 articles per source
            article = {
                "source": source,
                "title": entry.title,
                "link": entry.link,
                "summary": entry.summary if 'summary' in entry else "",
                "published": entry.published if 'published' in entry else "Unknown Date",
                "published_parsed": entry.get('published_parsed', None),  # For sorting
                "category": random.choice(CATEGORIES)  # Demo: Randomly assign category
            }
            all_articles.append(article)
    # Sort articles by published_parsed descending (newest first)
    sorted_articles = sorted(
        all_articles,
        key=lambda x: x['published_parsed'] if x['published_parsed'] else time.gmtime(0),
        reverse=True
    )
    return sorted_articles

@app.route('/')
def index():
    selected_category = request.args.get('category', 'All')
    selected_source = request.args.get('source', 'All')
    search_query = request.args.get('q', '').strip()
    articles = get_feeds()

    # Filter by category if not "All"
    if selected_category != "All":
        articles = [a for a in articles if a["category"] == selected_category]
    # Filter by source if not "All"
    if selected_source != "All":
        articles = [a for a in articles if a["source"] == selected_source]
    # Filter by search query (in title or summary)
    if search_query:
     articles = [
        a for a in articles
        if search_query.casefold() in a["title"].casefold() or search_query.casefold() in a["summary"].casefold()
    ]


    return render_template(
        "index.html",
        categories=CATEGORIES,
        articles=articles,
        selected_category=selected_category,
        selected_source=selected_source,
        news_sources=list(NEWS_FEEDS.keys()),
        search_query=search_query
    )

@app.route('/api/news')
def api_news():
    selected_category = request.args.get('category', 'All')
    selected_source = request.args.get('source', 'All')
    search_query = request.args.get('q', '').strip()
    articles = get_feeds()

    if selected_category != "All":
        articles = [a for a in articles if a["category"] == selected_category]
    if selected_source != "All":
        articles = [a for a in articles if a["source"] == selected_source]
    if search_query:
        articles = [
            a for a in articles
            if search_query.lower() in a["title"].lower() or search_query.lower() in a["summary"].lower()
        ]

    return jsonify(articles)

if __name__ == '__main__':
    app.run(debug=True)
