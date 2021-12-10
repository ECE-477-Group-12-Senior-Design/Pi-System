# Constants.py
# 
# ECE 47700
# Group 12
# Brace for Impact
#
# October 01, 2021
#

# 
# ---------- TWILIO ---------- 
#
TWILIO_ACCOUNT_SID = "TWILIO_ACCOUNT_SID"
TWILIO_AUTH_TOKEN = "TWILIO_AUTH_TOKEN"

TWILIO_FROM_NUMBER = '+14125047175'
TWILIO_USER_NAME = 'TWILIO_USER_NAME'
TWILIO_CONTACT_NAME = 'TWILIO_CONTACT_NAME'
TWILIO_CONTACT_NUMBER = 'TWILIO_CONTACT_NUMBER'

TWILIO_FORMATTED_TEST_SMS = 'Hi, {}. This is a test message from Brace for Impact.'
TWILIO_FORMATTED_EMERGENCY_SMS = '*** EMERGENCY: {} has fallen. Please contact them and/or emergency services immediately.'
TWILIO_FORMATTED_LOW_BATTERY_SMS = 'Hi, {contact_name}. {user_name}\'s fall detection bracelet is running low on battery. Please have them charge the device as soon as possible.'
TWILIO_FORMATTED_FULL_BATTERY_SMS = 'Hi, {contact_name}. {user_name}\'s fall detection bracelet is charged. Please have them wear the bracelet again.'
TWILIO_FORMATTED_CHARGING_BATTERY_SMS = 'Hi, {contact_name}. {user_name}\'s fall detection bracelet is charging. It\'ll be ready for reuse shortly.'
TWILIO_FORMATTED_BATTERY_FAULT_SMS = 'Hi, {contact_name}. {user_name}\'s fall detection bracelet has detected a charging fault. Please disconnect the charging cable from the device and try again. If issues persist, please contact our support center.'

# 
# ---------- GUI ---------- 
#
GUI_INPUT_USER_NAME = 'USER_NAME'
GUI_INPUT_CARETAKER_NAME = 'CARETAKER_NAME'
GUI_INPUT_CARETAKE_PHONE_NUMBER = 'CARETAKER_PHONE_NUMBER'
GUI_EVENT_QUIT = 'QUIT'
GUI_EVENT_SEND_TEST = 'Send Test Message'
GUI_FORMATTED_CONFIRM_SMS = 'Please have {} check their phone for a confirmation message.'
