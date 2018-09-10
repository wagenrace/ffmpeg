#!/usr/local/bin/python3
# module sys

from ffmpeg import video

from ffmpeg import audio


# 添加多个图片
img = [
        {
            "img": "01.png",
            "x": "",
            "y": "",
            "str_time": "5",
            "end_time": "15",
        },
        {
            "img": "01.png",
            "x": "",
            "y": "",
            "str_time": "20",
            "end_time": "25.5"
        }
    ]

video.ins_img("test.mp4", img,"out.mp4")


# 添加动图 gif apng
img = {
    "img": "img.apng",
    "x": "20",
    "y": "20",
    "str_time": "2",
    "end_time": "10"
}

video.ins_dynamic_img("test.mp4", img, "test.mp4")

# 视频静音 分离音频

video.separate_audio("test.mp4", "out.mp4")

# 视频静音 使用静音帧 将视频静音

video.video_ins_mute_audio("test.mp4", "mute.mp3", "out.mp4")

# 设置视频的分辨率 以及 码率
video.trans_code("test.mp4", "640", "480", "2000", "out.mp4")

# 视频加弹幕 context 弹幕内容 str_time 是第几秒显示 speet 速率 默认 150 当显示时间一定时 该值越大，速度越快
bage = [
    {
        "context": "Hello World 1 !!!",
        "fontcolor": "white",
        "fontsize": "40",
        "fontfile": "PingFang-SC-Regular.ttf",
        "y": "100",
        "str_time": "2",
        "speet": "150",
    },
    {
        "context": "Hello World 2 !!!",
        "fontcolor": "white",
        "fontsize": "40",
        "fontfile": "PingFang-SC-Regular.ttf",
        "y": "200",
        "str_time": "2",
        "speet": "150",
    },
]

video.ins_barrage("test.mp4", bage, "out.mp4")

# 调整视频速率 speed 小于 1 减速，大于 1 加速 1 等速
video.playback_speed("test.mpt", "1.5", "out.mp4")

# 倒放视频 + 音频
video.a_v_reverse("test.mp4", "out.mp4")

# 倒放视频 音频不变
video.v_reverse("test.mp4", "out.mp4")

# 调整音频速率
audio.audio_speed("test.mp3", "2", "out.mp3")