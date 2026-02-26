from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
pipeline = joblib.load("models/flight_pipeline.pkl")


@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    form_data = {}  # creating a dictionary to store previous inputs

    if request.method == "POST":
        # capture the raw form inputs as strings to send back to the html
        form_data = {
            "Airline": request.form["Airline"],
            "Source": request.form["Source"],
            "Departure Time": request.form["Departure Time"],
            "Stops": request.form["Stops"],
            "Arrival Time": request.form["Arrival Time"],
            "Destination": request.form["Destination"],
            "Class": request.form["Class"],
            "Duration": request.form["Duration"],
            "Days Left": request.form["Days Left"],
        }

        # create a copy and convert types just for the model prediction
        model_input = form_data.copy()
        model_input["Stops"] = int(model_input["Stops"])
        model_input["Duration"] = float(model_input["Duration"])
        model_input["Days Left"] = int(model_input["Days Left"])

        input_df = pd.DataFrame([model_input])
        predicted_price = pipeline.predict(input_df)[0]
        prediction = round(predicted_price, 2)

    # pass both the prediction AND the form_data back to the template
    return render_template("index.html", prediction=prediction, form_data=form_data)


if __name__ == "__main__":
    app.run(debug=True)
