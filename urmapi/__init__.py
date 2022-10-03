"""
Update Rollout Manager API [URM-API]

Simple? way to manage application updates?
Made by NoKodaAddictions, NoKoda
"""

import requests
from termcolor import colored

__version__ = "1.0"

class API:
    server:str = None
    response:str = None
    package_data:dict = None

    def __init__(self, link:str):
        self.server = link
        self.response = requests.get(f"{self.server}/config.urmapi.json")

        if self.response.status_code != 200:
            raise requests.RequestException(f"Error: {self.response.status_code}")

        else:
            self.package_data = self.response.json()

    def install(self):
        print(f"Reading config.urmapi.json at '{self.server}'...")
        return
    
    def update(self):
        return

class Build:
    pass