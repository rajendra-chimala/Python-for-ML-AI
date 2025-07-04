# 🔸 if — executes a block of code if the condition is true
x = 10
if x > 5:
    print("🔸 'if' Example: x is greater than 5")

# 🔸 if-else — adds alternative execution when condition is false
y = 3
if y % 2 == 0:
    print("🔸 'if-else' Example: y is even")
else:
    print("🔸 'if-else' Example: y is odd")

# 🟡 if-elif-else — handles multiple conditions clearly
marks = 85
if marks >= 90:
    print("🟡 'if-elif-else' Example: Grade A")
elif marks >= 75:
    print("🟡 'if-elif-else' Example: Grade B")
elif marks >= 60:
    print("🟡 'if-elif-else' Example: Grade C")
else:
    print("🟡 'if-elif-else' Example: Grade D or F")

# 🔻 Nested if — allows decision-making within decision-making
age = 20
has_id = True
if age >= 18:
    if has_id:
        print("🔻 'Nested if' Example: Allowed to vote")
    else:
        print("🔻 'Nested if' Example: ID required to vote")
else:
    print("🔻 'Nested if' Example: Not eligible to vote")

# 💠 match-case (Python 3.10+) — modern switch-case
command = "start"
match command:
    case "start":
        print("💠 'match-case' Example: Starting process")
    case "stop":
        print("💠 'match-case' Example: Stopping process")
    case "pause":
        print("💠 'match-case' Example: Pausing process")
    case _:
        print("💠 'match-case' Example: Unknown command")
