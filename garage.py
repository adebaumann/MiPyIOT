import tinyweb
from machine import Pin
from time import sleep

# Create web server application
app = tinyweb.webserver()
Button=Pin(2,Pin.OUT)
Button.on()

# Index page
@app.route('/')
async def index(request, response):
    # Start HTTP response with content-type text/html
    await response.start_html()
    # Send actual HTML page
    await response.send('<html><body><h1>Hi George!</h1><a href="button/1">Push the garage door button</a></html>\n')


# Another one, more complicated page
@app.route('/button/<nr>')
async def table(request, response,nr):
    # Start HTTP response with content-type text/html
    Button.off()
    sleep(1)
    Button.on()
    await response.start_html()
    await response.send('<html><body><h1>Hi George!</h1>Button number %s pushed. <a href="/">Go back.</a> <a href="button">Or push it again.</a></html>\n'%nr)


def run():
    print ("running app")
    app.run(host='0.0.0.0', port=80)
