from flask import Flask, render_template, request
from markupsafe import Markup
from datetime import datetime, timedelta
from utils import get_fact_by_date, get_tags_from_fact
from ai import generate_ai_response

app = Flask(__name__)

from datetime import datetime, timedelta

@app.route("/")
def index():
    selected_day = request.args.get("day")
    today = datetime.today().date()

    try:
        selected_date = datetime.strptime(selected_day, "%Y-%m-%d").date() if selected_day else today
    except ValueError:
        selected_date = today

    mm_dd = selected_date.strftime("%m-%d")
    current_date = selected_date.strftime("%Y-%m-%d")
    prev_date = (selected_date - timedelta(days=1)).strftime("%Y-%m-%d")
    next_date = (selected_date + timedelta(days=1)).strftime("%Y-%m-%d")

    fact = get_fact_by_date(mm_dd)  # rotate_index if needed

    return render_template(
        "index.html",
        fact=fact,
        tags=get_tags_from_fact(fact.get('tags', '')),
        current_date=current_date,
        prev_date=prev_date,
        next_date=next_date
    )


@app.route("/explore/<tag>")
def explore(tag):
    raw_text = generate_ai_response(tag)
    paragraphs = raw_text.split("\n\n")  # double newline = new paragraph
    formatted = Markup("".join(f"<p>{p.strip()}</p>" for p in paragraphs if p.strip()))
    return render_template("search.html", tag=tag, ai_response=formatted)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
