import logging

from stream.dslr   import dslr_camera
from stream.webcamp import web_camera
from stream.twitch_stream import TwitchStreamingService
from stream.youtube_stream import YouTubeStreamingService



def main():
    logging.basicConfig(level=logging.INFO)

    # create a device and streaming service
    service = YouTubeStreamingService()
    service.add_device(web_camera) 
    
    # start streaming
    reference = service.start_stream()
    service.fill_buffer(reference)
    service.stop_stream(reference)
    
    
if __name__ == "__main__":
    main()