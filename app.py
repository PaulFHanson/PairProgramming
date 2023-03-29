from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)


book_list = [
    {"Title": "Hobbit", "Author": "J.R.R Tolken", "Pages" : "450", "Classification": "Fiction", "Details": "I bought it"}
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", books=book_list
    )


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        title = form["btitle"]
        author = form["author"]
        pages = form["pages"]
        classification = form["classification"]
        details = form.getlist("details")

        print(title)
        print(author)
        print(pages)
        print(classification)
        print(details)

        details_string = ", ".join(details)


        book_dict = {
            "title": title,
            "author": author,
            "pages": pages,
            "classification": classification,
            "details": details_string
        }

        print(book_dict)
        book_list.append(
            book_dict
        ) 
        print(book_dict)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))

@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
