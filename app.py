import json
from datetime import datetime

from flask import Flask

from live_coding.src.application.controllers.population import \
    ControllerPopulationClimate

app = Flask(__name__)

@app.get("/")
def healthcheck():
    now = datetime.now()
    format_now = now.strftime("%d/%m/%Y %H:%M:%S")
    data_response = json.dumps({ "ok": "liveup", "release": "1.0.0", "date": f"{format_now}"})

    response = app.response_class(
        response=data_response,
        status=200,
        mimetype="application/json"
    )

    app.logger.info({ "healthcheck": "accepted", "ip_origin": "0.0.0.0","date": f"{format_now}"})
    return response

@app.get("/population/<climate>")
def population_climate(climate=None):
    if climate == None:
        return app.response_class(
            response=json.dumps({"error": "bad arguments for request, please check documentation!"}),
            status=400,
            mimetype="application/json"
        )

    controller_data = ControllerPopulationClimate().population_by_climate(app=app, climate=climate)
    print(controller_data)
    if controller_data == []:
        return app.response_class(
            response="No data for climate selected!",
            status=202,
            mimetype="application/json"
        )
    
    return app.response_class(
        response=controller_data,
        status=200,
        mimetype="application/json"
    )

if __name__ == "__main__":
    app.run()