from flask import Flask, jsonify, request, make_response
from flask_cors import CORS
import SubwayLoader


loader = SubwayLoader.SubwayLoader()
loader.load_from_file("/Users/bilalwazir/Desktop/v2 harry testing/RouteFinder-Team-Based-Project-Assignment-main/ObjectvilleSubway.txt")
subway = loader.get_subway()

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {
    "origins": "*",
    "allow_headers": ["Content-Type", "Authorization", "Access-Control-Allow-Credentials"],
    "expose_headers": ["Access-Control-Allow-Origin"],
    "supports_credentials": True
}})


@app.route('/route', methods=['GET'])
def get_route():
    start_station = request.args.get('start')
    end_station = request.args.get('end')

    # Find the route
    route = subway.get_directions(start_station, end_station)

    # Convert the route to a list of dictionaries for JSON serialization
    route_dict = [
        {
            "start": connection.get_station1(),
            "end": connection.get_station2(),
            "line": connection.get_line()
        }
        for connection in route
    ]

    response = make_response(jsonify(route_dict))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


@app.route('/stations', methods=['GET'])
def get_stations():
    response = make_response(jsonify(subway.get_all_stations()))
    response.headers['Content-Type'] = 'application/json; charset=utf-8'
    return response


if __name__ == '__main__':
    app.run(debug=True)
