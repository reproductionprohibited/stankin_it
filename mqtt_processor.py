import paho.mqtt.client as mqtt


class MQTTProcessor:
    def __init__(self):
        self.data = {}

    def connect(self):
        self.data = {}
        def on_connect(client, userdata, flags, rc):
            if rc == 0:
                print('Connected to MQTT Broker!')
            else:
                print(f'Failed to connect, return code {rc}')
                self.data = {'status': 'error', 'temperature': '-', 'humidity': '-'}
                self.client.disconnect()
        def on_message(client, userdata, msg):
            print(f'Received `{msg.payload.decode()}` from `{msg.topic}` topic')
            self.data[msg.topic] = msg.payload.decode()
            if len(self.data) >= 2:
                self.data['temperature'] = self.data['sens/t']
                self.data['humidity'] = self.data['sens/h']
                self.data.__delitem__('sens/h')
                self.data.__delitem__('sens/t')
                self.data['status'] = 'success'
                self.client.disconnect()

        self.client = mqtt.Client(client_id='any')
        self.client.on_connect = on_connect
        self.client.username_pw_set('admin1', '@dm!N')
        self.client.on_message = on_message
        self.client.connect('82.146.60.95', 1883)
        self.client.subscribe('sens/t')
        self.client.subscribe('sens/h')
        return self.client

    def receive_data(self):
        self.client.loop_forever()