import speedtest

speed_test_report = []

def getMySpeed():
    print("###---Started Speed Test---###")
    speedTestHelper = speedtest.Speedtest()
    
    print("###---Choosing best server---###")
    speedTestHelper.get_best_server()

    #Check download speed 
    print("###---Testing Download Speed---###")
    speedTestHelper.download()
    #Check upload speed
    print("###---Testing Upload Speed---###")
    speedTestHelper.upload()

    #generate shareable link
    speedTestHelper.results.share()

    #fetch result
    result = speedTestHelper.results.dict()
    upload_speed = result['download']
    download_speed = result['upload']

    return ["ISP Upload speed is "+str(upload_speed)+"Download speed is "+str(download_speed),result['share']]

def init():
  #Chek Internet Speed
  speed_test_report = getMySpeed()
  print(speed_test_report[0])

  print("Full Result -> " + speed_test_report[1])

if __name__ == '__main__':
    init()
