# 🌸 Cocos2d Dumper by d1xus

> 🧠 Инструмент для дампа классов и методов Cocos2d (на C++) из ELF-библиотек .so
> 🔍 Поддержка вывода на русском и английском языке

---

## 📦 Что это?

**Cocos2d Dumper** — это простой и мощный скрипт на Python, который позволяет извлекать и анализировать информацию из cocos2d-x игр разработанный на основе readelf

---

## 🛠️ Установка

```bash
git clone https://github.com/d1xus/cocos2d-dumper
cd cocos2d-dumper
```

---

## 🚀 Использование

```bash
python3 dump.py путь_к_файлу.so [язык]
```

| Аргумент          | Описание                                                    |
| ----------------- | ----------------------------------------------------------- |
| `путь_к_файлу.so` | Путь к ELF-библиотеке                                       |
| `[язык]`          | `en` для английского, `ru` для русского (по умолчанию `en`) |

### ✅ Пример:

```bash
python3 dump.py libcocos2dcpp.so ru
```

---

## 🔍 Пример вывода

```cpp
class SoldierController {
    // offset: 0x00f12cd0
    void SoldierController();
    // offset: 0x00f12f68
    void addBodyShape();
    // offset: 0x00f13180
    void addDualWeapon(Weapon*);
    // offset: 0x00f13054
    void getMove();
    // offset: 0x00f13860
    void setAlive(bool);
    // offset: 0x00f12df0
    void ~SoldierController();
};
```

📚 Автоматически определяются имена, параметры, типы и даже деструкторы.

---

## 📌 Особенности

* Поддержка двух языков вывода
* Распознавание vtables и методов
* Удобный для реверс-инженеров и моддеров
* Работает с Cocos2d-x 2.x и 3.x

---

## ✨ Автор

Разработано с любовью 💜
**by [d1xus](https://github.com/d1xus)**
