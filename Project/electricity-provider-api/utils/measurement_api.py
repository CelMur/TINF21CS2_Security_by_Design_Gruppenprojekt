import requests
from datetime import datetime, timedelta

class ApiException(Exception):
    def __init__(self, message:str, status_code:int, error_data:dict = None):
        self.message = message
        self.status_code = status_code
        self.__error_data = error_data

    @property
    def error_data(self):
        return self.__error_data
    


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
        '''
        Wrapper method for external api endpoint used for creation of smart meter.

        Args:
            None
        
        Returns: 
            The UID of the created meter

        Raises: 
            ApiException if the request fails for any reason (status code != 201)
        Raises: 
            Exception if any other error occurs (=> probably a bug in the code, lol)
        '''

        url = self.__api_endpoints["meter_create"]
        data = {
            "customerUID": self.__customer_uid
        }
        response = requests.post(url, json=data, headers=self.__headers)

        if response.status_code != 201: #201 => created
            raise ApiException(f"Request failed with status {response.status_code}: {response.text}", response.status_code, response.json())
        return response.json().get("meterUID")

    def get_meter_measurements(self, meter_uid:str, start_time:datetime, end_time:datetime, data_interval:int):
        '''
        Wrapper method for external api endpoint used for getting the measurements of a smart meter.

        Args:
            meter_uid: The UID of the meter
            start_time: The start time of the measurements
            end_time: The end time of the measurements
            data_interval: The interval between measurements in seconds

        Returns:
            The measurements of the meter as dict

        Raises:
            ApiException if the request fails for any reason (status code != 200)
        Raises:
            Exception if any other error occurs (=> probably a bug in the code, le mau o_O)
        '''
        
        url = self.__api_endpoints["meter_measurements"]
        params = {
            "customerUID": self.__customer_uid,
            "meterUID": meter_uid,
            "startTime": start_time.isoformat(),
            "endTime": end_time.isoformat(),
            "dataInterval": data_interval
        }
        response = requests.get(url, params=params, headers=self.__headers)

        if response.status_code != 200:
            raise ApiException(f"Request failed with status {response.status_code}: {response.text}", response.status_code, response.json())
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
        '''
        Wrapper method for external api endpoint used for getting the latest measurements of a smart meter.
        Args: 
            meter_uid: The UID of the meter

        Returns: 
            The latest measurements of the meter

        Raises: 
            ApiException if the request fails for any reason (status code != 200)
        Raises: 
            Exception if any other error occurs (=> probably a bug in the code, have fun debugging xD)
        '''

        url = self.__api_endpoints["meter_measurements"]
        params = {
            "customerUID": self.__customer_uid,
            "meterUID": meter_uid,
            "startTime": datetime.now().isoformat(),
            "endTime": (datetime.now() - timedelta(seconds=1)).isoformat(),
            "dataInterval": 1
        }
        response = requests.get(url, params=params, headers=self.__headers)

        if response.status_code != 200:
            raise ApiException(f"Request failed with status {response.status_code}: {response.text}", response.status_code, response.json())

        return response.json()