    let currentStreamers = [];

    function addStream() {

        let streamer = document.getElementById('twitch').value;

        let url = "twitch.tv/" + streamer

        currentStreamers.unshift([url, streamer]);

        let display = "";

        for (entry of currentStreamers) {
            display += "<a href=" + entry[0] + ">" + entry[1] + " </a>\n";
        }
        document.getElementById('currentStreams').innerHTML = display;
}