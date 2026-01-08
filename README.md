# jHub Coding Scheme Module 9 - Cloud Computing

## Task
Graduates of Module 3 (Python)

Deploy a web API, using Python and an open source framework such as Flask, to provide a simple 'weather' service that could be connected to by other (future) military web applications.
 The API should have at least 2 endpoints eg:
'temperature at location' which provides the user a (random) temperature, having been passed a location
'wind speed at location' which provides the user a (random) wind speed and direction (12kts at 058deg), having been passed a location
The API should be deployed to the cloud and made available either publicly or beyond a deployed compute instance (eg Elastic Beanstalk / Azure App Services, not just localhost). Connection to a database will allow for a richer user interaction, but this is not required. Example solutions include:
https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/create-deploy-python-flask.html
https://docs.microsoft.com/en-us/samples/azure-samples/azure-sql-db-python-rest-api/azure-sql-db-python-rest-api/
Provide a link the source code, along with a brief description of the process undertaken to host the API. Attach screenshots of the API running in the cloud, showing the result of API calls as directed by the user. 