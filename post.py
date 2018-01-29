import facebook
import lcdlib
import time
import sys
access_token = 'EAAAALPXpAIkBACfPB7mDq7qQ2DpsBe1ZCvinHNt0GD0Wpzps67I6WMtVCX7IB4U1R8wxzYgsbZBnK6sqNaMvyJAiY4u6LurusE024zBNw52gVrNwQGpIh9lmPG1gOsBr3hZAJjCm0efldkUSZBkUa6MpXv9fxbeCbZA7ZCyP9wuQZDZD'
post_id = sys.argv[1]
lcd=lcdlib.lcd()
graph = facebook.GraphAPI(access_token, version="2.11")

try:
        while 1:
		post = graph.get_object(post_id, fields='reactions.summary(true).limit(0),comments.summary(true).limit(0)')
		reactions = post['reactions']['summary']['total_count']
		comments = post['comments']['summary']['total_count']
		lcd.lcd_display_string("Reactions {}".format(reactions), 1)
    		lcd.lcd_display_string("Comments {}".format(comments), 2)	
		print("Reactions : {} | Comments : {}".format(reactions, comments))
		time.sleep(1)
except:
        lcd.lcd_clear()
	lcd.backlight(0)
