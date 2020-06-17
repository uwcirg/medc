from flask_restful import Resource, reqparse
from werkzeug.exceptions import BadRequest


med_multiplier = {
    "codeine": 0.15,
    "fentynl": 2.4,
    "hydrocodone": 1.0,
    "hydromorphone": 4.0,
    "morphine": 1.0,
    "oxycodone": 1.5,
    "oxymorphone": 3.0,
    "tapentodol": 0.367,
    "tramadol": 0.2}


def methadone_calc(value):
    if value == 0:
        return 0
    elif value <= 21:
        return value * 4.0
    elif value <= 41:
        return value * 8.0
    elif value <= 60:
        return value * 10.0
    elif value > 60:
        return value * 12.0


class MEDCalc(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument("codeine")
        parser.add_argument("fentynl")
        parser.add_argument("hydrocodone")
        parser.add_argument("hydromorphone")
        parser.add_argument("methadone")
        parser.add_argument("morphine")
        parser.add_argument("oxycodone")
        parser.add_argument("oxymorphone")
        parser.add_argument("tapentodol")
        parser.add_argument("tramadol")
        args = parser.parse_args(strict=True)

        result = 0
        for med, value in args.items():
            if value is None:
                continue
            try:
                value = float(value)
            except ValueError:
                raise BadRequest(f"Non decimal value {value} given for {med}")

            if med == 'methadone':
                result += methadone_calc(value)
            elif med in med_multiplier:
                result += value * med_multiplier[med]
            else:
                # Per RequestParser docs, won't happen
                raise BadRequest(f"Unexpected med {med}")

        return result, 200
