response = "INTERNAL:1.00:0.03"

if "INTERNAL" in response:
    newCalib = response.split(":")
    print(newCalib)
    calib_angle = float(newCalib[1]) - float(newCalib[2])
    print(calib_angle, float(newCalib[1]) , float(newCalib[2]))
