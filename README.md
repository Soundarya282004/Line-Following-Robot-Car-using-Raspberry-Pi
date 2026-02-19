# Line-Following-Robot-Car-using-Raspberry-Pi
This project builds an autonomous robot car that follows a track made of black lines. The robot uses infrared obstacle/line detection sensors to detect the track and control motor movement. Based on sensor input, the car moves forward, turns left/right, or stops to stay between the lines.

🔌 Hardware Required
- Raspberry Pi
- Motor Driver Module (L298N / L293D)
- 2 DC Motors + Wheels
- Robot Chassis
- 2 IR Line/Obstacle Sensors
- Battery Pack
- Jumper Wires

🔧 GPIO Pin Configuration

<img width="526" height="145" alt="image" src="https://github.com/user-attachments/assets/1ced4f72-bba8-471e-b6e3-004dfde5fbee" />

💻 Software Requirement

RPi.GPIO library (usually preinstalled)

If not:

    pip install RPi.GPIO

▶ How to Run the Code
1️⃣ Save the file

Save as:

    main.py

2️⃣ Connect all hardware

Make sure:

Motors connected to motor driver

Motor driver connected to GPIO pins

IR sensors connected to GPIO 20 and 21

Proper power supply given

3️⃣ Run on Raspberry Pi

    python3 main.py

The robot will start moving automatically based on track detection.

⚙️ How the Robot Works

You can put this under “Working Principle” in GitHub.

🟢 Moving Forward

    forward()

When both sensors are not detecting the line, the car moves forward.

⛔ Stop Condition

    if GPIO.input(OD2) == 1 and GPIO.input(OD1) == 1:
        stop()

If both sensors detect the line (or obstacle), the car stops.

↩ Turning Left
    
    if GPIO.input(OD2):
        stop()
        backward()
        Left()


If the right sensor detects the line, the robot corrects by turning left.

↪ Turning Right

    if GPIO.input(OD1):
        stop()
        backward()
        Right()

If the left sensor detects the line, the robot corrects by turning right.

🔁 Continuous Monitoring

The loop runs forever, checking sensors every 0.5 seconds to stay on track.

🛑 Stopping the Robot

Press:

    CTRL + C
GPIO pins reset safely using:

    GPIO.cleanup()
