
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    result = None
    cheapest = None

    if request.method == 'POST':
        # Get user input
        cpu = int(request.form['cpu'])
        ram = int(request.form['ram'])
        storage = int(request.form['storage'])
        region = request.form['region']
        hours = int(request.form['hours'])

        # Region pricing multiplier
        region_multiplier = {
            "US-East": 1.0,
            "Asia": 1.1,
            "Europe": 1.2
        }

        factor = region_multiplier[region]

        # Cost calculations
        aws_cost = ((cpu * 8 + ram * 2 + storage * 0.1) * factor * hours) / 720
        azure_cost = ((cpu * 9 + ram * 2.2 + storage * 0.12) * factor * hours) / 720
        gcp_cost = ((cpu * 7.5 + ram * 1.8 + storage * 0.09) * factor * hours) / 720




       

        # Store results
        result = {
            "AWS": round(aws_cost, 2),
            "Azure": round(azure_cost, 2),
            "GCP": round(gcp_cost, 2)
        }

        # Find cheapest provider
        cheapest = min(result, key=result.get)

    return render_template(
        'index.html',
        result=result,
        cheapest=cheapest
    )

if __name__ == '__main__':
    app.run(debug=True)

