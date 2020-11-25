from flask import request, render_template


class Channels_HTML():
    endpoints = ["/channels", "/channels.html"]
    endpoint_name = "page_channels_html"

    def __init__(self, fhdhr):
        self.fhdhr = fhdhr

    def __call__(self, *args):
        return self.get(*args)

    def get(self, *args):

        channelslist = []
        for fhdhr_id in list(self.fhdhr.device.channels.list.keys()):
            channel_obj = self.fhdhr.device.channels.list[fhdhr_id]
            channel_dict = channel_obj.dict.copy()
            channel_dict["play_url"] = channel_obj.play_url()
            channelslist.append(channel_dict)

        return render_template('channels.html', request=request, fhdhr=self.fhdhr, channelslist=channelslist)
