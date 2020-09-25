let request = new XMLHttpRequest();


function publish_stream(){
    var formData = new FormData();
    const stream_link = document.getElementById("stream_link").value;
    const stream_key = document.getElementById("stream_key").value;
    const file_path = document.getElementById("file_path").value;

    formData.append(
        "stream_link",
        stream_link
    );
    formData.append(
        "stream_key",
        stream_key
    );
    formData.append(
        "file_path",
        file_path
    );

    request.open("POST", "/publish");
    request.send(formData);

    document.getElementById("record").innerHTML += `<br>
    <div class="blinking" style="display: inline-block;background: green;width: 1.3em;height: 1.3em;border-radius: 100%;margin-top: 3px;"></div>
    <div style="display: inline-block;color: white;font-size: 15px;padding-left: 15px;" id="record-desc">[ ${stream_link}/${stream_key} ] - ( ${file_path} )</div>`;
}