from flask import Flask
import timers
import healthdata


app = Flask(__name__)

@app.route("/info")
def hello_world():
    return timers.get_health()


#Aktuelles API Problem das Script wird lediglich einmal getriggert und dann nichtmehr bis zum erneutem reload
#Somit wird die Uptime des Servers nicht korrekt angezeigt 

@app.route("/health")
def get_health():
    return healthdata.uptime()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)