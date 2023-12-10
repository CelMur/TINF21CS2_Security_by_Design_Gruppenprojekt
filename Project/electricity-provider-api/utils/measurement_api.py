import requests
from datetime import datetime, timedelta

class Api:
    def __init__(self, api_key:str, customer_uid:str, api_url:str):
        self.__api_key:str = api_key
        self.__api_url:str = api_url
        self.__customer_uid:str = customer_uid
        self.__api_endpoints = {
            "meter_create": f"{self.__api_url}/v1/provider/meter-create",
            "meter_measurements": f"{self.__api_url}/v1/provider/meter-measurements",
            "meter_delete": f"{self.__api_url}/v1/provider/meter-delete"
        }

        self.__headers = {
            "Authorization": f"Bearer {self.__api_key}"
        }
        

    def create_meter(self):
        url = self.__api_endpoints["meter_create"]
        data = {
            "customerUID": self.__customer_uid
        }
        response = requests.post(url, json=data, headers=self.__headers)
        return response.json()

    def get_meter_measurements(self, meter_uid:str, start_time:datetime, end_time:datetime, data_interval:int):
        url = self.__api_endpoints["meter_measurements"]
        params = {
            "customerUID": self.__customer_uid,
            "meterUID": meter_uid,
            "startTime": start_time.isoformat(),
            "endTime": end_time.isoformat(),
            "dataInterval": data_interval
        }
        response = requests.get(url, params=params, headers=self.__headers)
        return response.json()

    def delete_meter(self, meter_uid:str):
        url = self.__api_endpoints["meter_delete"]
        data = {
            "meterUID": meter_uid,
            "customerUID": self.__customer_uid
        }
        response = requests.delete(url, json=data, headers=self.__headers)
        return response.json()
    
    def get_lates_measurements(self, meter_uid:str):
        url = self.__api_endpoints["meter_measurements"]
        params = {
            "customerUID": self.__customer_uid,
            "meterUID": meter_uid,
            "startTime": datetime.now().isoformat(),
            "endTime": (datetime.now() - timedelta(seconds=1)).isoformat(),
            "dataInterval": 1
        }
        response = requests.get(url, params=params, headers=self.__headers)
        return response.json()