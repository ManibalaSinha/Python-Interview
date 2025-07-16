#Implement a rate limiter (token bucket)
import time #time module to track timestamps and delays

class TokenBucket: #to implement rate limiting logic
    def __init__(self, capacity, refill_rate): #constructor method to initialize the bucket
        self.capacity = capacity #maximum numbers of tokens the bucket can hold
        self.tokens = capacity #At the beginning, the bucket is full — all tokens are available.
        self.refill_rate = refill_rate  # Number of tokens added per second to the bucket (e.g 1 token/sec)
        self.last_refill = time.time() #Stores the timestamp of the last time the bucket was refilled (in seconds)


    def allow_request(self): #Method that is called whenever a new request comes in
        now = time.time() #Gets the current time in seconds
        elapsed = now - self.last_refill #Calculates how much time has passed since the last refill
        #Refill tokens Formula: tokens += elapsed_time × refill_rate
        self.tokens = min(self.capacity, self.tokens + elapsed * self.refill_rate)
        self.last_refill = now #Update the last refill timestamp to the current time after adding tokens

        if self.tokens >= 1: #Check if at least 1 token is available to allow the request.
            self.tokens -= 1 #Consume one token for the request
            return True
        else:
            return False

# Usage
bucket = TokenBucket(capacity=5, refill_rate=1)  # 5 requests burst, 1 per second refill

for i in range(10):
    if bucket.allow_request():
        print("Request allowed")
    else:
        print("Rate limit hit")
    time.sleep(0.5)
