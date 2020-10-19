# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction
import string
import random


class ActionGetMealCategory(Action):

    def name(self) -> Text:
        return "action_meal_category"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        meal_category = tracker.get_slot("meal_category")
        if meal_category == 'veg_pizza':
            dispatcher.utter_message('pick your pizza- Panner or Farmhouse')
        else:
            dispatcher.utter_message('pick your pizza- Chicken or Pepperoni')

        return []

class PizzaOrderForm(FormAction):

    def name(self) -> Text:

        return "pizza_order_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["pizza_type", "pizza_size"]

    def slot_mappings(self) -> Dict[Text, Any]:
        return {"pizza_type":self.from_entity(entity="pizza_type",
                                             intent=["select_pizza"]),
                "pizza_size":self.from_entity(entity="size",
                                              intent=["pizza_size"])}
    
    def submit(self,
               dispatcher: CollectingDispatcher,
               tracker: Tracker,
               domain: Dict[Text, Any]) -> List[Dict]:

        # meal_category = tracker.get_slot('meal_category')
        pizza = tracker.get_slot('pizza_type')
        size = tracker.get_slot('pizza')

        dispatcher.utter_message(f'your order is 1 {size} {pizza} pizza')
        
        return []

class CustomerDetailsForm(FormAction):

    def name(self) -> Text:
        return "customer_details_form"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        return ["customer_name", "address", "pincode", "phone_number"]

    def slot_mappings(self) -> Dict[Text, Any]: 
        return {
            "customer_name":self.from_entity(entity="customer_name", intent=["customer_info"]),
            "address":self.from_entity(entity="address", intent=["customer_info"]),
            "pincode":self.from_entity(entity="pincode", intent=["customer_info"]),
            "phone_number":self.from_entity(entity="phone_number", intent=["customer_info"])
        }

    def submit(self, dispatcher: CollectingDispatcher, tracker: Tracker, 
               domain: Dict[Text, Any]) -> List[Dict]:
        
        cust_name = tracker.get_slot('customer_name')
        cust_address = tracker.get_slot('address')
        cust_pincode = tracker.get_slot('pincode')
        cust_phone = tracker.get_slot('phone_number')

        dispatcher.utter_message(f'your address is: \n {cust_name} \n {cust_address} \n {cust_pincode} \n phone:{cust_phone}')

        return []


class ActionPlaceOrder(Action):

    def name(self) -> Text:
        return "action_place_order"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        pizza = tracker.get_slot("pizza_type")
        size =  tracker.get_slot("pizza_size")
        name = tracker.get_slot("customer_name")
        address = tracker.get_slot("address") +" "+ tracker.get_slot("pincode")
        phone = tracker.get_slot("phone_number")
        order_id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
     
        dispatcher.utter_message(f'your order is confirmed with order id: {order_id}')
    
        return []


class ActionOrderStatus(Action):

    def name(self) -> Text:
        return "action_order_status"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        status = ['CONFIRMED', 'IN KITCHEN', 'DELIVERED']
        dispatcher.utter_message(f'your order status is: {random.choice(status)}')
    
        return []
        
