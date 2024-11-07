from flask import Flask, render_template, abort


app = Flask(__name__)


projects = [
     {
        "name": "Coding School REST API with Flask, Docker, and SQLAlchemy",
        "thumb": "img/personal-finance.png",
        "hero": "img/personal-finance.png",
        "categories": ["Python", "REST API"],
        "slug": "coding-school",
        "prod": "https://coding-school-api.discoverwitherick.tech/swagger-ui",
        "repo": "https://github.com/kiminzajnr/coding-school-api",
    },
    {
        "name": "Habit tracking app with Python and MongoDB",
        "thumb": "img/habit-tracking.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": "https://habit-tracker.discoverwitherick.tech/",
        "repo": "https://github.com/kiminzajnr/Habit_Tracker",
    },
    {
        "name": "Movie Watchlist with Python and MongoDB",
        "thumb": "img/rest-api-docs.png",
        "hero": "img/habit-tracking-hero.png",
        "categories": ["python", "web", "Databases"],
        "slug": "movie-watchlist",
        "prod": "https://habit-tracker.discoverwitherick.tech/",
        "repo": "https://github.com/kiminzajnr/Movie-Watchlist",
    },
    # {
    #     "name": "REST API with Flask, Docker, and SQLAlchemy",
    #     "thumb": "img/rest-api-docs.png",
    #     "hero": "img/rest-api-docs.png",
    #     "categories": ["Python", "REST API"],
    #     "slug": "know-us-api",
    #      "prod": "https://know-us-rest-api.discoverwitherick.tech/swagger-ui",
    #     "repo": "https://github.com/kiminzajnr/REST-API",
    # }
]


slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(
        f"project_{slug}.html",
        project=slug_to_project[slug]
    )


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404