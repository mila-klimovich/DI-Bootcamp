class Phone:
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        who_called_who = f"{other_phone.phone_number} called {self.phone_number}"
        print(who_called_who)
        self.call_history.append(who_called_who)

    def show_call_history(self):
        print(self.call_history)

    def send_message(self, other_phone, content):
        message = {
            "to": self.phone_number,
            "from": other_phone.phone_number,
            "content": content
        }
        self.messages.append(message)

    def show_outgoing_messages(self): 
        for message in self.messages:
            if message["from"] == self.phone_number:
                print(message)
    def show_incoming_messages(self): 
        for message in self.messages:
            if message["to"] == self.phone_number:
                print(message)

    def show_messages_from(self, other_phone):
        for message in self.messages:
            if message["from"] == other_phone.phone_number:
                print(message)

my_phone = Phone('1234567890')
friends_phone = Phone('0987654321')

my_phone.send_message(friends_phone, "TeSTTTTTTTT")
my_phone.send_message(friends_phone, "Hey you")
my_phone.send_message(friends_phone, "wake up")
my_phone.show_outgoing_messages()
friends_phone.show_incoming_messages()
friends_phone.show_messages_from(my_phone)