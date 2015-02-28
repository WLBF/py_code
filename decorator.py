import functools



def log(func):

    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'Begin call'
        func(*args, **kw)
        print 'End call'
        

    return wrapper

@log
def hello():
    return 'Hello world!'



print hello()
