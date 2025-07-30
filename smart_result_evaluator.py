# 🌟 Smart Student Result Evaluator
# Designed by NoorXai 💻 | Intelligent, Elegant, Expressive 🧠

print("═════════════════════════════════")
print("🎓 WELCOME TO NOOR'S RESULT MACHINE")
print("═════════════════════════════════\n")

name = input("🪪 Enter Student Name: ")
roll = input("🔢 Enter Roll Number: ")

print("\n📥 Enter marks out of 100:")

english = int(input("📘 English: "))
math = int(input("📐 Math: "))
physics = int(input("🧲 Physics: "))
computer = int(input("💻 Computer: "))

# 🧠 Intelligent Calculations
total_marks = english + math + physics + computer
average = total_marks / 4

# 🎯 Grade Decision (Einstein Style)
if average >= 90:
    grade = "A+ (Outstanding)"
elif average >= 80:
    grade = "A (Excellent)"
elif average >= 70:
    grade = "B (Good)"
elif average >= 60:
    grade = "C (Satisfactory)"
else:
    grade = "F (Fail – Needs Improvement)"

# 📊 Report Output
print("\n═════════════════════════════════")
print(f"📄 RESULT CARD for {name} | Roll#: {roll}")
print("═════════════════════════════════")
print(f"📘 English: {english}")
print(f"📐 Math: {math}")
print(f"🧲 Physics: {physics}")
print(f"💻 Computer: {computer}")
print("─────────────────────────────────")
print(f"🔢 Total Marks: {total_marks} / 400")
print(f"📈 Average: {average:.2f}")
print(f"🎖️ Grade: {grade}")
print("═════════════════════════════════\n")

print("👨‍🏫 Created with 💙 by NoorXai")
