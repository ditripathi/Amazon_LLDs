#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 17 02:57:45 2024

@author: dinesht
"""

from datetime import datetime

class MeetingRoom:
    def __init__(self, room_id):
        self.room_id = room_id
        self.calendar = {}  # key: datetime, value: meeting details

    def book_meeting(self, start_time, end_time, participants):
        if self.is_available(start_time, end_time):
            meeting_details = {
                'start_time': start_time,
                'end_time': end_time,
                'participants': participants
            }
            self.calendar[start_time] = meeting_details
            print(f"Meeting booked in room {self.room_id} from {start_time} to {end_time}.")
            self.notify(participants)
        else:
            print("Meeting room is not available at that time.")

    def is_available(self, start_time, end_time):
        for booked_start, booked_end in self.calendar.items():
            if start_time < booked_end['end_time'] and end_time > booked_start:
                return False
        return True

    def notify(self, participants):
        print(f"Notifying participants: {participants}")

    def get_history(self):
        return list(self.calendar.values())[:20]


class MeetingScheduler:
    def __init__(self):
        self.meeting_rooms = {}

    def add_meeting_room(self, room_id):
        if room_id not in self.meeting_rooms:
            self.meeting_rooms[room_id] = MeetingRoom(room_id)
            print(f"Meeting room {room_id} added.")
        else:
            print("Meeting room already exists.")

    def book_meeting(self, room_id, start_time, end_time, participants):
        if room_id in self.meeting_rooms:
            self.meeting_rooms[room_id].book_meeting(start_time, end_time, participants)
        else:
            print("Meeting room does not exist.")

    def get_history(self, room_id):
        if room_id in self.meeting_rooms:
            return self.meeting_rooms[room_id].get_history()
        else:
            print("Meeting room does not exist.")
            return []

# Example usage:

scheduler = MeetingScheduler()

# Adding meeting rooms
scheduler.add_meeting_room("Room 1")
scheduler.add_meeting_room("Room 2")

# Booking a meeting
scheduler.book_meeting("Room 1", datetime(2024, 3, 17, 10, 0), datetime(2024, 3, 17, 11, 0), ["Alice", "Bob"])

# Getting history of last 20 booked meetings
history = scheduler.get_history("Room 1")
print("Meeting history:")
for meeting in history:
    print(meeting)
    
    
    '''
    
    Class: MeetingRoomScheduler
        Methods:
            - __init__(self)
            - add_meeting_room(self, room_id)
            - book_meeting(self, room_id, start_time, end_time, participants)
            - get_history(self, room_id)
    
    Class: MeetingRoom
        Methods:
            - __init__(self, room_id)
            - book_meeting(self, start_time, end_time, participants)
            - is_available(self, start_time, end_time)
            - notify(self, participants)
            - get_history(self)
        
        
        '''
  '''      
        LINK: https://leetcode.com/discuss/interview-question/490962/Design-Meeting-Scheduler
        
        Design Meeting Scheduler. Here there are n given meeting rooms. Book a meeting in any meeting room at given interval(starting time, end time). Also send notifications to all person who are invited for meeting.
You should use calender for tracking date and time. And also history of all the meetings which are booked and meeting room.
write an API for client who will give date and time and API should return meeting room with booked scheduled time. client should also query for history of last 20 booked meetings.
Is meeting room available? etc

'''

