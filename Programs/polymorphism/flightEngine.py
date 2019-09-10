class Flight:
    def __init__(self, engine):
        self.engine = engine
    
    def startEngine(self):
        self.engine.start()
    
class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine.")

class BoingEngine:
    def start(self):
        print("Starting Boing Engine.")

ae = AirbusEngine()
be = BoingEngine()
fae = Flight(ae)
fae.startEngine()
fbe = Flight(be)
fbe.startEngine()

# So this is how we can pass the object dynamically in python.