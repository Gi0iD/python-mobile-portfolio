# 📱 Mobile-First Python Portfolio

Welcome to my personal archive of Python applications. These projects were engineered entirely on an Android mobile device using **Pydroid 3** and **Termux**. 

Rather than modifying or hiding my past scripts, I have uploaded them in their raw, authentic forms to showcase my foundational logic, resourcefulness, and growth as an IT professional.

---

## 💡 My Coding Journey & Philosophy

When I was first introduced to Python and stumbled upon `import random`, I immediately knew that my childhood dream of creating my own games was right in front of me. I didn't have a laptop or a PC at the time, and my knowledge was strictly limited to the absolute basics of the language. 

But I didn't let that stop me. I refused to let physical or educational limitations get in the way of building what was in my head. You can see this raw problem-solving directly in my early code: instead of using advanced Object-Oriented Programming (OOP) which I wasn't comfortable with yet, I engineered custom workarounds using nested lists (`list` inside a `list`). I even utilized that scratch-built list structure to handle my file save-and-load data persistence, ensuring that whenever I closed Pydroid on my Android phone, I could open it right back up and continue exactly where I left off.

---

## 🎮 1. Games (Category 1)

### 🦖 Caveman Survival (ver: 180)
A deep, text-based survival simulator featuring dynamic state management (health, energy, hunger, weather cycles, and seasons) and an intentional "Hard Mode" permadeath state deletion system.

* **Custom Persistence Engine:** To achieve data persistence on a mobile device without relying on external databases, I engineered a self-writing data module (`cmsave.py`). The main loop writes state updates directly as native Python classes, allowing instant type recognition upon re-importing.
* **Error & Boundary Validation:** Implements manual verification routines (`wi()`, `nem()`, `ws()`) to catch unexpected user inputs and prevent unhandled application exceptions during gameplay execution cycles.
