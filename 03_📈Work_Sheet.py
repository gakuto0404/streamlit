import streamlit as st
import os.path
import pandas as pd
import sqlite3
import time

# Streamlit Setting-------------------------------------
st.set_page_config(
    page_title = "Mfg. System",
    page_icon = "//192.168.1.212//アイシス//01_製造_組立進歩システム//00_作業進歩表//ISIS_Logo.png",
    layout="wide",
    initial_sidebar_state="expanded"
)
# ------------------------------------------------------


# Path を指定-------------------------------------------------------------------------------
cd = os.path.dirname(__file__)
Press_csv  = pd.read_csv(filepath_or_buffer="//192.168.1.212/アイシス/00_製造_自動発注システム/10_Press_No/Press_No.csv", 
                         encoding="ANSI", 
                         sep=",")
Work_schedule_csv  = pd.read_csv('C://Users//tani//Desktop//desktop_python2//作業工程表.csv')
leader_path    = "//192.168.1.212//アイシス//生産管理//会議資料//担当者一覧.xlsx"
BUP_DB_Path ="//192.168.1.212/アイシス/00_製造_自動発注システム/20_DataBase/Auto_Order_Sys.db"

# ページタイトル-----------------------------------------------------------------------------
st.title('Work Sheet')


# -----------------------------------------------------------------------------------------
# Streamlitで遅延理由の記入欄を表示
# -----------------------------
def start_Order_His():
    st.write("<b>絞り込み条件</b>",unsafe_allow_html=True)
    
    cols = st.columns((1, 1, 1))
    work_name = cols[0].selectbox(
        "■ 作業者名を選択してください。",
        ["-","佐野","谷本","猿谷","山崎","原田","浪岡","岸田","小山","若松","今泉","林",]
        )

    cols = st.columns((1, 1, 1))

    date = cols[0].date_input("■ 作業日")

    selected_Press = cols[1].selectbox(
        "■ 機種の絞り込みです。選択してください。",
        ["-",
         "PLENOX series",
         "U series",
         "N series",
         "S・G series",
         "ES series",
         "KIT series",
         "C series",
         "DM series",
         "VIVO series"
         ]
        )
    list_type = list()
    if selected_Press == "PLENOX series":
        P_list_offset = 1
        P_list_read   = 12
    elif selected_Press == "U series":
        P_list_offset = 31
        P_list_read   = 24
    elif selected_Press == "N series":
        P_list_offset = 61
        P_list_read   = 7
    elif selected_Press == "S・G series":
        P_list_offset = 91
        P_list_read   = 11
    elif selected_Press == "ES series":
        P_list_offset = 81
        P_list_read   = 2
    elif selected_Press == "KIT series":
        P_list_offset = 121
        P_list_read   = 3
    elif selected_Press == "C series":
        P_list_offset = 111
        P_list_read   = 4
    elif selected_Press == "DM series":
        P_list_offset = 131
        P_list_read   = 3
    elif selected_Press == "VIVO series":
        P_list_offset = 21
        P_list_read   = 3
    else :
        P_list_offset = 900
        P_list_read   = 5
        
    readmax = P_list_offset + P_list_read
    list_type = Press_csv[P_list_offset:readmax]["1"]
    selected_Press_type = cols[2].selectbox(
        "ー機種を選択してください。",
        list_type   
        )

    Wrok_time = cols[0].time_input("■ かかった時間")

    selected_Work_Item = cols[1].selectbox(
        "■ 作業工程の絞り込みです。選択してください。",
        ["-",
         "ベッド・レッグ",
         "コラム",
         "クラウン・フレーム",
         "クランク",
         "フライホイール",
         "モータ",
         "クラッチ",
         "スライド",
         "ダイナミックバランサー",
         "コネクションユニット",
         "ボルスター",
         "ガイドコラム",
         "配管",
         "仮回し"
         ]
        )
    Work_list_code = list()
    if selected_Work_Item == "ベッド・レッグ":
        W_list_offset = 1
        W_list_read   = 9
    elif selected_Work_Item == "コラム":
        W_list_offset = 21
        W_list_read   = 3
    elif selected_Work_Item == "クラウン・フレーム":
        W_list_offset = 31
        W_list_read   = 6
    elif selected_Work_Item == "クランク":
        W_list_offset = 41
        W_list_read   = 13
    elif selected_Work_Item == "フライホイール":
        W_list_offset = 61
        W_list_read   = 5
    elif selected_Work_Item == "モータ":
        W_list_offset = 71
        W_list_read   = 5
    elif selected_Work_Item == "クラッチ":
        W_list_offset = 81
        W_list_read   = 6
    elif selected_Work_Item == "スライド":
        W_list_offset = 91
        W_list_read   = 13
    elif selected_Work_Item == "ダイナミックバランサー":
        W_list_offset = 111
        W_list_read   = 9
    elif selected_Work_Item == "コネクションユニット":
        W_list_offset = 131
        W_list_read   = 12
    elif selected_Work_Item == "ボルスター":
        W_list_offset = 151
        W_list_read   = 9
    elif selected_Work_Item == "ガイドコラム":
        W_list_offset = 171
        W_list_read   = 5
    elif selected_Work_Item == "配管":
        W_list_offset = 181
        W_list_read   = 12
    elif selected_Work_Item == "仮回し":
        W_list_offset = 201
        W_list_read   = 1
    else :
        W_list_offset = 900
        W_list_read   = 5
        
    readmax = W_list_offset + W_list_read
    Work_list_code = Work_schedule_csv[W_list_offset:readmax]["1"]
    selected_Work = cols[2].selectbox(
        "ー作業工程項目を選択してください。",
        Work_list_code   
        )

    comment = st.text_area("■ コメント")

    S_button1 = st.button("検索")






#以下未変更
# ----------------------------------------------------
        
    # ----------------------------------------------------
    # Main Screen
    # ----------------------------------------------------
    if S_button1 == False:
        st.info("検索ボタンを押してください。")
        #st.info("検索ボタンを押してください。", icon="ℹ️")
    
    if S_button1 == True:
        with st.spinner('Wait for it...'):
            time.sleep(2)
        db_sys = Auto_Order_Database()
        db_data = db_sys.get(
                selected_Press,
                selected_Press_type,
            )
        db_sys.close()
              
        styles = [
            dict(selector="th", props=[("font-size", "150%"),
                               ("text-align", "center")])
                ]
        
        # データが存在しないときはエラー表記
        if db_data.empty :
            st.error("SQLにデータが存在しません🥺")
            st.stop()
        
        # カーソル無
        #st.table(db_data)
        
        # カーソル有
        st.dataframe(db_data,2500, 1300)
        

   # -----------------------------------------------------------------------------------------
# 自動発注履歴をSQLから取得
# -----------------------------
class Auto_Order_Database:
    # 初期化=====================================================================
    def __init__(self):
        self.conn   = sqlite3.connect(BUP_DB_Path, check_same_thread=False)
        self.cur    = self.conn.cursor()
        self.table  = []
    #===========================================================================
    
    # データ取得=================================================================
    def get(self, db_press, db_press_type):    
    
        if db_press == "-":
            logic1 = "or"
        else:
            logic1 = "and"
        
        
        if db_press == "-":
            sql_text = ""
        else:
            sql_text =f"""
            where 
            Press_Type = "{db_press_type}" {logic1}
            """
            
        sql_read = f""" SELECT * FROM OT {sql_text} """
        df = pd.read_sql(sql_read, self.conn)
        return df
    #===========================================================================
    
    # SQLを閉じる================================================================
    def close(self):
        self.cur.close()
        self.conn.close()
    #===========================================================================
        

#===========================================================================================
# Main Program
#===========================================================================================

start_Order_His()