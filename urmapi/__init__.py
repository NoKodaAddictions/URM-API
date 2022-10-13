"""
Update Rollout Manager API [URM-API]

Simple? way to manage application updates?
Made by NoKodaAddictions, NoKoda
"""

import json
import requests
from termcolor import colored
import os

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
    directory:str = None
    response:requests.Response = None
    package_data:dict = None
    package_version:str = None

    def __init__(self, server:str = None, directory:str = None):
        self.server = server
        self.directory = directory

        if self.directory != None:
            with open(self.directory) as r:
                self.package_data = json.load(r)
                self.server = self.package_data["HEAD"]["package"]["package_url"]

        self.response = requests.get(f"{self.server}/config.urmapi.json")
        
        if self.response.status_code != 200:
            raise requests.RequestException(f"Error: {self.response.status_code}")

        else:
            self.package_data = self.response.json()

    def install(self, location:str = None):
        print(f"Reading config.urmapi.json at '{self.server}'...")
        self.package_name = self.package_data["HEAD"]["package"]["name"]
        self.package_version = self.package_data["HEAD"]["config"]["version"]

        success = 0
        errors = 0

        if self.package_version in __accepted_versions__:
            print(colored('Package versions match', 'green'))
            os.system(f'mkdir "{self.package_name}"')

            print("Downloading Files...")

            for file in self.package_data["CONTENT"]["files"]:
                print(f"Fetching: {file}...")

                get = requests.get(f"{self.server}/{file}")

                if get.status_code == 200:
                    print(colored(f"Downloading {file}...", "green"))
                    success += 1
                
                    path = os.path.dirname(file)

                    if path != "":
                        if location != None:
                            os.mkdir(f'{location}/{self.package_name}/{path}')
                        
                        else:
                            os.mkdir(f'{self.package_name}/{path}')

                    with open(f"{self.package_name}/{file}",'wb') as w:
                        w.write(get.content)

                
                else:
                    print(colored(f"File not found: {file}", "red"))
                    errors += 1

            print("Download Summary: ")
            print(f"Success: {success} | Fails: {errors} | Percentage: {(success/(success+errors))*100}%")

        else:
            raise Exceptions.UnsupportedPackageError(f"Package Version is: {self.package_version}. \
                This version of URM-API only supports: {__accepted_versions__}")
    
    def update(self):
        return

class Build:
    pass