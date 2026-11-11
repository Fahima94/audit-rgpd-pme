from flask import Flask, render_template, request, session, redirect, url_for, send_file, jsonify
from questions import QUESTIONS, CATEGORIES
from pdf_report import generate_pdf
import json, os

app = Flask(__name__)
app.secret_key = os.urandom(24)


def compute_scores(answers: dict):
    """Compute global and per-category scores (0-100)."""
    cat_map = {c["id"]: c for c in CATEGORIES}

    cat_totals = {c["id"]: {"max": 0, "got": 0, "weight": c["weight"]} for c in CATEGORIES}
    action_plan = []

    for q in QUESTIONS:
        cid = q["category"]
        max_val = max(opt["value"] for opt in q["options"])
        got_val = int(answers.get(q["id"], 0))

        cat_totals[cid]["max"] += max_val * cat_map[cid]["weight"]
        cat_totals[cid]["got"] += got_val * cat_map[cid]["weight"]

        if got_val < max_val:
            action_plan.append({
                "question": q["text"],
                "recommendation": q["recommendation"],
                "priority": q["priority"],
                "category": cat_map[cid]["label"],
                "category_icon": cat_map[cid]["icon"],
                "score_gap": max_val - got_val,
            })

    category_scores = []
    weighted_total = 0
    weight_sum = 0

    for c in CATEGORIES:
        cid = c["id"]
        t = cat_totals[cid]
        score = round((t["got"] / t["max"] * 100) if t["max"] > 0 else 0)
        category_scores.append({
            "id": cid,
            "label": c["label"],
            "icon": c["icon"],
            "score": score,
        })
        weighted_total += score * c["weight"]
        weight_sum += c["weight"]

    global_score = round(weighted_total / weight_sum) if weight_sum > 0 else 0

    # Sort action plan by priority then score gap
    priority_order = {"haute": 0, "moyenne": 1, "faible": 2}
    action_plan.sort(key=lambda x: (priority_order.get(x["priority"], 2), -x["score_gap"]))

    return global_score, category_scores, action_plan


@app.route("/")
def index():
    session.clear()
    return render_template("index.html")


@app.route("/audit", methods=["GET", "POST"])
def audit():
    if request.method == "POST":
        answers = {}
        for q in QUESTIONS:
            val = request.form.get(q["id"])
            if val is not None:
                answers[q["id"]] = int(val)

        company = request.form.get("company_name", "Mon Entreprise")
        session["answers"] = answers
        session["company_name"] = company
        return redirect(url_for("results"))

    questions_by_cat = {}
    for c in CATEGORIES:
        questions_by_cat[c["id"]] = {
            "label": c["label"],
            "icon": c["icon"],
            "questions": [q for q in QUESTIONS if q["category"] == c["id"]],
        }

    return render_template("audit.html", categories=CATEGORIES, questions_by_cat=questions_by_cat)


@app.route("/results")
def results():
    answers = session.get("answers")
    company = session.get("company_name", "Mon Entreprise")
    if not answers:
        return redirect(url_for("audit"))

    global_score, category_scores, action_plan = compute_scores(answers)
    return render_template(
        "results.html",
        company=company,
        global_score=global_score,
        category_scores=category_scores,
        action_plan=action_plan,
        total_questions=len(QUESTIONS),
        answered=len(answers),
    )


@app.route("/export-pdf")
def export_pdf():
    answers = session.get("answers")
    company = session.get("company_name", "Mon Entreprise")
    if not answers:
        return redirect(url_for("audit"))

    global_score, category_scores, action_plan = compute_scores(answers)
    pdf_buf = generate_pdf(company, global_score, category_scores, action_plan, answers)

    filename = f"audit_rgpd_{company.lower().replace(' ', '_')}.pdf"
    return send_file(pdf_buf, as_attachment=True, download_name=filename, mimetype="application/pdf")


@app.route("/restart")
def restart():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=os.environ.get("FLASK_DEBUG") == "1", port=int(os.environ.get("PORT", 5000)))
