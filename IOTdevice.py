import tinyweb
from machine import Pin
from machine import reset
from time import sleep
import json

settings=json.loads(''.join(open('settings.json').readlines()))

# Create web server application
app = tinyweb.webserver()

# Hardware Setup, e.g. Garage Door Remote
Button={}
for name in settings["buttons"].keys():
    Button[name]=Pin(settings["buttons"][name]["pin"],Pin.OUT)
    Button[name].off()

# Index page
@app.route('/')
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    # Send actual HTML page, in this example with three buttons
    await response.send('''<html><head>
                           <style>.button {  display: inline-block;  border-radius: 4px;  background-color: #00001e;  border: none;  color: #FFFFFF;  text-align: center;  font-size: 28px;  padding: 20px;  width: 200px;  transition: all 0.5s;  cursor: pointer;  margin: 5px;}</style>
                           </head><body><h1>Garage Door Remote</h1>
                           <a href="button/1"><button class="button">1</button></a>
                           <a href="button/2"><button class="button">2</button></a>
                           <a href="button/3"><button class="button">3</button></a>
                           </html>\n''')

@app.route('/reset')
async def index(request, response):
    await response.start_html()
    await response.send('''<html><head>
                           <style>.button {  display: inline-block;  border-radius: 4px;  background-color: #00001e;  border: none;  color: #FFFFFF;  text-align: center;  font-size: 28px;  padding: 20px;  width: 200px;  transition: all 0.5s;  cursor: pointer;  margin: 5px;}</style>
                           </head><body><h1>RESETTING...</h1>
                           </html>\n''')
    reset()

@app.route('/button/<nr>')
async def button(request, response,nr):
    # Start HTTP response with content-type text/html
    # Machine control
    Button[nr].on()
    sleep(settings['buttons'][nr]['delay'])
    Button[str(nr)].off()
    # Debug string
    print ('button %s (Pin %s) pressed for %s seconds'%(nr,Button[nr],settings['buttons'][nr]['delay']))
    #Send response
    await response.start_html()
    await response.send('<html><head><meta http-equiv="refresh" content="0;url=/" /></head><body><h1>Hi George!</h1>Button number %s pushed for %s seconds. <a href="/">Go back.</a></html>\n'%(nr,settings['buttons'][str(nr)]['delay']))

def Write_Settings():
    File=open('settings.json','w')
    File.write(json.dumps(settings))
    File.close()

#@app.route('/config',save_headers=[])
class config():
    def get(self,data):
        SanitizedSettings=settings.copy()
        if 'password' in SanitizedSettings:
            SanitizedSettings['password']='*not displayed*'
        if 'AP-password' in SanitizedSettings:
            SanitizedSettings['AP-password']='*not displayed*'
        return SanitizedSettings
    def post(self, data):
        print (data)
        for Setting in data.keys():
            settings[Setting]=data[Setting]
            print("Setting %s to %s"%(Setting,data[Setting]))
        Write_Settings()
        return data
    
    def delete(self,data):
        for Setting in data.keys():
            settings.pop(Setting)
            Write_Settings()
        return data    


def run():
    print ("running app")
    app.add_resource(config,"/config")
    app.run(host='0.0.0.0', port=80)
