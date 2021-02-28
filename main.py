import bottle 

@bottle.route('/')
def initialIndex():
    return bottle.static_file('index.html', root='.')

@bottle.route('/index.html')
def index():
    return bottle.static_file('index.html', root='.')

@bottle.route('/aboutus.html')
def aboutus():
    return bottle.static_file('aboutus.html', root='.')

@bottle.route('/login.html')
def login():
    return bottle.static_file('login.html', root='.')

@bottle.route('/presentations.html')
def presentations():
    return bottle.static_file('presentations.html', root='.')

@bottle.route('/presentTest.html')
def presentTest():
  return bottle.static_file('presentTest.html',
  root='.')

@bottle.route('/upload.html')
def upload():
  return bottle.static_file('upload.html',
  root='.')

@bottle.route('/stream.html')
def stream():
  return bottle.static_file('stream.html',
  root='.')

@bottle.route('/myStyle.css')
def css():
    return bottle.static_file('myStyle.css', root='.')

bottle.run(host='0.0.0.0', port='8080', debug=True)