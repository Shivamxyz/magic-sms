target = 9876448998
# Credits to Ansh Dadwal
target = str(target)
true = "true"
false = "false"

apidata = {

"Byjus":("https://mtnucleus.byjusweb.com/api/acs/v2/send-otp",{"phoneNumber":target,"page":"free-trial-classes"},{},"POST","""{"isOtpExhausted":false,"""),

"Rummycircle":(f"https://www.rummycircle.com/api/fl/auth/v3/getOtp",{"mobile":target,"deviceId":"d6be3862-7659-46c0-98b9-3d13328a243c","deviceName":"","refCode":"","isPlaycircle":"false"},{},"POST",'''success":true'''),

"lona":(f"https://www.loanbaba.com/sdgpeknj/MAppService.asmx/SendOTPonCall",{"phoneNo":f"str(target)"},{"Content-Type":"application/json"},"POST","200")


}


apis = [

apidata["Byjus"],
apidata["Rummycircle"],
apidata["lona"]
]
