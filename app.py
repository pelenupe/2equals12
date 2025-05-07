# Import necessary libraries
from flask import Flask, render_template, request
from markupsafe import Markup
from datetime import datetime, timedelta
from utils import get_fact_by_date, get_tags_from_fact, get_all_categories_and_tags, get_all_quotes
from ai import generate_ai_response
import pytz

# Initialize Flask app
app = Flask(__name__)

# --------------------
# Route: Homepage "/"
# --------------------
# Displays today's Black History Fact or a selected date's fact
@app.route("/")
def index():
    selected_day = request.args.get("day")
    today = datetime.today().date()

    # Parse selected date or fallback to today
    try:
        selected_date = datetime.strptime(selected_day, "%Y-%m-%d").date() if selected_day else today
    except ValueError:
        selected_date = today

    # Prepare dates for navigation
    mm_dd = selected_date.strftime("%m-%d")
    current_date = selected_date.strftime("%Y-%m-%d")
    prev_date = (selected_date - timedelta(days=1)).strftime("%Y-%m-%d")
    next_date = (selected_date + timedelta(days=1)).strftime("%Y-%m-%d")

    # Fetch fact for the selected date
    fact = get_fact_by_date(mm_dd)

    return render_template(
        "index.html",
        fact=fact,
        tags=get_tags_from_fact(fact.get('tags', '')),
        current_date=current_date,
        prev_date=prev_date,
        next_date=next_date
    )
# ------------------------------
# Route: Pass tags to every page for drop down predictive search
# ------------------------------
@app.context_processor
def inject_all_tags():
    categories_tags = get_all_categories_and_tags()

    # Flatten all tags into a single list and deduplicate
    all_tags = []
    for tags in categories_tags.values():
        all_tags.extend(tags)

    return dict(all_tags=sorted(set(all_tags)))


# ------------------------------
# Route: Explore a Tag "/explore/<tag>"
# ------------------------------
# Uses AI to generate additional info based on a selected tag
@app.route("/explore/<tag>")
def explore(tag):
    raw_text = generate_ai_response(tag)
    paragraphs = raw_text.split("\n\n")  # Split into paragraphs for better readability
    formatted = Markup("".join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip()))
    
    return render_template("explore.html", tag=tag, ai_response=formatted)

# --------------------
# Route: About Page "/about"
# --------------------
# Displays static About information
@app.route("/about")
def about():
    return render_template("about.html")

# --------------------
# Route: Topics Page "/topics"
# --------------------
# Displays all searchable tags, sorted alphabetically
@app.route("/topics")
def topics():
    categories_tags = get_all_categories_and_tags()

    # Flatten all tags into a single list and deduplicate
    all_tags = []
    for tags in categories_tags.values():
        all_tags.extend(tags)

    return render_template("topics.html", all_tags=sorted(set(all_tags)))

# --------------------
# Route: Quotes Page "/quotes"
# --------------------
# Displays a motivational quote based on the current month
@app.route("/quotes")
def quotes():
    quotes_list = get_all_quotes()

    # Find the quote that matches the current month
    today = datetime.today()
    current_month = today.strftime("%B")
    try:
        current_index = next(i for i, q in enumerate(quotes_list) if q["month"] == current_month)
    except StopIteration:
        current_index = 0  # fallback to first quote if no match found

    return render_template("quotes.html", quotes=quotes_list, current_index=current_index)

# --------------------
# Run Flask app
# --------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
