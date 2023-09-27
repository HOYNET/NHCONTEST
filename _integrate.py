import pandas as pd

data1: pd.DataFrame = pd.read_csv(
    "/home/lhstar/SKKU/NHContest/data/nadag_stock_data_1.csv"
)
data2: pd.DataFrame = pd.read_csv(
    "/home/lhstar/SKKU/NHContest/data/nadag_stock_data_2.csv"
)
data3: pd.DataFrame = pd.read_csv(
    "/home/lhstar/SKKU/NHContest/data/nadag_stock_data_3.csv"
)
data4: pd.DataFrame = pd.read_csv(
    "/home/lhstar/SKKU/NHContest/data/nadag_stock_data_4.csv"
)

data: pd.DataFrame = pd.concat([data1, data2, data3, data4], axis=0)

print(data.info)

target: pd.DataFrame = pd.read_csv(
    "/home/lhstar/SKKU/NHContest/data/NASDAQ_DT_FC_STK_QUT.csv"
)

print(target.info)

print("----------------------------")
print(data.columns, target.columns)

data = data.rename(
    columns={
        "Date": "trd_dt",
        "Open": "gts_iem_ong_pr",
        "High": "gts_iem_hi_pr",
        "Low": "gts_iem_low_pr",
        "Close": "gts_iem_end_pr",
        "Volume": "gts_acl_trd_qty",
    }
)

target = target.drop(columns=["gts_sll_cns_sum_qty", "gts_byn_cns_sum_qty"])
target["trd_dt"] = pd.to_datetime(target["trd_dt"], format="%Y%m%d")
target["tck_iem_cd"] = target["tck_iem_cd"].str.strip()


data["tck_iem_cd"] = data["tck_iem_cd"].str.strip()
data["trd_dt"] = pd.to_datetime(data["trd_dt"])

data = pd.concat([data, target], axis=0)

print(data[data["tck_iem_cd"] == "AACG"])
data.to_csv("./data/data_0.csv")