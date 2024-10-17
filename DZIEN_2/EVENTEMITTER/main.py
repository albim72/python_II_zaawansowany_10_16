from event import EventEmitter,NotificationService,Order

event_emitter = EventEmitter()

notification_service = NotificationService(event_emitter)
order = Order(event_emitter)

#złożenie zamówienia
order.place_order(3456)
