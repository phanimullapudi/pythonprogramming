import twitter

api = twitter.Api(consumer_key='pTGD1ic97oZd1A66nBNE2LT8r',
  consumer_secret='A781wWJLIbQwipnBxVyFkYdbkkSqvZRrq3K06OKLLA0EsskRwL',
    access_token_key='CzIiUxiM3NuYUcy4IrfqK6ds9zk3Q6T2DYi8KppZm',
    access_token_secret='P2R3Qf8Q5BjJandrUuvueauB4zxejQeQnA5acqiT7DpWr')

print(api.VerifyCredentials())