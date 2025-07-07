# c0ld ema1l // tldr - a keypad to help you with your job search!

Hi! This is **c0ld ema1l**, my custom 6-button keypad designed to make applying for jobs easier! 
This project was inspired by my experience cold emailing for opportunities, now made easier with this automated keypad :))

---
# Required Photos
<img width="300" alt="Screenshot 2025-07-06 at 5 45 39 PM" src="https://github.com/user-attachments/assets/1092ee78-1c73-4802-819b-0cd804cbeb44" />
<img width="300" alt="Screenshot 2025-07-06 at 5 46 39 PM" src="https://github.com/user-attachments/assets/e0462319-e3be-4fb8-82ca-0ae33fcf34a9" />
<img width="300" alt="Screenshot 2025-07-06 at 5 49 33 PM" src="https://github.com/user-attachments/assets/1e863105-9b6c-41a3-b48c-567d6d3e103e" />
<img width="300" alt="Screenshot 2025-07-06 at 5 48 37 PM" src="https://github.com/user-attachments/assets/799259c3-8aa2-4c40-9686-4f1565230ebf" />

---

## Features

- 6 mechanical keys, each one types out a different piece of a job application:
  - Cold email intro
  - Portfolio link
  - Closing line
  - Resume link
  - Thank you follow-up
  - Last key types Soham Parekh’s full cold email template
- Combo keys -- you press 2 at once to:
  - Open LinkedIn
  - Open GitHub
  - Open Google Sheets

---

## PCB

<img width="400" alt="Screenshot 2025-07-06 at 5 45 39 PM" src="https://github.com/user-attachments/assets/10ff6e82-db68-45a2-9ce5-04eb6816dcbc" />


I designed the PCB in KiCad. There are 6 switches in a simple matrix, added diodes, and a USB-C connector. DRC passed with zero errors.

---

## CAD Model

The 3D printed case holds everything snugly, with space for the USB port and switches.

<img width="400" alt="Screenshot 2025-07-06 at 5 49 33 PM" src="https://github.com/user-attachments/assets/032b0e3d-e0ef-4aa3-9ac8-23feaf83d609" />


It assembles with M3 screws and M3 heat-set inserts.

---

## Firmware

The firmware is a file included in my Firmware folder as main.py. This project uses KMK firmware.
- Types text over USB.
- Custom combos detect when 2 keys are pressed to launch websites automatically.

---

## Bill of Materials (BOM)

| Item | Source | Notes |
|------|--------|-------|
| 1x Microcontroller (Pro Micro / XIAO) | Provided | Soldered directly |
| 6x Mechanical switches | Provided | Any MX-compatible switch |

| M3x5mmx4mm heat-set inserts (4 pcs) | Provided | For case assembly |
| USB-C cable | Provided | To connect it all |


6x MX-Style Switches

6x DSA Blank White Keycaps

6x 1N4148 signal diodes

9x SK6812 MINI-E RGB LEDs

1x Seeed XIAO RP2040

1x Case (2 printed parts)

4x M3 × 16 mm pan-head screws

1x USB-C Cable

---

## How it works

1. Plug it into your computer via USB-C.
2. Press any key: parts of a cold email are typed out for you instantly.
3. Press combos: jump straight to **LinkedIn**, **GitHub**, or **Google Sheets**.
---
