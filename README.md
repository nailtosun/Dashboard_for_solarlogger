
# Web scraping for Solar-log with Python3

## Needed libraries


```python
import requests
```

If you don't have request module 
- For windows 
pip install requests
- Unix (Linux, Mac OS)
sudo pip install requests

##  Request Methods

We are gonna use POST method for scraping. request.post method takes 2 input parameters
- 'url'
- data (headers)

### Finding right headers
I collect some useful data headers for solar-log device. You can find cheat-sheet at following link. 
However if you want to search for other data you can use your browsers developer tools (F12). All transferred data package is in Network tab. You can find all headers at getjp packages. 

![title](asfas.png)

I chose total energy supplied by Ayasli GES data with following header


```python
headers = 'token=;preval=none;{"801":{"130":null,"131":null}}'
```

### Requesting 


```python
data_that_i_scraped = requests.post('http://144.122.167.229/getjp', data = headers)
```

#### Checking the response
data_that_i_scraped is a variable contains response
- 200 Success
- 404 Not found


```python
data_that_i_scraped
```




    <Response [200]>



Transferred data in the form of JSON file. To convert into string i used .json() method


```python
data_formed_as_string =  data_that_i_scraped.json()
```


```python
data_formed_as_string
```




    {'801': {'130': {'100': '82609.633',
       '101': '38099.5404',
       '102': '0.000',
       '103': '0.0000',
       '104': '0.0000',
       '105': '0.000',
       '106': '0.0000',
       '107': '38099.5404',
       '108': '0.0000',
       '109': '38099.5404',
       '110': '0.0000'},
      '131': {'100': '173.777',
       '101': '80.1459',
       '102': '0.000',
       '103': '0.0000',
       '104': '0.0000',
       '105': '0.000',
       '106': '0.0000',
       '107': '80.1459',
       '108': '0.0000',
       '109': '80.1459',
       '110': '0.0000'}}}




```python
total_energy = data_formed_as_string['801']['130']['100']
```


```python
total_energy
```




    '82609.633'


