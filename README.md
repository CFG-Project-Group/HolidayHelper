<h1 align="center">
Holiday Helper
</h1>

This app will help you find your way around a new place you’re visiting! Starting slowly with just 4 cities (Barcelona, Budapest, London and Prague) but looking to the future with expansion vision for any place you're dreaming of!
To use the app you have to register, but then you’ll free to roam around. You can check the area on the map, look for nearby attractions and current weather, you can check what events are happening in the next few days or check how to say ‘Hello’ in native language! And if you’re planning to shop around you can always check how much it is in your currency so you don’t have to worry about spending over your limit. Who knew Kč285 is around £10?!

<h2> Installation Guide: </h2>
There are few bits to install before running the app. 
SQL schema to run in MySQL Workbench (or similar):

- schema.sql

Use the terminal to install Python packages (or go to Python Packages and search for them):

- flask
- flask-login
- mysql-connector-python
- requests
- google-cloud-translate

Create new txt file called config.txt and insert your app key for weather and events API, which should look like this:

![Picture1](https://user-images.githubusercontent.com/109172518/199459455-e020fe02-e89c-40df-9cfa-55d47cec3dba.png)


For translator API you need to create a JSON called GoogleKey.json file with your key, which should look like this:

![Picture2](https://user-images.githubusercontent.com/109172518/199459507-496fde9b-b68d-41d7-9d68-4791fea9944b.png)


<h2> Helpful Documentation: </h2>

- OpenWeather API documentation: https://openweathermap.org/api/one-call-3
- Serpapi-Google Events API documentation: https://serpapi.com/google-events-api
- Google Translation API documentation: https://cloud.google.com/translate/docs/quickstarts?hl=en_GB&_ga=2.118855433.-1612761519.1665944235
- Google Maps API documentation: https://github.com/googlemaps/google-maps-services-python
- Frankfurter API documentation: https://www.frankfurter.app/docs/

<h2> Navigation in the app: </h2>
Once your app runs it will ask you to register or log in if you already have an account, once logged in it will grant you access to Holiday Helper and redirect you to our home page. You are now free to explore all the available information about your chosen cities!

<h2> Collaborators: </h2>
Maneh Seiranian, Magdalena Sosinska, Mary Ruth Bongon, Samin Nazarpouri

<h3> CFG Degree – Final Project – Software-2 -Nov 2022 </h3>
