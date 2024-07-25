# Thresholds
IMG_SIZE_THRESHOLD = 3500 # This can be pixel^2 because it also shows image resolution
OCR_CONF_THRESHOLD = 0.4
YBBOX_DIS_THRESHOLD = 0.15 # This one and below should be fraction because not all images have same resolution
XBBOX_DIS_THRESHOLD = 0.2

# Positions
PLATE_NUM_XPOS = 0.5
PLATE_NUM_YPOS = 0.33
PLATE_PRO_XPOS = 0.5
PLATE_PRO_YPOS = 0.85

# Provinces
PROVINCES = [
    "กรุงเทพมหานคร", "กระบี่", "กาญจนบุรี", "กาฬสินธุ์", "กำแพงเพชร",
    "ขอนแก่น", "จันทบุรี", "ฉะเชิงเทรา", "ชลบุรี", "ชัยนาท",
    "ชัยภูมิ", "ชุมพร", "เชียงใหม่", "เชียงราย", "ตรัง",
    "ตราด", "ตาก", "นครนายก", "นครปฐม", "นครพนม",
    "นครราชสีมา", "นครศรีธรรมราช", "นครสวรรค์", "นนทบุรี", "นราธิวาส",
    "น่าน", "บึงกาฬ", "บุรีรัมย์", "ปทุมธานี", "ประจวบคีรีขันธ์",
    "ปราจีนบุรี", "ปัตตานี", "พะเยา", "พังงา", "พัทลุง",
    "พิจิตร", "พิษณุโลก", "เพชรบุรี", "เพชรบูรณ์", "แพร่", "ภูเก็ต", "มหาสารคาม", "มุกดาหาร", "แม่ฮ่องสอน",
    "ยโสธร", "ยะลา", "ร้อยเอ็ด", "ระนอง",
    "ระยอง", "ราชบุรี", "ลพบุรี", "ลำปาง", "ลำพูน",
    "เลย", "ศรีสะเกษ", "สกลนคร", "สระแก้ว", "สมุทรปราการ","สมุทรสงคราม","สมุทรสาคร",
    "สุโขทัย", "สุพรรณบุรี", "สุรินทร์", "สุราษฎร์ธานี", "สตูล",
    "สงขลา", "สิงห์บุรี", "สระบุรี","หนองคาย","หนองบัวลำภู", "อ่างทอง", "อำนาจเจริญ", "อุดรธานี", "อยุธยา"
    "อุตรดิตถ์", "อุทัยธานี", "อุบลราชธานี"
]
PROVINCES_TO_THAI = {
    "amnat_charoen": "อำนาจเจริญ",
    "ang_thong": "อ่างทอง",
    "bangkok": "กรุงเทพมหานคร",
    "bueng_kan": "บึงกาฬ",
    "buriram": "บุรีรัมย์",
    "chachoengsao": "ฉะเชิงเทรา",
    "chai_nat": "ชัยนาท",
    "chaiyaphum": "ชัยภูมิ",
    "chanthaburi": "จันทบุรี",
    "chiang_mai": "เชียงใหม่",
    "chiang_rai": "เชียงราย",
    "chonburi": "ชลบุรี",
    "chumphon": "ชุมพร",
    "kalasin": "กาฬสินธุ์",
    "kamphaeng_phet": "กำแพงเพชร",
    "kanchanaburi": "กาญจนบุรี",
    "khon_kaen": "ขอนแก่น",
    "krabi": "กระบี่",
    "lampang": "ลำปาง",
    "lamphun": "ลำพูน",
    "loei": "เลย",
    "lopburi": "ลพบุรี",
    "mae_hong_son": "แม่ฮ่องสอน",
    "maha_sarakham": "มหาสารคาม",
    "mukdahan": "มุกดาหาร",
    "nakhon_nayok": "นครนายก",
    "nakhon_pathom": "นครปฐม",
    "nakhon_phanom": "นครพนม",
    "nakhon_ratchasima": "นครราชสีมา",
    "nakhon_sawan": "นครสวรรค์",
    "nakhon_si_thammarat": "นครศรีธรรมราช",
    "nan": "น่าน",
    "narathiwat": "นราธิวาส",
    "nong_bua_lam_phu": "หนองบัวลำภู",
    "nong_khai": "หนองคาย",
    "nonthaburi": "นนทบุรี",
    "pathum_thani": "ปทุมธานี",
    "pattani": "ปัตตานี",
    "phang_nga": "พังงา",
    "phatthalung": "พัทลุง",
    "phayao": "พะเยา",
    "phetchabun": "เพชรบูรณ์",
    "phetchaburi": "เพชรบุรี",
    "phichit": "พิจิตร",
    "phitsanulok": "พิษณุโลก",
    "phra_nakhon_si_ayutthaya": "พระนครศรีอยุธยา",
    "phrae": "แพร่",
    "phuket": "ภูเก็ต",
    "prachinburi": "ปราจีนบุรี",
    "prachuap_khiri_khan": "ประจวบคีรีขันธ์",
    "ranong": "ระนอง",
    "ratchaburi": "ราชบุรี",
    "rayong": "ระยอง",
    "roi_et": "ร้อยเอ็ด",
    "sa_kaeo": "สระแก้ว",
    "sakon_nakhon": "สกลนคร",
    "samut_prakan": "สมุทรปราการ",
    "samut_sakhon": "สมุทรสาคร",
    "samut_songkhram": "สมุทรสงคราม",
    "saraburi": "สระบุรี",
    "satun": "สตูล",
    "si_sa_ket": "ศรีสะเกษ",
    "sing_buri": "สิงห์บุรี",
    "songkhla": "สงขลา",
    "sukhothai": "สุโขทัย",
    "suphanburi": "สุพรรณบุรี",
    "surat_thani": "สุราษฎร์ธานี",
    "surin": "สุรินทร์",
    "tak": "ตาก",
    "trang": "ตรัง",
    "trat": "ตราด",
    "ubon_ratchathani": "อุบลราชธานี",
    "udon_thani": "อุดรธานี",
    "uthai_thani": "อุทัยธานี",
    "uttaradit": "อุตรดิตถ์",
    "yala": "ยะลา",
    "yasothon": "ยโสธร"
}


# Letter Recognition
LETTER_INDEX = {0: '0', 1: '1', 2: 'ก', 3: 'ข', 4: 'ค', 5: 'ฆ', 6: 'ง', 7: 'จ', 8: 'ฉ', 9: 'ช', 10: 'ฌ', 11: 'ญ', 12: '2', 13: 'ฎ', 14: 'ฐ', 15: 'ฒ', 16: 'ณ', 17: 'ด', 18: 'ต', 19: 'ถ', 20: 'ท', 21: 'ธ', 22: 'น', 23: '3', 24: 'บ', 25: 'ผ', 26: 'พ', 27: 'ฟ', 28: 'ภ', 29: 'ม', 30: 'ย', 31: 'ร', 32: 'ล', 33: 'ว', 34: '4', 35: 'ศ', 36: 'ษ', 37: 'ส', 38: 'ห', 39: 'ฬ', 40: 'อ', 41: 'ฮ', 42: '5', 43: '6', 44: '7', 45: '8', 46: '9'}