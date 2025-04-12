import requests
from datetime import datetime, timedelta

# 日期范围
start_date = datetime(2025, 3, 30)
end_date = datetime(2025, 4, 12)
dates = [
    (start_date + timedelta(days=i)).strftime("%m%d")
    for i in range((end_date - start_date).days + 1)
]

base_url = "https://cdn.hinatazaka46.com/files/14/H46%20NEWS/"

# 无日期模板（已加入更多可能组合）
templates_without_date = [
    "hnt46_14th_asya_FIX_s.jpg",
    "hnt46_14th_asya_FIX.jpg",
    "hnt46_14th_asya_fix.jpg",
    "hnt46_14th_asya.jpg",
    "hnt46_asya_FIX_s.jpg",
    "hnt46_asya_FIX.jpg",
    "hnt46_asya.jpg",
    "14th_asya_FIX.jpg",
    "14th_asya.jpg",
    "14th.jpg",
    "_14th.jpg",
    "_asya_FIX_s.jpg",
    "_asya_FIX.jpg",
    "_asya.jpg",
    "asya_FIX.jpg",
    "asya.jpg",
    "アー写.jpg",
    "アー写_FIX.jpg",
    "アー写_FIX_s.jpg",
    "14th_アー写.jpg",
    "14th_アー写_FIX.jpg",
    "_14th_アー写.jpg",
    "_アー写.jpg",
    "_アー写_FIX.jpg",
    "hnt46_アー写.jpg",
    "hnt46_アー写_FIX.jpg",
    "hnt46_アー写_14th.jpg",
    "hnt46_14th_アー写.jpg",
    "hnt46_14th_main.jpg",
    "hnt46_14th.jpg",
    "hnt46_14.jpg",
    "hnt46_FIX.jpg",
    "HNT_14th.jpg",
    "ア写.jpg",
    "hnt46_ア写.jpg",
    "hnt46_ア写_FIX.jpg",
]

# 有日期模板（加入更多变体）
templates_with_date = [
    "_アー写_{date}.jpg",
    "アー写_14th_{date}.jpg",
    "14th_asya_{date}.jpg",
    "14th_Asya_FIX_{date}.jpg",
    "14th_Acmyk_{date}.jpg",
    "14th_{date}.jpg",
    "_14th_{date}.jpg",
    "hnt46_14th_{date}.jpg",
    "hnt46_14th_main_{date}.jpg",
    "{date}_14th_asya.jpg",
    "{date}_14th_main.jpg",
    "hnt46_アー写_14th_{date}.jpg",
    "hnt46_アー写_FIX_{date}.jpg",
    "HNT_14th_{date}.jpg",
    "asya_FIX_{date}.jpg",
    "asya_{date}.jpg",
    "_asya_{date}.jpg",
    "_asya_FIX_{date}.jpg",
    "アー写_{date}.jpg",
    "アー写_FIX_{date}.jpg",
    "_アー写14th_{date}.jpg",
    "hnt46_asya_{date}.jpg",
    "hnt46_asya_FIX_{date}.jpg",
    "hnt46_FIX_{date}.jpg",
    "_FIX_{date}.jpg",
    "14th_アー写_{date}.jpg",
    "14th_asya_FIX_s_{date}.jpg",
    "hnt46_asya_FIX_s_{date}.jpg",
    "asya_FIX_s_{date}.jpg",
    "14th_asya_s_{date}.jpg",
    "hnt46_ア写_{date}.jpg",
    "hnt46_ア写_FIX_{date}.jpg",
]

# 请求检测
def check_url(url):
    try:
        response = requests.head(url, timeout=15)
        return response.status_code == 200
    except Exception as e:
        print(f"⚠️ 请求失败: {url} -> {e}")
        return False

# 测试无日期模板
print("🔍 [Step 1] 尝试不含日期的文件名...")
for filename in templates_without_date:
    full_url = base_url + filename
    print(f"尝试中: {full_url}")
    if check_url(full_url):
        print(f"\n✅ 找到有效链接: {full_url}")
        exit(0)

# 测试有日期模板
print("🔍 [Step 2] 尝试含日期的文件名...")
for date in dates:
    for tpl in templates_with_date:
        filename = tpl.format(date=date)
        full_url = base_url + filename
        print(f"尝试中: {full_url}")
        if check_url(full_url):
            print(f"\n✅ 找到有效链接: {full_url}")
            exit(0)

print("\n🛑 全部尝试完毕，未找到有效链接。")
