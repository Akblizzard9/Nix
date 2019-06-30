'''this is the most complete version of what I want'''
''' This will request and process a ski weather report from an API. I wanted to query and store server 
	side then have the user query my own db to keep the number of API request down.  '''
import psycopg2
import psycopg2.extras
import urllib.parse
import urllib.request
import json
import datetime

api_key = "f80f69a2dc2343fcbbe04557192904"

conn = psycopg2.connect(
	host= "localhost",
	user="mshaf",
	password="",
    port='5432',
	database="nix")


dict_cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
dict_cur.execute("""SELECT * FROM "site_face_resorts" ;""")
myresult = dict_cur.fetchall()
print(myresult)


'''this will take gps points stored in Resorts table and generate an api request'''
def snowfall_from(location):
	base_url = 'https://api.worldweatheronline.com/premium/v1/ski.ashx?'
	args = {'q': location, 'num_of_days': 1, 'key': api_key, 'format': 'json'}
	url = base_url + urllib.parse.urlencode(args)
	contents = urllib.request.urlopen(url).read()
	json_data = json.loads(contents)['data']
	weather = json_data['weather'][0]
	bottom_weather = json_data['weather'][0]['bottom'][0]
	middle_weather = json_data['weather'][0]['mid'][0]
	top_weather = json_data['weather'][0]['top'][0]

	bottom_mintemp = bottom_weather['mintempF']
	bottom_maxtemp = bottom_weather['maxtempF']
	middle_maxtemp = middle_weather['maxtempF']
	middle_mintemp = middle_weather['mintempF']
	top_mintemp = top_weather['mintempF']
	top_maxtemp = top_weather['maxtempF']
	snowfall = weather['totalSnowfall_cm']

	return { 'bottom_mintemp' : bottom_mintemp, 'bottom_maxtemp' : bottom_maxtemp, 'middle_mintemp' : middle_mintemp, 'middle_maxtemp' : middle_maxtemp, 'top_mintemp' : top_mintemp, 'top_maxtemp' : top_maxtemp, 'snowfall' : snowfall }

data = []
'''this will assign key pairs to insert into table Reports'''
for var in myresult:
	resort_id = var['id']
	weather = (snowfall_from(var['location']))
	date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
	data.append({"resort_id" : resort_id, "date" : date, "snowfall" : weather["snowfall"], "bottom_mintemp" : weather["bottom_mintemp"], "bottom_maxtemp" : weather["bottom_maxtemp"],
	 "middle_mintemp" : weather["middle_mintemp"], "middle_maxtemp" : weather["middle_maxtemp"], "top_mintemp" : weather["top_mintemp"], "top_maxtemp" : weather["top_maxtemp"]})

print (data)
'''data inserted into table Reports'''
for row in data:
	query = (
		f"INSERT INTO site_face_reports (resort_id_id, todays_date, snowfall, bottom_mintemp, bottom_maxtemp, mid_mintemp, mid_maxtemp, top_mintemp, top_maxtemp)\n"
		f"VALUES ({row['resort_id']}, '{row['date']}', {row['snowfall']}, {row['bottom_mintemp']}, {row['bottom_maxtemp']}, {row['middle_mintemp']}, {row['middle_maxtemp']}, {row['top_mintemp']}, {row['top_maxtemp']})"
	)
	dict_cur.execute(query)
	print(query)


conn.commit()
dict_cur.close()
conn.close()
