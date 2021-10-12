

class Plugin_OBJ():

    def __init__(self, plugin_utils):
        self.plugin_utils = plugin_utils

    @property
    def tuners(self):
        return self.plugin_utils.config.dict["ustvgo"]["tuners"]

    @property
    def stream_method(self):
        return self.plugin_utils.config.dict["ustvgo"]["stream_method"]

    def get_channels(self):

        channels_url = "https://ustvgo.tv/tvguide/national.json"

        chan_req = self.plugin_utils.web.session.get(channels_url)
        entries = chan_req.json()

        channel_list = []
        chan_number_index = 0
        for channel_dict in entries:
            chan_number_index += 1

            clean_station_item = {
                                 "name": channel_dict["channel"]["fullName"],
                                 "callsign": channel_dict["channel"]["name"],
                                 "number": chan_number_index,
                                 "id": channel_dict["channel"]["sourceId"],
                                 "thumbnail": "https://static.streamlive.to/images/tv/%s.png" % channel_dict["channel"]["name"].lower().replace("&", "")
                                 }
            channel_list.append(clean_station_item)
        return channel_list

    def get_channel_stream(self, chandict, stream_args):

        streamurl = self.get_ustvgo_stream(chandict["callsign"])

        stream_info = {"url": streamurl}

        return stream_info

    def get_ustvgo_stream(self, chancode):
        data = {'stream': chancode}
        stream_url = self.plugin_utils.web.session.post('https://ustvgo.tv/data.php', data=data).text
        return stream_url
