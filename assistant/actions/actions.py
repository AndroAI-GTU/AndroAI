# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from rasa_sdk.forms import FormValidationAction
import requests


class ActionCreateApp(Action):

    def name(self) -> str:
        return "action_create_app"

    def run(self, dispatcher, tracker, domain):

        # `is_open_source` slotuna False değerini ata
        dispatcher.utter_message(response="utter_creating_app")
        return [SlotSet("is_open_source", False)]


class ActionCreateOpenSourceApp(Action):

    def name(self) -> str:
        return "action_create_open_source_app"

    def run(self, dispatcher, tracker, domain):

        # `is_open_source` slotuna True değerini atas
        dispatcher.utter_message(response="utter_creating_app")
        return [SlotSet("is_open_source", True)]


class ValidateAndroidAppForm(FormValidationAction):

    def name(self) -> Text:
        return "validate_android_app_form"

    def validate_app_name(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
       
        if slot_value and len(slot_value.strip()) > 0:
            return {"app_name": slot_value}
        
        dispatcher.utter_message(text="App name cannot be empty. Please provide a valid name for the app.")
        return {"app_name": None}

    def validate_activity_names(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
       
        if slot_value and len(slot_value.strip()) > 0:
            # Girilen metni virgül ile böl
            activity_names_list = [name.strip() for name in slot_value.split(',')]

            # Activity nesneleri yerine sadece isimlerin olduğu bir liste döndür
            return {"activity_names": activity_names_list}

        dispatcher.utter_message(text="Activity names cannot be empty. Please provide valid names for the activities.")
        return {"activity_names": None}

    def validate_activity_content_explanations(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        
        if slot_value and len(slot_value.strip()) > 0:
            return {"activity_content_explanations": slot_value}
        
        dispatcher.utter_message(text="Content explanations cannot be empty. Please provide valid content explanations for the activities.")
        return {"activity_content_explanations": None}

    def validate_activity_links(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        
        if slot_value and len(slot_value.strip()) > 0:
            return {"activity_links": slot_value}
        
        dispatcher.utter_message(text="Activity links cannot be empty. Please provide valid links between the activities.")
        return {"activity_links": None}

    def validate_general_explaining(self, slot_value: Any, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> Dict[Text, Any]:
        
        if slot_value and len(slot_value.strip()) > 0:
            return {"general_explaining": slot_value}
        
        dispatcher.utter_message(text="General explanation cannot be empty. Please provide a valid general explanation for the app.")
        return {"general_explaining": None}


class ActionSubmitAppForm(Action):

    def name(self) -> Text:
        return "action_submit_app_form"

    def run(self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Slotlardan veriyi toplayalım
        app_name = tracker.get_slot('app_name')
        activity_names = tracker.get_slot('activity_names')
        activity_contents = tracker.get_slot('activity_content_explanations')
        activity_links = tracker.get_slot('activity_links')
        general_explaining = tracker.get_slot('general_explaining')

        # Gönderilecek form verileri
        form_data = {
            "appName": app_name,
            "activities": [
                {
                    "name": name,
                    "content": content,
                    "links": links
                } for name, content, links in zip(activity_names, activity_contents, activity_links)
            ],
            "generalExplanation": general_explaining,
            "userId": tracker.sender_id  # User ID'yi de ekliyoruz
        }

        # NestJS API'ye POST isteği
        try:
            response = requests.post('http://nest:5000/user/create-app', json=form_data)
            
            if response.status_code == 200:
                dispatcher.utter_message(text="App form successfully submitted to the server.")

            else:
                dispatcher.utter_message(text=f"Failed to submit app form: {response.status_code}")
        
        except Exception as e:
            dispatcher.utter_message(text=f"An error occurred: {str(e)}")

        return []
