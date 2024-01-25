import boto3
import os
import time
from pathlib import Path

example_videos = {
    "2": "A332_det_v_2.mp4",
    "25": "A205_pea_v_2.mp4",
    "33": "A55_hap_p_2.mp4",
    "20": "A227_tri_p_2.mp4",
    "18": "A323_awe_p_3.mp4",
    "29": "A437_int_v_2.mp4",
    "19": "A327_ins_v_2.mp4",
    "24": "A67_sex_p_3.mp4",
    "27": "A221_conc_p_3.mp4",
    "38": "A64_rel_v_2.mp4",
    "21": "A334_hop_v_3.mp4",
    "22": "A407_neu_sit1_v.mp4",
    "7": "A55_gra_p_3_ver1.mp4",
    "13": "A410_amu_v_3.mp4",
    "36": "A55_exc_v_3.mp4",
    "28": "A435_ten_p_3.mp4",
    "5": "A425_adm_v_3.mp4",
    "42": "A437_mov_v_3.mp4",
    "41": "A337_pri_v_3.mp4",
    "8": "A205_ele_p_3.mp4",
    "9": "A327_pos_sur_p_2.mp4",
    "23": "A438_ple_v_2.mp4",
    "16": "A102_sat_v_3.mp4",
    "10": "A334_fea_p_3.mp4",
    "34": "A227_anx_v_2.mp4",
    "15": "A417_scha_p_2.mp4",
    "17": "A410_dist_v_3.mp4",
    "4": "A337_env_p_2.mp4",
    "39": "A303_emb_p_2.mp4",
    "12": "A55_ang_p_2.mp4",
    "30": "A205_nos_p_2.mp4",
    "14": "A426_rej_p_2.mp4",
    "43": "A405_sha_p_2.mp4",
    "0": "A303_reg_p_2.mp4",
    "32": "A426_cont_v_3.mp4",
    "35": "A334_disg_p_2.mp4",
    "6": "A437_sad_p_3.mp4",
    "37": "A220_disa_v_2.mp4",
    "31": "A200_sar_v_3.mp4",
    "11": "A337_neg_sur_p_2.mp4",
    "26": "A221_bor_p_3.mp4",
    "40": "A337_gui_p_2.mp4",
    "3": "A405_dou_v_2.mp4"
}

t1 = time.time()

session = boto3.Session(profile_name='rackspaceAcc')

s3_client = session.client('s3')

bucket_name = 'mainstack-videofiles720pc366226e-haxvasmgqgdh'


def list_objects(bucket, continuation_token=None):
    if continuation_token:
        resp = s3_client.list_objects_v2(Bucket=bucket, ContinuationToken=continuation_token)
    else:
        resp = s3_client.list_objects_v2(Bucket=bucket)
    return resp


keys = []
token = None
while True:
    response = list_objects(bucket_name, token)
    keys.extend([obj['Key'] for obj in response.get('Contents', [])])

    # Check if more objects are available
    if response.get('IsTruncated'):
        token = response.get('NextContinuationToken')
    else:
        break

t2 = time.time()

print(len(keys))

print(f'Elapsed time: {t2 - t1}')

for val in example_videos.values():
    if val in keys:
        print(val)
