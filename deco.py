import functools
def log(msg=None):
    def decorator(func):
        @functools.wraps(func)
        def wraper(*args,**kw):
            print 'begin call'
            rest=func(args,**kw)
            print 'end call'
            return rest
        return wraper
    return decorator

@log('excute')
def now():
    print '2015-11-11'

now()
