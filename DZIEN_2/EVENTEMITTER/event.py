#rejestr zdarzeń
class EventEmitter:
    def __init__(self):
        self.listeners = {}
        
    def on(self,event:str,listener):
        if event not in self.listeners:
            self.listeners[event]=[]
        self.listeners[event].append(listener)
        
    def emit(self,event:str,*args,**kwargs):
        if event in self.listeners:
            for listener in self.listeners[event]:
                listener(*args,**kwargs)
                
                
#komponent zamówienia
class Order:
    def __init__(self,event_emitter:EventEmitter):
        self.event_emitter = event_emitter
        
    def place_order(self,order_id:int):
        print(f"złożono zamówienie: {order_id}")
        #publikacja zamówinia
        self.event_emitter.emit("order_placed",order_id)
        
#komponent powiadomień
class NotificationService:
    def __init__(self,event_emitter:EventEmitter):
        event_emitter.on("order_placed",self.send_notification)
        
    def send_notification(self,order_id:int):
        print(f"wysłano powiadomienie o złożeniu zamówienia: {order_id}")
