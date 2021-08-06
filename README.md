# [FastAPI + PostgreSQL + Docker]

## About Technologies
- FastAPI: _Web framework for building APIs with Python_
- PostgreSQL: _Open source object-relational database system_
- Docker: _Open source containerization platform_

## Problem case
In this task, I have created a micro service which obtains information on active containers
travelling on sea using scrapers and a work-management system.

### Containers# & Bill of Lading# Tracking
- Hit the url https://www.msc.com/track-a-shipment [Use the search bar values given]
- Use Container #’s [Each Container is shipped by a Carrier]: FSCU8362129 (Active)
- Use Bill of Lading #’s [Each of bill of lading is a collection of Container #’s]: MEDUJ1581977 (Active)

## How to Run this project?
- Make sure Docker is intalled and running on your machine
- Open terminal to the 'docker-compose.yml' path and run the bellow command:
```sh
docker-compose up -d 
```
- Open up a browser and use the following URL to test the APIs:
```
http://0.0.0.0:8000/docs
```
