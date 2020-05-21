import os
import io
import requests

from tqdm import tqdm
import pandas as pd


def get_spreadsheets(key, gid, save_dir, name):
    """スプレッドシートをcsvに保存する関数

    Arguments:
        key {String} -- スプレッドシートのkey
        gid {int} -- スプレッドシートのgid
        save_dir {String} -- 保存するフォルダ
        name {Strin} -- 保存するcsvのファイル名
    """

    if os.path.isdir(save_dir)==False:
        os.makedirs(save_dir)
    
    url = 'https://docs.google.com/spreadsheets/d/{}/export?gid={}&format=csv'.format(key, gid)
    fname = name + '.csv'

    r = requests.get(url)
    df = pd.read_csv(io.BytesIO(r.content))
    df.to_csv(save_dir+"/"+fname, index=False)



if __name__ == "__main__":
    # signateのデータセット
    # https://signate.jp/competitions/260
    # https://drive.google.com/drive/folders/1EcVW5JQKMB6zoyfHm8_zLVj---t_hccF
    signate_targets = {
                '罹患者': ['10MFfRQTblbOpuvOs_yjIYgntpMGBg592dL8veXoPpp4',960903158],
                '罹患者統計': ['10MFfRQTblbOpuvOs_yjIYgntpMGBg592dL8veXoPpp4', 809590826],
                # '罹患者関係': ['1NQ3xrnRi6ta82QtitpJFmIYGvO0wZBmBU5H9EfUGtts', 1227116169],
                # '罹患者トランザクション': ['1_P0kWAJ5XFqP-2xx5JnCtQNYWQdOXvXUxHE-l--hCiQ', 926614575],
                '都道府県マスタ': ['1NQjppYx0QZQmt6706gCOw9DcIDxgnaEy9QTzfeqeMrQ', 1940307536],
                '市区町村マスタ': ['1NQjppYx0QZQmt6706gCOw9DcIDxgnaEy9QTzfeqeMrQ', 1195643752],
                '外国・外国都市マスタ': ['1NQjppYx0QZQmt6706gCOw9DcIDxgnaEy9QTzfeqeMrQ', 936972654],
                '症例マスタ': ['1NQjppYx0QZQmt6706gCOw9DcIDxgnaEy9QTzfeqeMrQ', 1510953868],
                '場所マスタ': ['1NQjppYx0QZQmt6706gCOw9DcIDxgnaEy9QTzfeqeMrQ', 1069933424],
                '職業マスタ': ['1NQjppYx0QZQmt6706gCOw9DcIDxgnaEy9QTzfeqeMrQ', 589312147],
                'トランザクションマスタ': ['1NQjppYx0QZQmt6706gCOw9DcIDxgnaEy9QTzfeqeMrQ', 356513104]
                }

    # けんもねずみ氏のデータセット
    # https://datastudio.google.com/u/0/reporting/c4e0fe88-f72e-464e-a3b8-5e4e591c238d?s=oA3tV-uQzaE
    # https://docs.google.com/spreadsheets/d/1Cy4W9hYhGmABq1GuhLOkM92iYss0qy03Y1GeTv4bCyg/edit#gid=1547889217&range=A1
    kenmo_targets = {
                'positive_list': ['1Cy4W9hYhGmABq1GuhLOkM92iYss0qy03Y1GeTv4bCyg',1196047345],
                'deceased_list': ['1Cy4W9hYhGmABq1GuhLOkM92iYss0qy03Y1GeTv4bCyg', 216648738],
                'positive_num': ['1Cy4W9hYhGmABq1GuhLOkM92iYss0qy03Y1GeTv4bCyg', 2111350392],
                'unknown_num': ['1Cy4W9hYhGmABq1GuhLOkM92iYss0qy03Y1GeTv4bCyg', 776740964],
                'inspection_num': ['1Cy4W9hYhGmABq1GuhLOkM92iYss0qy03Y1GeTv4bCyg', 1641547325],
                'GDS': ['1Cy4W9hYhGmABq1GuhLOkM92iYss0qy03Y1GeTv4bCyg', 845297461],
                'GDS2': ['1Cy4W9hYhGmABq1GuhLOkM92iYss0qy03Y1GeTv4bCyg', 491635333]
                }

    # signate取得
    for name, info in tqdm(signate_targets.items()):
        get_spreadsheets(info[0], info[1], "./signate", name)

    # kenmo取得
    for name, info in tqdm(kenmo_targets.items()):
        get_spreadsheets(info[0], info[1], "./kenmo", name)