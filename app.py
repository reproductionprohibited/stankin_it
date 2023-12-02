import requests

from flask import Flask, render_template

from json_processor import JSONProcessor
from mqtt_processor import MQTTProcessor


app = Flask(__name__)
jsonprocessor = JSONProcessor()
mqttprocessor = MQTTProcessor()


@app.route('/programs/')
def programs():
    context = jsonprocessor.request_programs()
    print('programs: ', context)
    return render_template('programs.html', **context)


@app.route('/details/')
def details():
    context = jsonprocessor.request_details()
    print('details: ', context)
    return render_template('details.html', **context)


@app.route('/schemo/')
def schemo():
    html = requests.get('http://192.168.193.211/')
    html_text = html.text
    data = list(filter(lambda x: x.startswith('<p>'), html_text.split('\n')))[0]
    data = data.replace('<p>', '').replace('</div>', '')
    nums = data.split('</p>')
    print(nums)
    temperature, humidity = nums[:2]
    context = {
        'status': 'success',
        'temperature': temperature,
        'humidity': humidity,
    }
    print('schemo: ', context)
    return render_template('schemo.html', **context)


@app.route('/mqtt/')
def mqtt():
    try:
        mqttprocessor.connect()
        mqttprocessor.receive_data()
        data = mqttprocessor.data
    except:
        data = {'status': 'error', 'temperature': '-', 'humidity': '-'}
    print('mqtt: ', data)
    return render_template('mqtt.html', **data)


if __name__ == '__main__':
    app.run(debug=True)
