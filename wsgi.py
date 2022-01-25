from concurrent.futures import thread
from manage import app 
if __name__=="__main__":
    app.run(threaded=True)