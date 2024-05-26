from flask import Flask, jsonify
from shapely.geometry import Point, Polygon
import random

app = Flask(__name__)

# Define a more detailed polygon for the boundaries of Paris
paris_boundaries = Polygon([
    (2.224100, 48.815573), (2.229700, 48.817719), (2.235300, 48.819865), (2.240900, 48.822011),
    (2.246500, 48.824157), (2.252100, 48.826303), (2.257700, 48.828449), (2.263300, 48.830595),
    (2.268900, 48.832741), (2.274500, 48.834887), (2.280100, 48.837033), (2.285700, 48.839179),
    (2.291300, 48.841325), (2.296900, 48.843471), (2.302500, 48.845617), (2.308100, 48.847763),
    (2.313700, 48.849909), (2.319300, 48.852055), (2.324900, 48.854201), (2.330500, 48.856347),
    (2.336100, 48.858493), (2.341700, 48.860639), (2.347300, 48.862785), (2.352900, 48.864931),
    (2.358500, 48.867077), (2.364100, 48.869223), (2.369700, 48.871369), (2.375300, 48.873515),
    (2.380900, 48.875661), (2.386500, 48.877807), (2.392100, 48.879953), (2.397700, 48.882099),
    (2.403300, 48.884245), (2.408900, 48.886391), (2.414500, 48.888537), (2.420100, 48.890683),
    (2.425700, 48.892829), (2.431300, 48.894975), (2.436900, 48.897121), (2.442500, 48.899267),
    (2.448100, 48.901413), (2.453700, 48.903559), (2.459300, 48.905705), (2.464900, 48.907851),
    (2.469920, 48.902144),
    (2.469920, 48.815573),
    (2.224199, 48.815573),
    (2.224100, 48.815573)
])

def generate_random_point_within_polygon(polygon):
    min_x, min_y, max_x, max_y = polygon.bounds
    while True:
        random_point = Point(random.uniform(min_x, max_x), random.uniform(min_y, max_y))
        if polygon.contains(random_point):
            return random_point

@app.route('/random-coordinates', methods=['GET'])
def random_coordinates():
    random_point = generate_random_point_within_polygon(paris_boundaries)
    coordinates = {"latitude": random_point.y, "longitude": random_point.x }
    return jsonify(coordinates)

if __name__ == '__main__':
    app.run(debug=True)

