"""Program to Simulate YouTube Channel with Observer Pattern@AakashNinan IMCA Rollno:02"""
class Subscriber:
    def __init__(self, name):
        self.name = name
    def notify(self, video_title):
        print(f"{self.name} notified: New video uploaded - {video_title}")

class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
    def upload_video(self, title):
        print(f"\n{self.name} uploaded: {title}")
        for sub in self.subscribers:
            sub.notify(title)

s1 = Subscriber("Alice")
s2 = Subscriber("Bob")
s3 = Subscriber("Charlie")

channel = YouTubeChannel("TechWorld")
channel.subscribe(s1)
channel.subscribe(s2)
channel.subscribe(s3)

channel.upload_video("Observer Pattern in Python")
channel.upload_video("Factory Pattern Explained")
