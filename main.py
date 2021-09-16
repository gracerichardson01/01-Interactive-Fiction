#!/usr/bin/env python3
import sys
assert sys.version_info >= (3,9), "This script requires at least Python 3.9"
world = {
  "uuid": "A43B5555-84B2-49C3-9405-DB929936EBEB",
  "name": "The Late Employee",
  "creator": "Twine",
  "creatorVersion": "2.3.14",
  "schemaName": "Harlowe 3 to JSON",
  "schemaVersion": "0.0.6",
  "createdAtMs": 1631552695174,
  "passages": [
    {
      "name": "Bedroom",
      "tags": "",
      "id": "1",
      "text": "You wake up in a state of fog and turn to your alarm, your alarm didn't go off! Maybe you set it to the wrong time, maybe you set it for P.M. instead of A.M. whatever the reason, your running late for work. Not only that but this is your last straw before you will be fired. You look around and see a few main points of your room, your closet, your bathroom, the door that leads straight to the kitchen and of course, your trusty bed. Where would you like to go?\n\n[[BED->Ending One: Slept In]]\n[[CLOSET->Bedroom Closet]]\n[[BATHROOM->Bathroom]]\n[[DOOR->Kitchen]]",
      "links": [
        {
          "linkText": "BED",
          "passageName": "Ending One: Slept In",
          "original": "[[BED->Ending One: Slept In]]"
        },
        {
          "linkText": "CLOSET",
          "passageName": "Bedroom Closet",
          "original": "[[CLOSET->Bedroom Closet]]"
        },
        {
          "linkText": "BATHROOM",
          "passageName": "Bathroom",
          "original": "[[BATHROOM->Bathroom]]"
        },
        {
          "linkText": "DOOR",
          "passageName": "Kitchen",
          "original": "[[DOOR->Kitchen]]"
        }
      ],
      "hooks": [],
      "cleanText": "You wake up in a state of fog and turn to your alarm, your alarm didn't go off! Maybe you set it to the wrong time, maybe you set it for P.M. instead of A.M. whatever the reason, your running late for work. Not only that but this is your last straw before you will be fired. You look around and see a few main points of your room, your closet, your bathroom, the door that leads straight to the kitchen and of course, your trusty bed. Where would you like to go?"
    },
    {
      "name": "Ending One: Slept In",
      "tags": "",
      "id": "2",
      "text": "You decide to stay in bed and spend the rest of the day sleeping. Although it sounded like a good idea at the time, you ended up getting a call from your boss telling you that you have been fired. Were those extra two hours of sleep worth it?\n\t\t\t\t\t\t\t\tGAME OVER",
      "links": [],
      "hooks": [],
      "cleanText": "You decide to stay in bed and spend the rest of the day sleeping. Although it sounded like a good idea at the time, you ended up getting a call from your boss telling you that you have been fired. Were those extra two hours of sleep worth it?\n\t\t\t\t\t\t\t\tGAME OVER"
    },
    {
      "name": "Bedroom Closet",
      "tags": "",
      "id": "3",
      "text": "You step into the closet to pick out an outfit for the day. You change out of your pajamas as you settle on a green button-up and khakis.You look great! Where would you like to go?\n\n[[LEAVE->Bedroom]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "Bedroom",
          "original": "[[LEAVE->Bedroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "You step into the closet to pick out an outfit for the day. You change out of your pajamas as you settle on a green button-up and khakis.You look great! Where would you like to go?"
    },
    {
      "name": "Bathroom",
      "tags": "",
      "id": "4",
      "text": "You step into the bathroom and start to get ready for the day, you brush your teeth, style your hair, and wash your face. What would you like to do?\n\n[[LEAVE->Bedroom]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "Bedroom",
          "original": "[[LEAVE->Bedroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "You step into the bathroom and start to get ready for the day, you brush your teeth, style your hair, and wash your face. What would you like to do?"
    },
    {
      "name": "Kitchen",
      "tags": "",
      "id": "5",
      "text": "You step into the kitchen and look around. You hear your stomach start rumbling and look around. You could have a bowl of cereal. What would you like to do?\n\n[[LEAVE->Car]]\n[[EAT CEREAL->Kitchen Table]]\n[[GO  BACK TO BEDROOM->Bedroom]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "Car",
          "original": "[[LEAVE->Car]]"
        },
        {
          "linkText": "EAT CEREAL",
          "passageName": "Kitchen Table",
          "original": "[[EAT CEREAL->Kitchen Table]]"
        },
        {
          "linkText": "GO  BACK TO BEDROOM",
          "passageName": "Bedroom",
          "original": "[[GO  BACK TO BEDROOM->Bedroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "You step into the kitchen and look around. You hear your stomach start rumbling and look around. You could have a bowl of cereal. What would you like to do?"
    },
    {
      "name": "Car",
      "tags": "",
      "id": "6",
      "text": "You get into your car and start the engine and head on your way to work. You look around and don't see any other cars on the road. What would you like to do?\n\n[[SPEED->Ending 2: Parking Ticket]]\n[[OBEY THE LAW->Road]]\n[[HOME->Kitchen]]",
      "links": [
        {
          "linkText": "SPEED",
          "passageName": "Ending 2: Parking Ticket",
          "original": "[[SPEED->Ending 2: Parking Ticket]]"
        },
        {
          "linkText": "OBEY THE LAW",
          "passageName": "Road",
          "original": "[[OBEY THE LAW->Road]]"
        },
        {
          "linkText": "HOME",
          "passageName": "Kitchen",
          "original": "[[HOME->Kitchen]]"
        }
      ],
      "hooks": [],
      "cleanText": "You get into your car and start the engine and head on your way to work. You look around and don't see any other cars on the road. What would you like to do?"
    },
    {
      "name": "Kitchen Table",
      "tags": "",
      "id": "7",
      "text": "You pour a bowl of fruity colorful cereal and eat it quickly, it may have lost you a couple of minutes but atleast your stomach isn't making that horrendous noise. What would you like to do?\n\n[[LEAVE->Car]]\n[[BEDROOM->Bedroom]]",
      "links": [
        {
          "linkText": "LEAVE",
          "passageName": "Car",
          "original": "[[LEAVE->Car]]"
        },
        {
          "linkText": "BEDROOM",
          "passageName": "Bedroom",
          "original": "[[BEDROOM->Bedroom]]"
        }
      ],
      "hooks": [],
      "cleanText": "You pour a bowl of fruity colorful cereal and eat it quickly, it may have lost you a couple of minutes but atleast your stomach isn't making that horrendous noise. What would you like to do?"
    },
    {
      "name": "Ending 2: Parking Ticket",
      "tags": "",
      "id": "8",
      "text": "As you speed up you start to see flashing blue and red lights behind you, you couldv'e sworn they came out of nowhere. The police officer informs you that you were going 65 in a 30 and that you were driving recklessly. You are served with a ticket and fail to make it to work on time. Not only did you get fired you now have to pay a fine.\n\t\t\t\t\t\t\t\tGAME OVER",
      "links": [],
      "hooks": [],
      "cleanText": "As you speed up you start to see flashing blue and red lights behind you, you couldv'e sworn they came out of nowhere. The police officer informs you that you were going 65 in a 30 and that you were driving recklessly. You are served with a ticket and fail to make it to work on time. Not only did you get fired you now have to pay a fine.\n\t\t\t\t\t\t\t\tGAME OVER"
    },
    {
      "name": "Road",
      "tags": "",
      "id": "9",
      "text": "Although you could try to go faster, you decide to take the safe route and obey the speed limit. On your way to work you make it to a coffee shop. You are tired but are not sure whether you want to take the time loss or not. Despite that, a caramel machiatto does sound good. What would you like to do?\n\n[[GET COFFEE->Coffee Shop]]\n[[SKIP IT->Road Two]]",
      "links": [
        {
          "linkText": "GET COFFEE",
          "passageName": "Coffee Shop",
          "original": "[[GET COFFEE->Coffee Shop]]"
        },
        {
          "linkText": "SKIP IT",
          "passageName": "Road Two",
          "original": "[[SKIP IT->Road Two]]"
        }
      ],
      "hooks": [],
      "cleanText": "Although you could try to go faster, you decide to take the safe route and obey the speed limit. On your way to work you make it to a coffee shop. You are tired but are not sure whether you want to take the time loss or not. Despite that, a caramel machiatto does sound good. What would you like to do?"
    },
    {
      "name": "Coffee Shop",
      "tags": "",
      "id": "10",
      "text": "You walk into the coffee shop and the aroma of freshly ground coffee hits you. The barista approcahes you and asks for your order, upon telling her she informs you that they do have a cold pot but are brewing a new one now if you are happy to wait a few minutes. What would you like to do?\n\n[[WAIT->Ending Three: Hot Coffee]]\n[[DRINK COLD COFFEE->Order is Ready]]\n[[LEAVE->Road Three]]",
      "links": [
        {
          "linkText": "WAIT",
          "passageName": "Ending Three: Hot Coffee",
          "original": "[[WAIT->Ending Three: Hot Coffee]]"
        },
        {
          "linkText": "DRINK COLD COFFEE",
          "passageName": "Order is Ready",
          "original": "[[DRINK COLD COFFEE->Order is Ready]]"
        },
        {
          "linkText": "LEAVE",
          "passageName": "Road Three",
          "original": "[[LEAVE->Road Three]]"
        }
      ],
      "hooks": [],
      "cleanText": "You walk into the coffee shop and the aroma of freshly ground coffee hits you. The barista approcahes you and asks for your order, upon telling her she informs you that they do have a cold pot but are brewing a new one now if you are happy to wait a few minutes. What would you like to do?"
    },
    {
      "name": "Road Two",
      "tags": "",
      "id": "11",
      "text": "You decide to pass on the coffee and continue to drive. As you drive you can feel your eye shutting and your mind fogging up. Before you know it you have crashed into a small pond. You must have closed your eyes for a little too long. You are okay but your car is done for. Atleast you have a good story to tell. \n\t\t\t\t\t\t\t\tGAME OVER",
      "links": [],
      "hooks": [],
      "cleanText": "You decide to pass on the coffee and continue to drive. As you drive you can feel your eye shutting and your mind fogging up. Before you know it you have crashed into a small pond. You must have closed your eyes for a little too long. You are okay but your car is done for. Atleast you have a good story to tell. \n\t\t\t\t\t\t\t\tGAME OVER"
    },
    {
      "name": "Ending Three: Hot Coffee",
      "tags": "",
      "id": "12",
      "text": "You wait a substancial amount of time for the coffee and when you finally get it it is boiling hot. You pay for it and grab it from the barista. You walk outside only to trip on a crack in the sidewalk spilling the boiling hot coffee all over you, resulting in 3rd degree burns. You spend the rest of your day at the hospital.\n\t\t\t\t\t\t\t\tGAME OVER",
      "links": [],
      "hooks": [],
      "cleanText": "You wait a substancial amount of time for the coffee and when you finally get it it is boiling hot. You pay for it and grab it from the barista. You walk outside only to trip on a crack in the sidewalk spilling the boiling hot coffee all over you, resulting in 3rd degree burns. You spend the rest of your day at the hospital.\n\t\t\t\t\t\t\t\tGAME OVER"
    },
    {
      "name": "Order is Ready",
      "tags": "",
      "id": "13",
      "text": "After paying for the lukewarm drink you leave and get back in your car. The coffee tastes mediocre but atleast it's better than nothing. Now that you feel energized you are ready to get back on the road.\n\n[[DRIVE->Road Three]]",
      "links": [
        {
          "linkText": "DRIVE",
          "passageName": "Road Three",
          "original": "[[DRIVE->Road Three]]"
        }
      ],
      "hooks": [],
      "cleanText": "After paying for the lukewarm drink you leave and get back in your car. The coffee tastes mediocre but atleast it's better than nothing. Now that you feel energized you are ready to get back on the road."
    },
    {
      "name": "Road Three",
      "tags": "",
      "id": "14",
      "text": "You continue to drive when you see a field full of flowers and group of people with long hair, flowing oufits, and crazy sunglasses basking in the sun listening and singing music. Hippies... What would you like to do?\n\n[[DRIVE->Road Four]]\n[[JOIN THEM->Ending 4: Hippies]]",
      "links": [
        {
          "linkText": "DRIVE",
          "passageName": "Road Four",
          "original": "[[DRIVE->Road Four]]"
        },
        {
          "linkText": "JOIN THEM",
          "passageName": "Ending 4: Hippies",
          "original": "[[JOIN THEM->Ending 4: Hippies]]"
        }
      ],
      "hooks": [],
      "cleanText": "You continue to drive when you see a field full of flowers and group of people with long hair, flowing oufits, and crazy sunglasses basking in the sun listening and singing music. Hippies... What would you like to do?"
    },
    {
      "name": "Road Four",
      "tags": "",
      "id": "15",
      "text": "You continue to drive as you chuckle to yourself at the absurdity that you have just passed.You look at the time and start to get worried. While driving on the highwau you see a small cardbox, as you get closer you see a small puppy that has been abandoned. What would you like to do?\n\n[[RESCUE PUPPY->Rescued]]\n[[CALL FOR HELP->Call]]\n[[DRIVE PAST->Drive Past]]",
      "links": [
        {
          "linkText": "RESCUE PUPPY",
          "passageName": "Rescued",
          "original": "[[RESCUE PUPPY->Rescued]]"
        },
        {
          "linkText": "CALL FOR HELP",
          "passageName": "Call",
          "original": "[[CALL FOR HELP->Call]]"
        },
        {
          "linkText": "DRIVE PAST",
          "passageName": "Drive Past",
          "original": "[[DRIVE PAST->Drive Past]]"
        }
      ],
      "hooks": [],
      "cleanText": "You continue to drive as you chuckle to yourself at the absurdity that you have just passed.You look at the time and start to get worried. While driving on the highwau you see a small cardbox, as you get closer you see a small puppy that has been abandoned. What would you like to do?"
    },
    {
      "name": "Ending 4: Hippies",
      "tags": "",
      "id": "16",
      "text": "You run into the field of flowers forgetting about your job, capitalism, society, and anything else that may trouble you. Are you in a cult? It doesn't matter, you have found your people, you are free now!\n\t\t\t\t\t\t\t\tGAME OVER",
      "links": [],
      "hooks": [],
      "cleanText": "You run into the field of flowers forgetting about your job, capitalism, society, and anything else that may trouble you. Are you in a cult? It doesn't matter, you have found your people, you are free now!\n\t\t\t\t\t\t\t\tGAME OVER"
    },
    {
      "name": "Rescued",
      "tags": "",
      "id": "17",
      "text": "You pull off onto the side of the road and pick up the cardboard box, you see asmall puppy braking with excitement and wagging its tail at the sight of you. You think about it for a moment and decide to forget about work and take it home. You may have gotten fired but that doesn't overshadow the joy that man's best friend gives you!\n\t\t\t\t\t\t\t\tGAME OVER",
      "links": [],
      "hooks": [],
      "cleanText": "You pull off onto the side of the road and pick up the cardboard box, you see asmall puppy braking with excitement and wagging its tail at the sight of you. You think about it for a moment and decide to forget about work and take it home. You may have gotten fired but that doesn't overshadow the joy that man's best friend gives you!\n\t\t\t\t\t\t\t\tGAME OVER"
    },
    {
      "name": "Call",
      "tags": "",
      "id": "18",
      "text": "You decide to pick up your phone and call the nearest animal rescue for them to come and pick the pup up. Although you feel bad leaving it, you didn't waste anytime and still are on pace to get to work in time.\n\n[[DRIVE->Work]]",
      "links": [
        {
          "linkText": "DRIVE",
          "passageName": "Work",
          "original": "[[DRIVE->Work]]"
        }
      ],
      "hooks": [],
      "cleanText": "You decide to pick up your phone and call the nearest animal rescue for them to come and pick the pup up. Although you feel bad leaving it, you didn't waste anytime and still are on pace to get to work in time."
    },
    {
      "name": "Drive Past",
      "tags": "",
      "id": "19",
      "text": "You drive past the box wothout any second thought. It may be brutal but hey, you've got to get to work!\n\n[[DRIVE->Work]]",
      "links": [
        {
          "linkText": "DRIVE",
          "passageName": "Work",
          "original": "[[DRIVE->Work]]"
        }
      ],
      "hooks": [],
      "cleanText": "You drive past the box wothout any second thought. It may be brutal but hey, you've got to get to work!"
    },
    {
      "name": "Work",
      "tags": "",
      "id": "20",
      "text": "You see the front of the building and your stress melts away. All your hard work has finally paid off. You sprint into the building and clock in. And head straight to your cubicle. With all this running around you've seem to have forgotten that your day really hasn't even started yet. You take a deep breath and start your day.\n                             GAME OVER: YOU WIN",
      "links": [],
      "hooks": [],
      "cleanText": "You see the front of the building and your stress melts away. All your hard work has finally paid off. You sprint into the building and clock in. And head straight to your cubicle. With all this running around you've seem to have forgotten that your day really hasn't even started yet. You take a deep breath and start your day.\n                             GAME OVER: YOU WIN"
    }
  ]
}
def find_current_location(location_label):
	if "passages" in world:
		for passage in world["passages"]:
			if location_label == passage["name"]:
				return passage
	return {}

# ----------------------------------------------------------------

def render(current_location, score, moves):
	if "name" in current_location and "cleanText" in current_location:
         print("Moves: " + str(moves) + ", Score: " + str(score))
         print("You are at the " + str(current_location["name"]))
         print(current_location["cleanText"] + "\n")

def get_input():
	response = input("What do you want to do? ")
	response = response.upper().strip()
	return response

def update(current_location, location_label, response):
	if response == "":
		return location_label
	if "links" in current_location:
		for link in current_location["links"]:
			if link["linkText"] == response:
				return link["passageName"]
	print("I don't understand what you are trying to do. Try again.")
	return location_label


# ----------------------------------------------------------------

location_label = "Bedroom"
current_location = {}
response = ""
score = 0
moves = 0

while True:
	if response == "QUIT":
	  break
moves =+ 1
location_label = update(current_location, location_label, response)
current_location = find_current_location(location_label)
render(current_location, score, moves)
if "score" in current_location:
  score = score + current_location["score"]
response = get_input()

print("Thanks for playing!")
