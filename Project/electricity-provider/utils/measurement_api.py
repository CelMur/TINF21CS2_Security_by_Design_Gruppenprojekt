import json
from uuid import uuid4
from django.conf import settings
import requests
from datetime import datetime, timedelta
from utils.logger import *

class ApiException(Exception):
    '''
    Custom Exception class for handling errors of the external measurement-provider-api.
    '''
    def __init__(self, message:str, status_code:int, error_data:dict = None):
        self.message = message
        self.status_code = status_code
        self.__error_data = error_data

    @property
    def error_data(self):
        return self.__error_data
    


class Api:
    def __init__(self, api_key:str, customer_uid:str, api_url:str, verify_ssl:bool, verify_ssl_path:str):
        self.__api_key:str = api_key
        self.__api_url:str = api_url
        self.__customer_uid:str = customer_uid
        self.__verify_ssl:bool = verify_ssl
        self.__verify_ssl_path:str = verify_ssl_path
        self.__api_endpoints = {
            "meter_create": f"{self.__api_url}/v1/provider/meter-create",
            "meter_measurements": f"{self.__api_url}/v1/provider/meter-measurements",
            "meter_delete": f"{self.__api_url}/v1/provider/meter-delete"
        }

        self.__headers = {
            "Authorization": f"Bearer {self.__api_key}"
        }
    
    @property
    def _verify_ssl(self) -> bool | str:
        if self.__verify_ssl: return self.__verify_ssl_path
        return False
        

    @staticmethod
    def get_instance():
        return Api(settings.MEASUREMENT_API_KEY, 
                   settings.MEASUREMENT_CUSTOMER_UID, 
                   settings.MEASUREMENT_API_URL,
                   settings.MEASUREMENT_API_VERIFY_SSL,
                   settings.MEASUREMENT_API_VERIFY_SSL_PATH)
    

    def create_meter(self) -> str:
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
        response = requests.post(url, json=data, headers=self.__headers, verify=self._verify_ssl)

        if response.status_code != 201: #201 => created
            raise ApiException(f"Request failed with status {response.status_code}: {response.text}", response.status_code, response.json())
        
        meter_uid = response.json().get("meterUID")
        logger.info(f"API: new meter created {meter_uid}")
        return meter_uid

    def get_meter_measurements(self, meter_uid:uuid4, start_time:datetime, end_time:datetime, data_interval:int) -> json:
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
            "meterUID": str(meter_uid),
            "startTime": start_time.astimezone().isoformat(),
            "endTime": end_time.astimezone().isoformat(),
            "dataInterval": data_interval
        }
        response = requests.get(url, params=params, headers=self.__headers, verify=self._verify_ssl)

        if response.status_code != 200:
            raise ApiException(f"Request failed with status {response.status_code}: {response.text}", response.status_code, response.json())
        return response.json()

    def delete_meter(self, meter_uid:str):
        url = self.__api_endpoints["meter_delete"]
        data = {
            "meterUID": str(meter_uid),
            "customerUID": self.__customer_uid
        }
        try:
            response = requests.delete(url, json=data, headers=self.__headers, verify=self._verify_ssl)
            logger.info(f"API: meter deleted {meter_uid}")
            return response.json()
        except Exception as e:
            logger.error(e, exc_info=True)
            raise e
        
    
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
            "meterUID": str(meter_uid),
            "startTime": datetime.now().isoformat(),
            "endTime": (datetime.now() - timedelta(seconds=1)).isoformat(),
            "dataInterval": 1
        }
        response = requests.get(url, params=params, headers=self.__headers, verify=self._verify_ssl)

        if response.status_code != 200:
            raise ApiException(f"Request failed with status {response.status_code}: {response.text}", response.status_code, response.json())

        return response.json()