# coordinates-data-parser
Python script to extract latitude and longitude coordinates from an HTML page automatically

## Description

**What is the Coordinates Data Parser?** 

**Purpose of the Project**
The purpose of this project is to automate a portion of data collection via scrape. Coordinates follow a pattern that can be parsed and extracted through regex. 

## Getting Started

### Dependencies
Simply import this module into your Scrapy scrape

### Installing
Once imported, you can call the function and pass the html response. Upon success the module will return a dict with the coordinates. Upon failure, the module will return None. you can simply add the following code into your scrape. Note that the parameter 'response' is the html data your scrape is directed to.
```python
    import CoordinatesDataParser
    def get_coords(self, response):
        parser = CoordinatesDataParser()
        return parser.get_coords(response)
```
### Executing program
The coordinates data parser is run by integrating into your scrape and activating through your standard means

### Limitations
As the coordinates are extracted via regex, the parser can only extract coordinates for the North American continent. Additionally, the parser is hard coded to search for coordinates only in the body of the html response, and does not currently have the functionality to search the \<head\> of the html response. This is done to cut down on false positive results.

## Help
If there are any problems or issues with this app, please contact the author.

## Authors
Coordinates  was developed by Alex Silvester in 2019
You may contact Alex via email at (aosilvester@gmail.com) with any questions.

## Version History
* 0.1
    * Initial Release
