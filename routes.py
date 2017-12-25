from app import app

@app.route('/')
@app.route('/index')
def index():
    return("Hello World")


@app.route('/dir', methods='GET')
def dir():
    results = DownloadListing.get_results()
    return resp