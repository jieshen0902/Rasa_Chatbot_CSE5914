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

SlotSet("song_type", "")
SlotSet("song_name", "")
SlotSet("singer_name", "")
SlotSet("album_name", "")
SlotSet("playlist_name", "")


# three lists
class Search_artists_by_artist_Action(Action):
    SlotSet("singer_name", "")
    def name(self) -> Text:
        return "action_get_singer_name_by_singer"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:

        result = search_artists_by_artist(token, search_for_artist(token, next(tracker.get_latest_entity_values("singer_name")))["id"])
        
        
        return [SlotSet("Singer_by_singer", result[0]), SlotSet("Singer_by_singer_url", result[1]),SlotSet("Singer_by_singer_img", result[2])]
        
class RespondWithCarouselSISI(Action):
    def name(self):
        return "action_respond_with_carousel_SISI"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Singer_by_singer")
        image_url_1 = tracker.get_slot("Singer_by_singer_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Singer_by_singer_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1[0],
                        "subtitle": " ",
                        "image_url": image_url_1[0],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[0],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[1],
                        "subtitle": " ",
                        "image_url": image_url_1[1],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[1],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[2],
                        "subtitle": " ",
                        "image_url": image_url_1[2],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[2],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[3],
                        "subtitle": " ",
                        "image_url": image_url_1[3],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[3],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[4],
                        "subtitle": " ",
                        "image_url": image_url_1[4],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[4],
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []


# three lists
class Search_songs_by_artist_Action(Action):
    SlotSet("singer_name", "")
    def name(self) -> Text:
        return "action_get_song_name_by_singer"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        result = search_songs_by_artist(token, search_for_artist(token, next(tracker.get_latest_entity_values("singer_name")))["id"])
        
        return [SlotSet("Song_by_singer", result[0]), SlotSet("Song_by_singer_url", result[1]), SlotSet("Song_by_singer_img", result[2])]
        

class RespondWithCarouselSOSI(Action):
    def name(self):
        return "action_respond_with_carousel_SOSI"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Song_by_singer")
        image_url_1 = tracker.get_slot("Song_by_singer_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Song_by_singer_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1[0],
                        "subtitle": " ",
                        "image_url": image_url_1[0],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[0],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[1],
                        "subtitle": " ",
                        "image_url": image_url_1[1],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[1],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[2],
                        "subtitle": " ",
                        "image_url": image_url_1[2],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[2],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[3],
                        "subtitle": " ",
                        "image_url": image_url_1[3],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[3],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[4],
                        "subtitle": " ",
                        "image_url": image_url_1[4],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[4],
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []

# 3 text
class Search_albums_by_song_Action(Action):
    SlotSet("song_name", "")
    def name(self) -> Text:
        return "action_get_album_name_by_song"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        result = search_albums_by_song(token, search_for_song(token, next(tracker.get_latest_entity_values("song_name")))["id"])
        return [SlotSet("Album_by_song", result[0]), SlotSet("Album_by_song_url", result[1]), SlotSet("Album_by_song_img", result[2])]
        
class RespondWithCarouselASO(Action):
    def name(self):
        return "action_respond_with_carousel_ASO"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Album_by_song")
        image_url_1 = tracker.get_slot("Album_by_song_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Album_by_song_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1,
                        "subtitle": " ",
                        "image_url": image_url_1,
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1,
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []

# 3 lists
class Search_albums_by_artist_Action(Action):
    SlotSet("singer_name", "")
    def name(self) -> Text:
        return "action_get_album_name_by_singer"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        result = search_albums_by_artist(token, search_for_artist(token, next(tracker.get_latest_entity_values("singer_name")))["id"])
        
        return [SlotSet("Album_by_singer", result[0]), SlotSet("Album_by_singer_url", result[1]), SlotSet("Album_by_singer_img", result[2])]
        
class RespondWithCarouselASI(Action):
    def name(self):
        return "action_respond_with_carousel_ASI"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Album_by_singer")
        image_url_1 = tracker.get_slot("Album_by_singer_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Album_by_singer_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1[0],
                        "subtitle": " ",
                        "image_url": image_url_1[0],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[0],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[1],
                        "subtitle": " ",
                        "image_url": image_url_1[1],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[1],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[2],
                        "subtitle": " ",
                        "image_url": image_url_1[2],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[2],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[3],
                        "subtitle": " ",
                        "image_url": image_url_1[3],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[3],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[4],
                        "subtitle": " ",
                        "image_url": image_url_1[4],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[4],
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []

# 3 lists
class Search_artists_by_song_Action(Action):
    SlotSet("song_name", "")
    def name(self) -> Text:
        return "action_get_singer_name_by_song"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        result = search_artists_by_song(token, search_for_song(token, next(tracker.get_latest_entity_values("song_name")))["id"])
        
        return [SlotSet("Singer_by_song", result[0]), SlotSet("Singer_by_song_url", result[1]), SlotSet("Singer_by_song_img", result[2])]
        
class RespondWithCarouselSISO(Action):
    def name(self):
        return "action_respond_with_carousel_SISO"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Singer_by_song")
        image_url_1 = tracker.get_slot("Singer_by_song_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Singer_by_song_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1[0],
                        "subtitle": " ",
                        "image_url": image_url_1[0],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[0],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[1],
                        "subtitle": " ",
                        "image_url": image_url_1[1],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[1],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[2],
                        "subtitle": " ",
                        "image_url": image_url_1[2],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[2],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[3],
                        "subtitle": " ",
                        "image_url": image_url_1[3],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[3],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[4],
                        "subtitle": " ",
                        "image_url": image_url_1[4],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[4],
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []

#2 lists
class Search_songs_by_album_Action(Action):
    SlotSet("album_name", "")
    def name(self) -> Text:
        return "action_get_song_name_by_album"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        result = search_songs_by_album(token, search_for_album(token, next(tracker.get_latest_entity_values("album_name")))["id"])
        
        return [SlotSet("Song_by_album", result[0]), SlotSet("Song_by_album_url", result[1])]
        
class RespondWithCarouselSOA(Action):
    def name(self):
        return "action_respond_with_carousel_SOA"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Song_by_album")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Song_by_album_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                    "buttons": [ 
                        {
                        "title": "Happy",
                        "payload": "Happy",
                        "type": "postback"
                        },
                        {
                        "title": "sad",
                        "payload": "sad",
                        "type": "postback"
                        }
                    ]
              }
        }
        dispatcher.utter_message(attachment=message)
        return []
        

# 3 lists
class Search_album_Action(Action):
    def name(self) -> Text:
        return "action_get_album"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        result = search_new_release_album(token)
        
        return [SlotSet("New_album", result[0]), SlotSet("New_album_url", result[1]), SlotSet("New_album_img", result[2])]
        
class RespondWithCarouselA(Action):
    def name(self):
        return "action_respond_with_carousel_A"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("New_album")
        image_url_1 = tracker.get_slot("New_album_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("New_album_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1[0],
                        "subtitle": " ",
                        "image_url": image_url_1[0],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[0],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[1],
                        "subtitle": " ",
                        "image_url": image_url_1[1],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[1],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[2],
                        "subtitle": " ",
                        "image_url": image_url_1[2],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[2],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[3],
                        "subtitle": " ",
                        "image_url": image_url_1[3],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[3],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[4],
                        "subtitle": " ",
                        "image_url": image_url_1[4],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[4],
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []
    
# 3 list    
class Search_song_by_all_Action(Action):
    def name(self) -> Text:
        return "action_get_song_by_all"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        artist = search_for_artist(token, next(tracker.get_latest_entity_values("singer_name")))["id"]
        genres = None
        song = search_for_song(token, next(tracker.get_latest_entity_values("song_name")))["id"]
        
        result = get_recommendation(token, artist, genres, song)
        return [SlotSet("Song_name_by_all", result[0]), SlotSet("Song_name_by_all_url", result[1]), SlotSet("Song_name_by_all_img", result[2])]
        
class RespondWithCarouselSOAL(Action):
    def name(self):
        return "action_respond_with_carousel_SOAL"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Song_name_by_all")
        image_url_1 = tracker.get_slot("Song_name_by_all_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Song_name_by_all_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1[0],
                        "subtitle": " ",
                        "image_url": image_url_1[0],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[0],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[1],
                        "subtitle": " ",
                        "image_url": image_url_1[1],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[1],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[2],
                        "subtitle": " ",
                        "image_url": image_url_1[2],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[2],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[3],
                        "subtitle": " ",
                        "image_url": image_url_1[3],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[3],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[4],
                        "subtitle": " ",
                        "image_url": image_url_1[4],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[4],
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []

#3 lists
 
class Search_singers_by_album_Action(Action):
    def name(self) -> Text:
        return "action_get_singer_name_by_album"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        
        result = search_artists_by_album(token,  next(tracker.get_latest_entity_values("album_name")))
        return [SlotSet("Singer_by_album", result[0]), SlotSet("Singer_by_album_url", result[1]), SlotSet("Singer_by_album_img", result[2])]
        
class RespondWithCarouselSIA(Action):
    def name(self):
        return "action_respond_with_carousel_SIA"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Singer_by_album")
        image_url_1 = tracker.get_slot("Singer_by_album_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Singer_by_album_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1[0],
                        "subtitle": " ",
                        "image_url": image_url_1[0],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[0],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[1],
                        "subtitle": " ",
                        "image_url": image_url_1[1],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[1],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[2],
                        "subtitle": " ",
                        "image_url": image_url_1[2],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[2],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[3],
                        "subtitle": " ",
                        "image_url": image_url_1[3],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[3],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[4],
                        "subtitle": " ",
                        "image_url": image_url_1[4],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[4],
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []

#nothing changed
class Search_album_date_Action(Action):
    def name(self) -> Text:
        return "action_get_album_date"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        return [SlotSet("Album_date", release_date_by_album(token,  next(tracker.get_latest_entity_values("album_name"))))]

# 3 lists 
class Search_songs_by_playlist_Action(Action):
    def name(self) -> Text:
        return "action_get_song_name_by_playlist"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        result = search_songs_by_playlist(token, search_for_playlist(token, next(tracker.get_latest_entity_values("playlist_name")))["id"])
        
        return [SlotSet("Song_by_playlist", result[0]), SlotSet("Song_by_playlist_url", result[1]), SlotSet("Song_by_playlist_img", result[2])]

class RespondWithCarouselSOL(Action):
    def name(self):
        return "action_respond_with_carousel_SOL"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Song_by_playlist")
        image_url_1 = tracker.get_slot("Song_by_playlist_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Song_by_playlist_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1[0],
                        "subtitle": " ",
                        "image_url": image_url_1[0],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[0],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[1],
                        "subtitle": " ",
                        "image_url": image_url_1[1],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[1],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[2],
                        "subtitle": " ",
                        "image_url": image_url_1[2],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[2],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[3],
                        "subtitle": " ",
                        "image_url": image_url_1[3],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[3],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[4],
                        "subtitle": " ",
                        "image_url": image_url_1[4],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[4],
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []

# 3 lists
class Search_song_by_song_Action(Action):
    def name(self) -> Text:
        return "action_get_song_name_by_song"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        artist = "None"
        genres = "None"
        song = search_for_song(token, next(tracker.get_latest_entity_values("song_name")))["id"]
        result = get_recommendation(token, artist, genres, song)
        return [SlotSet("Song_by_song", result[0]), SlotSet("Song_by_song_url", result[1]), SlotSet("Song_by_song_img", result[2])]
        
class RespondWithCarouselSOSO(Action):
    def name(self):
        return "action_respond_with_carousel_SOSO"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Song_by_song")
        image_url_1 = tracker.get_slot("Song_by_song_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Song_by_song_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1[0],
                        "subtitle": " ",
                        "image_url": image_url_1[0],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[0],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[1],
                        "subtitle": " ",
                        "image_url": image_url_1[1],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[1],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[2],
                        "subtitle": " ",
                        "image_url": image_url_1[2],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[2],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[3],
                        "subtitle": " ",
                        "image_url": image_url_1[3],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[3],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[4],
                        "subtitle": " ",
                        "image_url": image_url_1[4],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[4],
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []

# 3 lists
class SearchSongByTypeAction(Action):
    def name(self) -> Text:
        return "action_get_song_name_by_type"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        artist = "None"
        genres = next(tracker.get_latest_entity_values("song_type"))
        song = "None"
        result = get_recommendation(token, artist, genres, song)
        return [SlotSet("Song_by_type", result[0]), SlotSet("Song_by_type_url", result[1]), SlotSet("Song_by_type_img", result[2])]
        
class RespondWithCarouselSOT(Action):
    def name(self):
        return "action_respond_with_carousel_SOT"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, any]]:
        # Step 1: Extract the dynamic values from tracker slots or other sources
        title_1 = tracker.get_slot("Song_by_type")
        image_url_1 = tracker.get_slot("Song_by_type_img")
        button_title_1 = "listen"
        button_url_1 = tracker.get_slot("Song_by_type_url")
        message = {
            "type": "template",
            "payload": {
                "template_type": "generic",
                "elements": [
                    {
                        "title": title_1[0],
                        "subtitle": " ",
                        "image_url": image_url_1[0],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[0],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[1],
                        "subtitle": " ",
                        "image_url": image_url_1[1],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[1],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[2],
                        "subtitle": " ",
                        "image_url": image_url_1[2],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[2],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[3],
                        "subtitle": " ",
                        "image_url": image_url_1[3],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[3],
                            "type": "web_url"
                            }
                        ]
                    },
                    {
                        "title": title_1[4],
                        "subtitle": " ",
                        "image_url": image_url_1[4],
                        "buttons": [ 
                            {
                            "title": "Listen",
                            "url": button_url_1[4],
                            "type": "web_url"
                            }
                        ]
                    }
                ]
                }
        }
        dispatcher.utter_message(attachment=message)
        return []

