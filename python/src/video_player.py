"""A video player class."""
import random
from .video_library import VideoLibrary
video_playing = False
current_video_id = ''
old_video_id = ''
video_paused = False
class VideoPlayer:
    """A class used to represent a Video Player."""

    def __init__(self):
        self._video_library = VideoLibrary()
        self.video_playing = video_playing
        self.current_video_id = current_video_id
        self.old_video_id = old_video_id
        self.video_paused = video_paused

    def number_of_videos(self):
        num_videos = len(self._video_library.get_all_videos())
        print(f"{num_videos} videos in the library")

    def show_all_videos(self):
        """Returns all videos."""
        print("Here's a list of all available videos:")
        video_list = []
        for i in self._video_library.get_all_videos():
            
            tags = "["
            for tag in i.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            video_list.append([f"{i.title} ({i.video_id}) {tags}"])
        for video in sorted(video_list):
            for vid in video:
                print(vid) 
                
    def play_video(self, video_id):
        """Plays the respective video.

        Args:
            video_id: The video_id to be played.
        """
        self.current_video_id = video_id
                
        video_list = self._video_library.get_all_videos()
        video_dict = {i.video_id : i.title for i in video_list}
        if video_id in video_dict:
            if self.video_playing == False:
                # play the video for the first time
                print(f"Playing video: {video_dict.get(video_id)}")
                self.video_playing = True
                self.old_video_id = self.current_video_id
            else:
                for i in [f"Playing video: {video_dict.get(self.old_video_id)}", f"Stopping video: {video_dict.get(self.old_video_id)}", f"Playing video: {video_dict.get(self.current_video_id)}"][1::]:
                    print(i)
                self.old_video_id = self.current_video_id
                self.video_playing = True
        else:
            if self.video_playing == False:
                print("Cannot play video: Video does not exist")
            else:
                # print()
                for i in [f"Playing video: {video_dict.get(self.old_video_id)}", "Cannot play video: Video does not exist"][1::]:
                    print(i)
                

    def stop_video(self):
        """Stops the current video."""
        video_list = self._video_library.get_all_videos()
        video_dict = {i.video_id : i.title for i in video_list}

        if self.video_playing == True:
            for i in [f"Playing video: {video_dict.get(self.current_video_id)}", f"Stopping video: {video_dict.get(self.current_video_id)}"][1::]:
                print(i)
            self.video_playing = False
        elif self.current_video_id == '':
            print("Cannot stop video: No video is currently playing")
            self.video_playing = False
        else:
            for i in [f"Playing video: {video_dict.get(self.current_video_id)}", f"Stopping video: {video_dict.get(self.current_video_id)}", "Cannot stop video: No video is currently playing"][3::]:
                print(i)
            print("Cannot stop video: No video is currently playing")
            self.video_playing = False
         

    def play_random_video(self):
        """Plays a random video from the video library."""
        video_list = self._video_library.get_all_videos()
        video_name_list = [name.title for name in video_list]
        video_dict = {i.video_id : i.title for i in video_list}

        if self.video_playing == False:
            print(f"Playing video: {random.choice(video_name_list)}")
            self.video_playing = True
        else:
            for i in [f"Playing video: {video_dict.get(self.current_video_id)}", f"Stopping video: {video_dict.get(self.current_video_id)}", f"Playing video: {random.choice(video_name_list)}"][1::]:
                print(i)
            self.video_playing = True

    def pause_video(self):
        """Pauses the current video."""
        video_list = []
        for i in self._video_library.get_all_videos():
            
            tags = "["
            for tag in i.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            video_list.append([i.title, i.video_id, tags])
        
        video_dict1 = {i[1] : i[0] for i in video_list}
        video_dict2 = {i[1] : i[2] for i in video_list}
        
        if self.video_paused == True:
            for i in [f"Playing video: {video_dict1.get(self.current_video_id)}", f"Pausing video: {video_dict1.get(self.current_video_id)}", f"Currently playing: {video_dict1.get(self.current_video_id)} ({self.current_video_id}) {video_dict2.get(self.current_video_id)} - PAUSED"][1::]:
                print(i)
        else:
            for i in [f"Playing video: {video_dict1.get(self.current_video_id)}", f"Pausing video: {video_dict1.get(self.current_video_id)}"][1::]:
                print(i)
            self.video_playing = False
            self.video_paused = True

    def continue_video(self):
        """Resumes playing the current video."""

        print("continue_video needs implementation")

    def show_playing(self):
        """Displays video currently playing."""
        video_list = []
        for i in self._video_library.get_all_videos():
            
            tags = "["
            for tag in i.tags:
                tags = tags + tag + " "
            tags = tags + "]"

            if tags != "[]":
                tags = tags[0:len(tags) - 2] + "]"

            video_list.append([i.title, i.video_id, tags])
        
        video_dict1 = {i[1] : i[0] for i in video_list}
        video_dict2 = {i[1] : i[2] for i in video_list}

        if self.video_playing == False:
            print("No video is currently playing")

        elif self.video_playing == True and self.video_paused == True:
            for i in [f"Playing video: {video_dict1.get(self.current_video_id)}", f"Pausing video: {video_dict1.get(self.current_video_id)}", f"Currently playing: {video_dict1.get(self.current_video_id)} ({self.current_video_id}) {video_dict2.get(self.current_video_id)} - PAUSED"][1::]:
                print(i)
        else:
            for i in [f"Playing video: {video_dict1.get(self.current_video_id)}", f"Currently playing: {video_dict1.get(self.current_video_id)} ({self.current_video_id}) {video_dict2.get(self.current_video_id)}"][1::]:
                print(i)
            
    def create_playlist(self, playlist_name):
        """Creates a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("create_playlist needs implementation")

    def add_to_playlist(self, playlist_name, video_id):
        """Adds a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be added.
        """
        print("add_to_playlist needs implementation")

    def show_all_playlists(self):
        """Display all playlists."""

        print("show_all_playlists needs implementation")

    def show_playlist(self, playlist_name):
        """Display all videos in a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("show_playlist needs implementation")

    def remove_from_playlist(self, playlist_name, video_id):
        """Removes a video to a playlist with a given name.

        Args:
            playlist_name: The playlist name.
            video_id: The video_id to be removed.
        """
        print("remove_from_playlist needs implementation")

    def clear_playlist(self, playlist_name):
        """Removes all videos from a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("clears_playlist needs implementation")

    def delete_playlist(self, playlist_name):
        """Deletes a playlist with a given name.

        Args:
            playlist_name: The playlist name.
        """
        print("deletes_playlist needs implementation")

    def search_videos(self, search_term):
        """Display all the videos whose titles contain the search_term.

        Args:
            search_term: The query to be used in search.
        """
        print("search_videos needs implementation")

    def search_videos_tag(self, video_tag):
        """Display all videos whose tags contains the provided tag.

        Args:
            video_tag: The video tag to be used in search.
        """
        print("search_videos_tag needs implementation")

    def flag_video(self, video_id, flag_reason=""):
        """Mark a video as flagged.

        Args:
            video_id: The video_id to be flagged.
            flag_reason: Reason for flagging the video.
        """
        print("flag_video needs implementation")

    def allow_video(self, video_id):
        """Removes a flag from a video.

        Args:
            video_id: The video_id to be allowed again.
        """
        print("allow_video needs implementation")
