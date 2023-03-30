from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

friends_dict = [
    {"name": "Test", "flavor": "swirl", "read": "yes", "activities": "reading"}
]

# Route for the homepage
@app.route("/")
def index():
    return render_template("index.html", pageTitle="Web form template", friends=friends_dict)

# Route for adding a new friend
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        # Process the form data and add a new friend to the list
        form = request.form

        fname = form["fname"]
        flavor = form["flavor"]
        read = form["read"]
        activities = form.getlist("activities")

        activities_string = ", ".join(activities)

        friend_dict = {
            "name": fname,
            "flavor": flavor,
            "read": read,
            "activities": activities_string,
        }

        friends_dict.append(friend_dict)

        return redirect(url_for("index"))
    else:
        # Render the form template for GET requests
        return render_template("add.html", pageTitle="Add a new friend")

# Route for the about page
@app.route("/about")
def about():
    return render_template("About.html", pageTitle="About Us")

if __name__ == "__main__":
    app.run(debug=True)
