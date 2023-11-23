from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_appliance_cost(units_consumed, appliances):
    total_cost = 0

    appliance_details = []
    for appliance, details in appliances.items():
        appliance_units = float(request.form.get(f"{appliance}_units"))
        appliance_hours = details['hours']
        appliance_cost = (appliance_units / 1000) * appliance_hours * details['rate']
        total_cost += appliance_cost

        appliance_details.append({
            'appliance': appliance,
            'units': appliance_units,
            'hours': appliance_hours,
            'cost': appliance_cost
        })

    return total_cost, appliance_details

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result.html', methods=['POST'])
def calculate_bill():
    units_consumed = float(request.form['total_units'])
    
    appliances = {
        'Refrigerator': {'hours': 24, 'rate': 5.50},
        'Air Conditioner': {'hours': 8, 'rate': 8.00},
        'Washing Machine': {'hours': 2, 'rate': 3.00}
        # Add more appliances and their details as needed
    }

    total_bill, appliance_details = calculate_appliance_cost(units_consumed, appliances)

    return render_template('result.html', units_consumed=units_consumed, total_bill=total_bill, appliance_details=appliance_details)

if __name__ == '__main__':
    app.run(debug=True)
