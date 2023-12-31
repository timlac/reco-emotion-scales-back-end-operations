video_files = [
    # f naro
    {"video_id": "A91",
     "sex": "f",
     "prosody": "naro"},
    {"video_id": "A102",
     "sex": "f",
     "prosody": "naro"},
    {"video_id": "A205",
     "sex": "f",
     "prosody": "naro"},
    {"video_id": "A221",
     "sex": "f",
     "prosody": "naro"},
    {"video_id": "A227",
     "sex": "f",
     "prosody": "naro"},
    {"video_id": "A425",
     "sex": "f",
     "prosody": "naro"},
    {"video_id": "A426",
     "sex": "f",
     "prosody": "naro"},

    # f meli
    {"video_id": "A323",
     "sex": "f",
     "prosody": "meli"},
    {"video_id": "A332",
     "sex": "f",
     "prosody": "meli"},
    {"video_id": "A334",
     "sex": "f",
     "prosody": "meli"},
    {"video_id": "A337",
     "sex": "f",
     "prosody": "meli"},
    {"video_id": "A405",
     "sex": "f",
     "prosody": "meli"},
    {"video_id": "A407",
     "sex": "f",
     "prosody": "meli"},
    {"video_id": "A424",
     "sex": "f",
     "prosody": "meli"},

    # m naro
    {"video_id": "A200",
     "sex": "m",
     "prosody": "naro"},
    {"video_id": "A207",
     "sex": "m",
     "prosody": "naro"},
    {"video_id": "A220",
     "sex": "m",
     "prosody": "naro"},
    {"video_id": "A72",
     "sex": "m",
     "prosody": "naro"},
    {"video_id": "A438",
     "sex": "m",
     "prosody": "naro"},
    {"video_id": "A435",
     "sex": "m",
     "prosody": "naro"},
    {"video_id": "A437",
     "sex": "m",
     "prosody": "naro"},

    # m meli
    {"video_id": "A303",
     "sex": "m",
     "prosody": "meli"},
    {"video_id": "A327",
     "sex": "m",
     "prosody": "meli"},
    {"video_id": "A55",
     "sex": "m",
     "prosody": "meli"},
    {"video_id": "A64",
     "sex": "m",
     "prosody": "meli"},
    {"video_id": "A67",
     "sex": "m",
     "prosody": "meli"},
    {"video_id": "A410",
     "sex": "m",
     "prosody": "meli"},
    {"video_id": "A417",
     "sex": "m",
     "prosody": "meli"},
]


sex_dict = {d['video_id']: d['sex'] for d in video_files}
prosody_dict = {d['video_id']: d['prosody'] for d in video_files}