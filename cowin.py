'''
Script: Vaccine Slot Availability on CoWin App telegram bot
Author: Priyanshu Dubey
'''

import requests
from datetime import datetime
import json

base_url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode=822101&"
now = datetime.now()
today_date = now.strftime("%d-%m-%Y")
api_url = 'https://api.telegram.org/bot1865951478:AAG_Q1mxrxEI_NiCAA6k5cu1BP7upKDp5As/sendMessage?chat_id=@__groupid__&text='
group_id = 'slot_booking'

def fetch_data():
    qp = "date={}".format(today_date)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    final_url = base_url+qp
    response = requests.get(final_url, headers = headers)
    print(response.text)
    extract_availability(response)
    
def extract_availability(response):
    response_j = response.json()
    for sessions in response_j["sessions"]:
        print(sessions["center_id"], sessions["name"], sessions["available_capacity_dose1"], sessions["min_age_limit"])
        if sessions["available_capacity_dose1"] > 0 and sessions["min_age_limit"] == 18:
            print(sessions["center_id"], sessions["name"], sessions["available_capacity_dose1"], sessions["min_age_limit"])
            message = "Pincode: {}, \nName: {}, \nvaccine: {}, \nSlots: {}, \nMin Age: {}".format(
                sessions["pincode"],sessions["name"],sessions["vaccine"],
                sessions["available_capacity_dose1"],sessions["min_age_limit"]) 
        else:
            message = "Pincode: {}, \nName: {}, \nvaccine: {}, \nSlots: {}, \nMin Age: {}".format(
                sessions["pincode"],sessions["name"],sessions["vaccine"],
                sessions["available_capacity_dose1"],sessions["min_age_limit"]) 
        send_telegram(message)
def send_telegram(message):
    final_tele_url = api_url.replace("__groupid__", group_id)
    final_tele_url = final_tele_url+message
    response = requests.get(final_tele_url)
    print(response)

if __name__ == "__main__":
    fetch_data()
