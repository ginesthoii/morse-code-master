# Morse Master — Raspberry Pi Pico Morse Trainer

A tiny, offline Morse-code practice device using:

• Raspberry Pi Pico  
• A single paddle key  
• Two LEDs for dot/dash feedback  
• Minimal, readable MicroPython code  

---

## Features

• Real-time dot/dash detection  
• LED feedback for timing accuracy  
• Simple thresholds for learning practice  
• Easy to modify or extend  
• Works on battery or USB  

---

## Wiring

KEY → GP14  
GREEN LED → GP16  
RED LED → GP15  
Both LEDs → resistor → GND  
Key → GND

See wiring-diagram.png.

---

## Usage

Press shortly for “dot.”  
Hold longer for “dash.”  
Bad timing → error flash.

---

## Extend This

• Add buzzer audio  
• Add OLED (SSD1306) showing letters  
• Add scoring (“accuracy mode”)  
• Add Bluetooth keyboard out  
• Fully enclosed 3D case included
