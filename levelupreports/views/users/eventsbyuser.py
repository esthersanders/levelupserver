"""Module for generating games by user report"""
import sqlite3
from django.shortcuts import render
from levelupapi.models import Event, Gamer
from levelupreports.views import Connection


def eventuser_list(request):
    """Function to build an HTML report of events by user"""
    if request.method == 'GET':
        # Connect to project database
        with sqlite3.connect(Connection.db_path) as conn:
            conn.row_factory = sqlite3.Row
            db_cursor = conn.cursor()

            # Query for all games, with related user info.
            db_cursor.execute("""
                SELECT 
                    e.id,
                    e.time,
                    e.description,
                    e.organizer_id,
                    e.date,
                    u.id as user_id,
                    g.title as game_name,
                    u.first_name || ' ' || u.last_name AS full_name
                    FROM levelupapi_event e
                    JOIN levelupapi_gamer o 
                    ON o.id = e.organizer_id
                    JOIN auth_user u on u.id = o.user_id
                    JOIN levelupapi_game g ON g.id = e.game_id;
            """)

            dataset = db_cursor.fetchall()

            # Take the flat data from the database, and build the
            # following data structure for each gamer.
            #
            # {
            #     1: {
            #         "organizer_id": 1,
            #         "full_name": "Molly Ringwald",
            #         "events": [
            #             {
            #                 "id": 5,
            #                 "date": "2020-12-23",
            #                 "time": "19:00",
            #                 "game_name": "Fortress America"
            #             }
            #         ]
            #     }
            # }

            events_by_user = {}

            for row in dataset:
                # Create an event instance and set its properties
                event = Event()
                event.date = row["date"]
                event.time = row["time"]
                event.game_name = row["game_name"]
               

                # Store the user's id
                uid = row["user_id"]

                # If the user's id is already a key in the dictionary...
                if uid in events_by_user:

                    # Add the current event to the `events` list for it
                    events_by_user[uid]['events'].append(event)

                else:
                    # Otherwise, create the key and dictionary value
                    events_by_user[uid] = {}
                    events_by_user[uid]["id"] = uid
                    events_by_user[uid]["full_name"] = row["full_name"]
                    events_by_user[uid]["events"] = [event]

        # Get only the values from the dictionary and create a list from them
        list_of_users_with_events = events_by_user.values()

        # Specify the Django template and provide data context
        template = 'users/list_with_events.html'
        context = {
            'eventuser_list': list_of_users_with_events
        }

        return render(request, template, context)
