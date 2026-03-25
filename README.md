# 💡 Arduino LED Brightness Control
### 🐍 Python × ⚡ Arduino × 🖥️ VS Code

> Control an LED's brightness **in real-time** using a potentiometer — powered entirely by Python, no C++ required.

---

## ✨ Features

- 🎛️ Real-time LED brightness control via potentiometer
- 🔁 Event-driven callback architecture — no CPU-heavy polling
- 🐍 100% Python — no C++ needed
- 🔌 Simple USB serial communication
- ⚡ PWM (Pulse Width Modulation) for smooth brightness transitions

---

## 🧰 Tech Stack

| 🔧 Tool | 📌 Purpose |
| :--- | :--- |
| 🐍 Python 3.14+ | Main programming language |
| 📦 pyfirmata2 | Serial communication library |
| 🤖 Arduino Uno | Microcontroller hardware |
| 🖥️ VS Code | Code editor |
| 📡 StandardFirmata | Arduino listener firmware |

---

## 🔌 Hardware Wiring

| 🧩 Component | 📍 Arduino Pin | 📝 Notes |
| :--- | :--- | :--- |
| 🎛️ Potentiometer (Middle Pin) | `A0` | Analog input signal |
| 🔴 Potentiometer (Left Pin) | `5V` | Power supply |
| ⚫ Potentiometer (Right Pin) | `GND` | Ground |
| 💡 LED (Long Leg / Anode) | `D9` | Must be a PWM pin `~` |
| ⚫ LED (Short Leg / Cathode) | `GND` via 220Ω Resistor | Current limiter |

---

## 🚀 Setup & Installation

### 📋 Step 1 — Upload Firmware to Arduino

1. Open the **Arduino IDE**
2. Navigate to `File` → `Examples` → `Firmata` → `StandardFirmata`
3. Select your board under `Tools` → `Board`
4. Select your port under `Tools` → `Port` *(e.g. `COM3`)*
5. Click **Upload** and wait for ✅ *"Done Uploading"*
6. ⚠️ **Close the Arduino IDE completely** — if it stays open, Python cannot access the port

---

### 📦 Step 2 — Install the Python Library

Open the terminal inside VS Code and run:

```bash
python -m pip install pyfirmata2
```

---

### ▶️ Step 3 — Run the Project

1. Open the project folder in **VS Code**
2. Run `app.py`
3. 🎛️ Rotate the potentiometer — watch the LED brightness change live!

---

## ⚙️ How It Works

```
🎛️ Potentiometer  →  📡 USB Serial (StandardFirmata)  →  🐍 Python Callback  →  💡 LED Brightness
```

Instead of writing C++ that runs directly on the chip, this project uses a **bridge approach**:

- 📡 The Arduino runs `StandardFirmata` — making it listen for commands over USB
- 🐍 Python runs on your PC and reacts to potentiometer changes
- 🔁 A **callback function** fires **automatically** every time the knob moves
- ⚡ The LED brightness updates instantly via **PWM signal**

---

## 🛠️ Troubleshooting

| ❌ Problem | ✅ Solution |
| :--- | :--- |
| `RuntimeError: Incorrect Arduino ID` | Close the Arduino IDE completely and re-run |
| `COM port not found` | Unplug and re-plug USB, check Device Manager |
| 💡 LED not responding | Make sure LED is on pin `D9` (the `~` pin) |
| 🔌 Wrong COM port | Change `PORT = 'COM3'` in `app.py` to match yours |
| 📦 Library not found | Run `python -m pip install pyfirmata2` again |

