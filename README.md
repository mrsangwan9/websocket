# websocket
#django channels
#js websocket


This is simple repo with that's show how django channels work with websocket.
But seriously websocket are a feature of js so to implement websocket over front end.
We have to use or start connection with the help of js in html file or during loads of page.

we have a consumer.py file for connect websocket with the help of django channels..

****tips***
To change data python(dict,list,) to string
import json 
change_str_data = json.dumps(python_data_variable)

to change data string to python
import json
change_py_data= json.loads(string_data_variable)


To change js object into string
changed_string = JSON.stringfy(js_object)

to change string to js object
js_object = JSON.parse(string)

