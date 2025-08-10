import requests
from datetime import datetime, timedelta

# 日期范围
start_date = datetime(2025, 3, 30)
end_date = datetime(2025, 4, 14)
release_date = datetime(2025, 5, 21)

dates = [
    start_date + timedelta(days=i) for i in range((end_date - start_date).days + 1)
]
dates.append(release_date)  # 添加发售日


# https://sakurazaka46.com/files/14/S46%20Release/11th%20UDAGAWA%20GENERATION/Sakurazaka46_11th%20Single_UDAGAWA%20GENERATION_AP_s.jpg
# https://sakurazaka46.com/files/14/S46%20Release/10th%20I%20want%20tomorrow%20to%20come/Sakurazaka46_10th%20Single_I%20want%20tomorrow%20to%20come_AP_s.jpg
# sakurazaka46.com/files/14/S46%20Release/9th%20自業自得/_Sakurazaka46_9th%20Single_自業自得_AP_s.jpg
# sakurazaka46.com/files/14/S46%20Release/8th%20何歳の頃に戻りたいのか？/_Sakurazaka46_8th%20Single_何歳の頃に戻りたいのか？_AP_s.jpg
# sakurazaka46.com/files/14/S46%20Release/7th%20承認欲求/_Sakurazaka46_7th%20Single_承認欲求_AP_s.jpg
# sakurazaka46.com/files/14/S46%20Release/6th%20Start%20over%21/Sakurazaka46_6th%20Single_start%20over%21_AP_S.jpg
# sakurazaka46.com/files/14/S46%20Release/5th%20桜月/_Sakurazaka46_5th%20Single%20桜月_AP_s.jpg
# sakurazaka46.com/files/14/S46%20Release/4th%20五月雨よ/_Sakurazaka46_4th_五月雨よ_KV_new_S.jpg
# sakurazaka46.com/files/14/sakurazaka46_kv_3rdsingle.jpg
# sakurazaka46.com/files/14/sakurazaka46_BAN_KV.jpg
# sakurazaka46.com/files/14/sakurazaka_Nobody%27s%20fault_KV_s.jpg


base_url = "https://sakurazaka46.com/files/14/S46%20Release/12th%20Make%20or%20Break/"

templates_without_date = [
  "_AP_s.jpg",
    "_AP_S.jpg",
    "_AP_RGB.jpg",
    "_AP_s_RGB.jpg",
    "_AP_S_RGB.jpg",
    "AP_s.jpg",
    "AP_S.jpg",
    "AP_RGB.jpg",
    "AP_s_RGB.jpg",
    "AP_S_RGB.jpg",
    "s.jpg",
    "S.jpg",
    "RGB.jpg",
    "s_RGB.jpg",
    "S_RGB.jpg",
    "12th%20Single_AP_s.jpg",
    "12th%20Single_AP_S.jpg",
    "12th%20Single_AP_RGB.jpg",
    "12th%20Single_AP_s_RGB.jpg",
    "12th%20Single_AP_S_RGB.jpg",
    "12th%20Single_AP_s.jpg",
    "12th%20Single_AP_S.jpg",
    "12th%20Single_AP_RGB.jpg",
    "12th%20Single_AP_s_RGB.jpg",
    "12th%20Single_AP_S_RGB.jpg",
    "12th%20Single_s.jpg",
    "12th%20Single_S.jpg",
    "12th%20Single_RGB.jpg",
    "12th%20Single_s_RGB.jpg",
    "12th%20Single_S_RGB.jpg",
    "Make%20or%20Break_AP_s.jpg",
    "Make%20or%20Break_AP_S.jpg",
    "Make%20or%20Break_AP_RGB.jpg",
    "Make%20or%20Break_AP_s_RGB.jpg",
    "Make%20or%20Break_AP_S_RGB.jpg",
    "Make%20or%20Break_AP_s.jpg",
    "Make%20or%20Break_AP_S.jpg",
    "Make%20or%20Break_AP_RGB.jpg",
    "Make%20or%20Break_AP_s_RGB.jpg",
    "Make%20or%20Break_AP_S_RGB.jpg",
    "Make%20or%20Break_s.jpg",
    "Make%20or%20Break_S.jpg",
    "Make%20or%20Break_RGB.jpg",
    "Make%20or%20Break_s_RGB.jpg",
    "Make%20or%20Break_S_RGB.jpg",
    "12th%20Single_Make%20or%20Break_AP_s.jpg",
    "12th%20Single_Make%20or%20Break_AP_S.jpg",
    "12th%20Single_Make%20or%20Break_AP_RGB.jpg",
    "12th%20Single_Make%20or%20Break_AP_s_RGB.jpg",
    "12th%20Single_Make%20or%20Break_AP_S_RGB.jpg",
    "12th%20Single_Make%20or%20Break_AP_s.jpg",
    "12th%20Single_Make%20or%20Break_AP_S.jpg",
    "12th%20Single_Make%20or%20Break_AP_RGB.jpg",
    "12th%20Single_Make%20or%20Break_AP_s_RGB.jpg",
    "12th%20Single_Make%20or%20Break_AP_S_RGB.jpg",
    "12th%20Single_Make%20or%20Break_s.jpg",
    "12th%20Single_Make%20or%20Break_S.jpg",
    "12th%20Single_Make%20or%20Break_RGB.jpg",
    "12th%20Single_Make%20or%20Break_s_RGB.jpg",
    "12th%20Single_Make%20or%20Break_S_RGB.jpg",
    "__AP_s.jpg",
    "__AP_S.jpg",
    "__AP_RGB.jpg",
    "__AP_s_RGB.jpg",
    "__AP_S_RGB.jpg",
    "_AP_s.jpg",
    "_AP_S.jpg",
    "_AP_RGB.jpg",
    "_AP_s_RGB.jpg",
    "_AP_S_RGB.jpg",
    "_s.jpg",
    "_S.jpg",
    "_RGB.jpg",
    "_s_RGB.jpg",
    "_S_RGB.jpg",
    "_12th%20Single_AP_s.jpg",
    "_12th%20Single_AP_S.jpg",
    "_12th%20Single_AP_RGB.jpg",
    "_12th%20Single_AP_s_RGB.jpg",
    "_12th%20Single_AP_S_RGB.jpg",
    "_12th%20Single_AP_s.jpg",
    "_12th%20Single_AP_S.jpg",
    "_12th%20Single_AP_RGB.jpg",
    "_12th%20Single_AP_s_RGB.jpg",
    "_12th%20Single_AP_S_RGB.jpg",
    "_12th%20Single_s.jpg",
    "_12th%20Single_S.jpg",
    "_12th%20Single_RGB.jpg",
    "_12th%20Single_s_RGB.jpg",
    "_12th%20Single_S_RGB.jpg",
    "_Make%20or%20Break_AP_s.jpg",
    "_Make%20or%20Break_AP_S.jpg",
    "_Make%20or%20Break_AP_RGB.jpg",
    "_Make%20or%20Break_AP_s_RGB.jpg",
    "_Make%20or%20Break_AP_S_RGB.jpg",
    "_Make%20or%20Break_AP_s.jpg",
    "_Make%20or%20Break_AP_S.jpg",
    "_Make%20or%20Break_AP_RGB.jpg",
    "_Make%20or%20Break_AP_s_RGB.jpg",
    "_Make%20or%20Break_AP_S_RGB.jpg",
    "_Make%20or%20Break_s.jpg",
    "_Make%20or%20Break_S.jpg",
    "_Make%20or%20Break_RGB.jpg",
    "_Make%20or%20Break_s_RGB.jpg",
    "_Make%20or%20Break_S_RGB.jpg",
    "_12th%20Single_Make%20or%20Break_AP_s.jpg",
    "_12th%20Single_Make%20or%20Break_AP_S.jpg",
    "_12th%20Single_Make%20or%20Break_AP_RGB.jpg",
    "_12th%20Single_Make%20or%20Break_AP_s_RGB.jpg",
    "_12th%20Single_Make%20or%20Break_AP_S_RGB.jpg",
    "_12th%20Single_Make%20or%20Break_AP_s.jpg",
    "_12th%20Single_Make%20or%20Break_AP_S.jpg",
    "_12th%20Single_Make%20or%20Break_AP_RGB.jpg",
    "_12th%20Single_Make%20or%20Break_AP_s_RGB.jpg",
    "_12th%20Single_Make%20or%20Break_AP_S_RGB.jpg",
    "_12th%20Single_Make%20or%20Break_s.jpg",
    "_12th%20Single_Make%20or%20Break_S.jpg",
    "_12th%20Single_Make%20or%20Break_RGB.jpg",
    "_12th%20Single_Make%20or%20Break_s_RGB.jpg",
    "_12th%20Single_Make%20or%20Break_S_RGB.jpg",
    "Sakurazaka46_AP_s.jpg",
    "Sakurazaka46_AP_S.jpg",
    "Sakurazaka46_AP_RGB.jpg",
    "Sakurazaka46_AP_s_RGB.jpg",
    "Sakurazaka46_AP_S_RGB.jpg",
    "Sakurazaka46_AP_s.jpg",
    "Sakurazaka46_AP_S.jpg",
    "Sakurazaka46_AP_RGB.jpg",
    "Sakurazaka46_AP_s_RGB.jpg",
    "Sakurazaka46_AP_S_RGB.jpg",
    "Sakurazaka46_s.jpg",
    "Sakurazaka46_S.jpg",
    "Sakurazaka46_RGB.jpg",
    "Sakurazaka46_s_RGB.jpg",
    "Sakurazaka46_S_RGB.jpg",
    "Sakurazaka46_12th%20Single_AP_s.jpg",
    "Sakurazaka46_12th%20Single_AP_S.jpg",
    "Sakurazaka46_12th%20Single_AP_RGB.jpg",
    "Sakurazaka46_12th%20Single_AP_s_RGB.jpg",
    "Sakurazaka46_12th%20Single_AP_S_RGB.jpg",
    "Sakurazaka46_12th%20Single_AP_s.jpg",
    "Sakurazaka46_12th%20Single_AP_S.jpg",
    "Sakurazaka46_12th%20Single_AP_RGB.jpg",
    "Sakurazaka46_12th%20Single_AP_s_RGB.jpg",
    "Sakurazaka46_12th%20Single_AP_S_RGB.jpg",
    "Sakurazaka46_12th%20Single_s.jpg",
    "Sakurazaka46_12th%20Single_S.jpg",
    "Sakurazaka46_12th%20Single_RGB.jpg",
    "Sakurazaka46_12th%20Single_s_RGB.jpg",
    "Sakurazaka46_12th%20Single_S_RGB.jpg",
    "Sakurazaka46_Make%20or%20Break_AP_s.jpg",
    "Sakurazaka46_Make%20or%20Break_AP_S.jpg",
    "Sakurazaka46_Make%20or%20Break_AP_RGB.jpg",
    "Sakurazaka46_Make%20or%20Break_AP_s_RGB.jpg",
    "Sakurazaka46_Make%20or%20Break_AP_S_RGB.jpg",
    "Sakurazaka46_Make%20or%20Break_AP_s.jpg",
    "Sakurazaka46_Make%20or%20Break_AP_S.jpg",
    "Sakurazaka46_Make%20or%20Break_AP_RGB.jpg",
    "Sakurazaka46_Make%20or%20Break_AP_s_RGB.jpg",
    "Sakurazaka46_Make%20or%20Break_AP_S_RGB.jpg",
    "Sakurazaka46_Make%20or%20Break_s.jpg",
    "Sakurazaka46_Make%20or%20Break_S.jpg",
    "Sakurazaka46_Make%20or%20Break_RGB.jpg",
    "Sakurazaka46_Make%20or%20Break_s_RGB.jpg",
    "Sakurazaka46_Make%20or%20Break_S_RGB.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_AP_s.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_AP_S.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_AP_RGB.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_AP_s_RGB.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_AP_S_RGB.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_AP_s.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_AP_S.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_AP_RGB.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_AP_s_RGB.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_AP_S_RGB.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_s.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_S.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_RGB.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_s_RGB.jpg",
    "Sakurazaka46_12th%20Single_Make%20or%20Break_S_RGB.jpg",
    "_Sakurazaka46_AP_s.jpg",
    "_Sakurazaka46_AP_S.jpg",
    "_Sakurazaka46_AP_RGB.jpg",
    "_Sakurazaka46_AP_s_RGB.jpg",
    "_Sakurazaka46_AP_S_RGB.jpg",
    "_Sakurazaka46_AP_s.jpg",
    "_Sakurazaka46_AP_S.jpg",
    "_Sakurazaka46_AP_RGB.jpg",
    "_Sakurazaka46_AP_s_RGB.jpg",
    "_Sakurazaka46_AP_S_RGB.jpg",
    "_Sakurazaka46_s.jpg",
    "_Sakurazaka46_S.jpg",
    "_Sakurazaka46_RGB.jpg",
    "_Sakurazaka46_s_RGB.jpg",
    "_Sakurazaka46_S_RGB.jpg",
    "_Sakurazaka46_12th%20Single_AP_s.jpg",
    "_Sakurazaka46_12th%20Single_AP_S.jpg",
    "_Sakurazaka46_12th%20Single_AP_RGB.jpg",
    "_Sakurazaka46_12th%20Single_AP_s_RGB.jpg",
    "_Sakurazaka46_12th%20Single_AP_S_RGB.jpg",
    "_Sakurazaka46_12th%20Single_AP_s.jpg",
    "_Sakurazaka46_12th%20Single_AP_S.jpg",
    "_Sakurazaka46_12th%20Single_AP_RGB.jpg",
    "_Sakurazaka46_12th%20Single_AP_s_RGB.jpg",
    "_Sakurazaka46_12th%20Single_AP_S_RGB.jpg",
    "_Sakurazaka46_12th%20Single_s.jpg",
    "_Sakurazaka46_12th%20Single_S.jpg",
    "_Sakurazaka46_12th%20Single_RGB.jpg",
    "_Sakurazaka46_12th%20Single_s_RGB.jpg",
    "_Sakurazaka46_12th%20Single_S_RGB.jpg",
    "_Sakurazaka46_Make%20or%20Break_AP_s.jpg",
    "_Sakurazaka46_Make%20or%20Break_AP_S.jpg",
    "_Sakurazaka46_Make%20or%20Break_AP_RGB.jpg",
    "_Sakurazaka46_Make%20or%20Break_AP_s_RGB.jpg",
    "_Sakurazaka46_Make%20or%20Break_AP_S_RGB.jpg",
    "_Sakurazaka46_Make%20or%20Break_AP_s.jpg",
    "_Sakurazaka46_Make%20or%20Break_AP_S.jpg",
    "_Sakurazaka46_Make%20or%20Break_AP_RGB.jpg",
    "_Sakurazaka46_Make%20or%20Break_AP_s_RGB.jpg",
    "_Sakurazaka46_Make%20or%20Break_AP_S_RGB.jpg",
    "_Sakurazaka46_Make%20or%20Break_s.jpg",
    "_Sakurazaka46_Make%20or%20Break_S.jpg",
    "_Sakurazaka46_Make%20or%20Break_RGB.jpg",
    "_Sakurazaka46_Make%20or%20Break_s_RGB.jpg",
    "_Sakurazaka46_Make%20or%20Break_S_RGB.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_AP_s.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_AP_S.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_AP_RGB.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_AP_s_RGB.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_AP_S_RGB.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_AP_s.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_AP_S.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_AP_RGB.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_AP_s_RGB.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_AP_S_RGB.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_s.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_S.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_RGB.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_s_RGB.jpg",
    "_Sakurazaka46_12th%20Single_Make%20or%20Break_S_RGB.jpg"
]
# https://cdn.hinatazaka46.com/files/14/H46%20Release/14th%20Love%20yourself%21/Hinatazaka46_14thSG%20Love%20yourself%21_AP_RGB.jpg
# https://cdn.hinatazaka46.com/files/14/H46%20NEWS/_%E3%82%A2%E3%83%BC%E5%86%99_1127.jpg
# https://cdn.hinatazaka46.com/files/14/H46%20NEWS/12th_Acmyk_0731.jpg
# https://cdn.hinatazaka46.com/files/14/H46%20NEWS/hnt46_11th_asya_FIX_s.jpg
# https://cdn.hinatazaka46.com/files/14/_hnt46_AL_asha_main_0920_%E8%BB%BD.jpg
# https://cdn.hinatazaka46.com/files/14/_h46_10th_asya_0615_FIX_RGB_%E8%BB%BD_2.jpg
templates_with_date = [
    "{date_yymmdd}_hnt46_14th_asya_FIX.jpg",
    "{date_yymmdd}_hnt46_asya_FIX.jpg",
    "{date_yymmdd}_asya.jpg",
    "{date_yymmdd}_14th_asya.jpg",
    "{date_yymmdd}_アー写.jpg",
    "{date_yymmdd}_14th.jpg",
    "{date_yymmdd}_FIX.jpg",
    "{date_yymmdd}_hnt46_FIX.jpg",
    "asya_FIX_{date}.jpg",
    "asya_{date}.jpg",
    "_asya_{date}.jpg",
    "_asya_FIX_{date}.jpg",
    "アー写_{date}.jpg",
    "アー写_FIX_{date}.jpg",
    "_アー写_{date}.jpg",
    "_アー写14th_{date}.jpg",
    "hnt46_asya_{date}.jpg",
    "hnt46_asya_FIX_{date}.jpg",
    "hnt46_FIX_{date}.jpg",
    "_FIX_{date}.jpg",
    "14th_asya_{date}.jpg",
    "14th_Asya_FIX_{date}.jpg",
    "14th_{date}.jpg",
    "hnt46_14th_main_{date}.jpg",
    "14th_asya_FIX_s_{date}.jpg",
    "hnt46_asya_FIX_s_{date}.jpg",
    "asya_FIX_s_{date}.jpg",
    "14th_asya_s_{date}.jpg",
    "hnt46_ア写_{date}.jpg",
    "hnt46_ア写_FIX_{date}.jpg",
    "14th_アー写_{date}.jpg",
    "HNT_14th_{date}.jpg",
    "hnt46_アー写_14th_{date}.jpg",
    "hnt46_アー写_FIX_{date}.jpg",
    "ア写_{date}.jpg",
]


def check_url(url):
    try:
        response = requests.head(url, timeout=15)
        return response.status_code == 200
    except Exception as e:
        print(f"⚠️ 请求失败: {url} -> {e}")
        return False


# Step 1: 不含日期
print("🔍 [Step 1] 尝试不含日期的文件名...")
for filename in templates_without_date:
    full_url = base_url + filename
    print(f"尝试中: {full_url}")
    if check_url(full_url):
        print(f"\n✅ 找到有效链接: {full_url}")
        exit(0)

# Step 2: 含日期
# print("🔍 [Step 2] 尝试含日期的文件名（任意位置）...")
# for date_obj in dates:
#     date = date_obj.strftime("%m%d")
#     date_yymmdd = date_obj.strftime("%y%m%d")
#     for tpl in templates_with_date:
#         filename = tpl.format(date=date, date_yymmdd=date_yymmdd)
#         full_url = base_url + filename
#         print(f"尝试中: {full_url}")
#         if check_url(full_url):
#             print(f"\n✅ 找到有效链接: {full_url}")
#             exit(0)

print("\n🛑 全部尝试完毕，未找到有效链接。")
