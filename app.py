from flask import Flask, redirect, url_for, request, render_template, session

app = Flask(__name__)

app.secret_key = 'sua_chave_secreta_aqui'

artwork1 = 0
artwork2 = 0
artwork3 = 0
artwork4 = 0
artwork5 = 0
totalVotes = 0

@app.route("/main-page")
def form():
    return render_template("main-page.html")

@app.route("/success", methods=["POST", "GET"])
def success():
    if request.method=="POST" and request.form["vote"]:
        global artwork1
        global artwork2
        global artwork3
        global artwork4
        global artwork5
        global totalVotes
        totalVotes += 1
        vote = request.form["vote"]
        match vote:
            case "artwork1":
                artwork1 += 1
            case "artwork2":
                artwork2 += 1
            case "artwork3":
                artwork3 += 1
            case "artwork4":
                artwork4 += 1
            case "artwork5":
                artwork5 += 1
            case _:
                pass
        session['artwork1'] = artwork1
        session['artwork2'] = artwork2
        session['artwork3'] = artwork3
        session['artwork4'] = artwork4
        session['artwork5'] = artwork5
        return render_template("success-page.html")
    else:
        return redirect(url_for("error"))
    
@app.route("/error")
def error():
    return render_template("error.html")

@app.route("/results", methods=["POST", "GET"])
def results():
    artwork1 = session.get('artwork1', 0)
    artwork2 = session.get('artwork2', 0)
    artwork3 = session.get('artwork3', 0)
    artwork4 = session.get('artwork4', 0)
    artwork5 = session.get('artwork5', 0)
    winner = max(artwork1, artwork2, artwork3, artwork4, artwork5)
    if winner==artwork1:
        winnerName = "artwork1"
    elif winner==artwork2:
        winnerName = "artwork2"
    elif winner==artwork3:
        winnerName = "artwork3"
    elif winner==artwork4:
        winnerName = "artwork4"
    elif winner==artwork5:
        winnerName = "artwork5"
    else:
        winnerName = "undefined"
    return render_template("results.html", artwork1=artwork1, artwork2=artwork2, artwork3=artwork3, artwork4=artwork4, artwork5=artwork5, winner = winnerName)

