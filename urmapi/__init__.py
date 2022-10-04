"""
Update Rollout Manager API [URM-API]

Simple? way to manage application updates?
Made by NoKodaAddictions, NoKoda
"""

import requests
from termcolor import colored

__version__ = "1.0"
__accepted_versions__ = [
    "1.0"
]

class Exceptions:
    class UnsupportedPackageError(Exception):
        """
        Raised if package versions do not match the URM-API Version
        """
    
    class PackageConfigError(Exception):
        """
        Raised if 
        - The package could not be read correctly
        - The package config is missing essential data
        """

class API:
    server:str = None
    response:requests.Response = None
    package_data:dict = None
    package_version:str = None

    def __init__(self, link:str):
        self.server = link
        self.response = requests.get(f"{self.server}/config.urmapi.json")

        if self.response.status_code != 200:
            raise requests.RequestException(f"Error: {self.response.status_code}")

        else:
            self.package_data = self.response.json()

    def install(self):
        print(f"Reading config.urmapi.json at '{self.server}'...")
        self.package_data = self.response.json()
        self.package_version = self.package_data["HEAD"]["config"]["version"] 
        if self.package_version == __version__:
            pass

        else:
            raise Exceptions.UnsupportedPackageError(f"Package Version is: {self.package_version}. \
                This version of URM-API only supports: {__accepted_versions__}")
    
    def update(self):
        return

class Build:
    pass