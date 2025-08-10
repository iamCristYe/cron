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

# https://sakurazaka46.com/files/14/S46%20Release/12th%20Make%20or%20Break/Sakurazaka46_12th%20Single_Make%20or%20Break_AP_yori.jpg
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

# https://cdn.hinatazaka46.com/files/14/H46%20Release/14th%20Love%20yourself%21/Hinatazaka46_14thSG%20Love%20yourself%21_AP_RGB.jpg
# https://cdn.hinatazaka46.com/files/14/H46%20NEWS/_%E3%82%A2%E3%83%BC%E5%86%99_1127.jpg
# https://cdn.hinatazaka46.com/files/14/H46%20NEWS/12th_Acmyk_0731.jpg
# https://cdn.hinatazaka46.com/files/14/H46%20NEWS/hnt46_11th_asya_FIX_s.jpg
# https://cdn.hinatazaka46.com/files/14/_hnt46_AL_asha_main_0920_%E8%BB%BD.jpg
# https://cdn.hinatazaka46.com/files/14/_h46_10th_asya_0615_FIX_RGB_%E8%BB%BD_2.jpg


base_url = "https://cdn.hinatazaka46.com/files/14/H46%20Release/15th%20お願いバッハ！/"
import itertools

def generate_templates(group, nth, title, shortcode):
    templates = []

    # 基本组合元素
    group_variants = [
        group,
        f"_{group}",
        group.lower(),  # 小写版
        f"_{group.lower()}",
    ]

    nth_variants = [
        f"{nth} Single",
        f"{nth}SG",
        nth,  # 纯数字版
    ]

    title_variants = [
        title,  # 原文
    ]

    # 后缀模式（参考你给的链接）
    suffixes = [
        "_AP_s.jpg", "_AP_S.jpg", "_AP_RGB.jpg", "_AP_s_RGB.jpg", "_AP_S_RGB.jpg",
        "_KV.jpg", "_KV_s.jpg", "_KV_S.jpg", "_KV_new_s.jpg", "_KV_new_S.jpg",
        "_asya_FIX_s.jpg", "_asya_FIX_RGB.jpg",
        "_asha_main.jpg",
        "_asha_main_0920_軽.jpg", "_asha_main_0920_軽_2.jpg",  # 示例
        "_Acmyk_0731.jpg",  # 示例
    ]

    # 1. Group + nth + title + suffix
    for g in group_variants:
        for n in nth_variants:
            for t in title_variants:
                for suf in suffixes:
                    templates.append(f"{g}_{n}_{t}{suf}")
                    templates.append(f"{g}_{n}%20{t}{suf}")  # 空格编码

    # 2. Group + title + suffix (无 nth)
    for g in group_variants:
        for t in title_variants:
            for suf in suffixes:
                templates.append(f"{g}_{t}{suf}")
                templates.append(f"{g}%20{t}{suf}")

    # 3. Shortcode + nth + asya/asha/acmyk 系列
    asya_suffixes = ["_asya_FIX_s.jpg", "_asya_FIX_RGB.jpg"]
    asha_suffixes = ["_asha_main.jpg", "_asha_main_0920_軽.jpg", "_asha_main_0920_軽_2.jpg"]
    acmyk_suffixes = ["_Acmyk_0731.jpg"]

    for suf in asya_suffixes:
        templates.append(f"{shortcode}_{nth}_asya{suf}")

    for suf in asha_suffixes:
        templates.append(f"_{shortcode}_AL_asha{suf}")

    for suf in acmyk_suffixes:
        templates.append(f"{shortcode}_{nth}_Acmyk_0731.jpg")

    return templates


# ==== 使用示例 ====
group = "Hinatazaka46"
nth = "15th"
title = "お願いバッハ！"
shortcode = "hnt46"  # 缩写

templates_without_date = generate_templates(group, nth, title, shortcode)

print(f"共生成 {len(templates_without_date)} 个模板")
for t in templates_without_date:
    print(t)

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
