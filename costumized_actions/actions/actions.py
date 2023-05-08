# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
from .api import *


# Set-up the client id and client secret
client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

token = get_token()

class Search_artists_by_artist_Action(Action):
    def name(self) -> Text:
        return "action_get_singer_name_by_singer"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        return [SlotSet("Singer_by_singer", search_artists_by_artist(token, search_for_artist(token, tracker.get_slot("singer_name"))["id"]))]



class Search_songs_by_artist_Action(Action):
    def name(self) -> Text:
        return "action_get_song_name_by_singer"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        return [SlotSet("Song_by_singer", search_songs_by_artist(token, search_for_artist(token, next(tracker.get_latest_entity_values("singer_name")))["id"]))]


""" class Search_albums_by_song_Action(Action):
    def name(self) -> Text:
        return "action_get_album_name_by_song"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        return [SlotSet("Album_by_song", search_albums_by_song(token, search_for_song(token, next(tracker.get_latest_entity_values("song_name")))["id"]))]
 """

class Search_albums_by_artist_Action(Action):
    def name(self) -> Text:
        return "action_get_album_name_by_singer"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        return [SlotSet("Album_by_singer", search_albums_by_artist(token, search_for_artist(token, next(tracker.get_latest_entity_values("singer_name")))["id"]))]


""" class Search_artists_by_song_Action(Action):
    def name(self) -> Text:
        return "action_get_singer_name_by_song"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        return [SlotSet("Singer_by_song", search_artists_by_song(token, search_for_song(token, next(tracker.get_latest_entity_values("song_name")))["id"]))]
 """


""" class Search_songs_by_album_Action(Action):
    def name(self) -> Text:
        return "action_get_song_name_by_album"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        return [SlotSet("Song_by_album", search_songs_by_album(token, search_for_album(token, next(tracker.get_latest_entity_values("album_name")))["id"]))]
 """