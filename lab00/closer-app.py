import time 

def elapsed(original_func):
  def wrapper():
    start = time.time()
    result = original_func() 
    end = time.time() 
    print("함수 수행시간: %f 초" % (end - start))
    
    return result 
  return wrapper

def myfunc():
    print("함수가 실행됩니다.")
    
decorated_myfunc = elapsed(myfunc)
decorated_myfunc()    