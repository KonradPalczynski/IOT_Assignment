# IOT Assignment
Reaction Time Game

This project is a reaction time games. it uses a raspberry pi, LED button, and the Blynk app. The user must press a button as quick as they can once the led turns on. The system then measures the time it took them to react in ms and gives them a rating saving the results in a JSON file.

<img width="1151" height="378" alt="Screenshot 2026-05-03 202958" src="https://github.com/user-attachments/assets/d25716e8-066d-466f-8e60-3cf5cf3a8a85" />
System Overview Diagram

---

How it works:
1. System connects to Blynk
2. Waits a random time between 2-5 seconds
3. LED turns on
4. Users presses button in the app
5. Reaction time is calculated
6. Results are:
   - Sent to gauge
   - Rated
   - Saved to a JSON file
  
Here is a diagram to show how the game works:

<img width="1120" height="624" alt="Screenshot 2026-05-03 205106" src="https://github.com/user-attachments/assets/5cfe22b5-0bd9-48f2-89b3-c9566e5130d2" />

---

## Features
- Reaction time measurement
- Blynk web and mobile interfaces
- Performance ratings
- Data saved in a JSON file
- Continuos game loop

---

## System Architecture
- Raspberry Pi
- Red LED button
- Blynk App
- JSON file

---

## How it looks in VsCode:
<img width="1919" height="1020" alt="Screenshot 2026-05-03 230250" src="https://github.com/user-attachments/assets/79969f5d-aa14-4269-9c99-957e7f6d64ca" />

---
JSON file:
<img width="1919" height="1025" alt="Screenshot 2026-05-03 230311" src="https://github.com/user-attachments/assets/c6b8d257-18e3-4294-9c58-c72ebbba18bf" />

The data is timestamped as seen in the screenshot. 

## Blynk dashboard
<img width="1919" height="868" alt="image" src="https://github.com/user-attachments/assets/7d7ee531-ade7-41f8-9817-ae2a347764c5" />

---

## Errors encountered
During this project I ran into plenty of errors. The first one was my red LED button not working. I tried fixing this for about 2 weeks before giving up on it and switching to a blynk button instead. I tried all kinds of code i could find online as well as code given to me by AI but nothing worked which is the reason i only have the one sensor working on my pi rather than the 2 required.

I also ran into this error a lot: 
<img width="1919" height="1079" alt="Screenshot 2026-04-30 223429" src="https://github.com/user-attachments/assets/b7e273e2-e470-46b0-a13b-e9dbb9f80180" />

This happened to me when working on the project at home connected to the wifi via lan cable. I spent hours fixing this code by trying to ssh onto the pi using its ip address that i found entering my router connections, but once it was fixed the error would come back the next time i turned it on.

---

## References
1. Tutors labs
2. https://ntsh-vicky.medium.com/basic-of-python-date-time-91349829971b
3. https://www.w3schools.io/file/json-python-read-write/?utm_source=chatgpt.com
4. https://pytutorial.com/writing-json-to-file-in-python/?utm_source=chatgpt.com
5.  AI was used to try fix my physical button error however none of the code worked and therefore wasnt used in the final project



  

