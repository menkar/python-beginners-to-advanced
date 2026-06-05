# 🐍 Python — Beginners to Advanced

> A structured, hands-on Python learning repository covering everything from fundamental syntax to Object-Oriented Programming, with a real-world **Bank Management System** as the capstone project.

---

## 📋 Table of Contents

- [About This Repository](#-about-this-repository)
- [Learning Path Overview](#-learning-path-overview)
- [Module 1 — Python Basics](#-module-1--python-basics)
- [Module 2 — Data Structures](#-module-2--data-structures)
- [Module 3 — Comprehensions](#-module-3--comprehensions)
- [Module 4 — Exception Handling](#-module-4--exception-handling)
- [Module 5 — File Handling](#-module-5--file-handling)
- [Module 6 — Lambda Functions](#-module-6--lambda-functions)
- [Module 7 — Modules & Packages](#-module-7--modules--packages)
- [Module 8 — Object-Oriented Programming (OOP)](#-module-8--object-oriented-programming-oop)
- [Capstone Project — Bank Management System](#-capstone-project--bank-management-system)
- [Tech Stack](#-tech-stack)
- [Prerequisites & Setup](#-prerequisites--setup)
- [Project Structure](#-project-structure)
- [Author](#-author)

---

## 📖 About This Repository

This repository is a **complete Python learning curriculum** designed for learners at every stage — from writing your very first `print()` statement to building a full-featured, database-backed web application using OOP principles.

Each module is self-contained with clean, well-commented scripts. Every concept is introduced progressively, with practical examples that build toward the final capstone project.

**What you will learn:**

| Area | Topics Covered |
|---|---|
| Language Fundamentals | Variables, data types, operators, control flow, loops, functions |
| Data Structures | Lists, tuples, sets, dictionaries — operations, methods, traversal |
| Pythonic Code | Comprehensions, lambda functions, star args |
| Robustness | Exception handling, file I/O |
| Code Organisation | Modules, packages, sub-packages |
| OOP | Classes, inheritance, encapsulation, polymorphism, abstraction, decorators |
| Real-World Project | Full-stack banking app (CLI + Streamlit web UI) |

---

## 🗺️ Learning Path Overview

```
Basics → Data Structures → Comprehensions → Exception Handling
      → File Handling → Lambda Functions → Modules & Packages
      → Object-Oriented Programming → Capstone Project
```

Each step builds on the previous one. By the end of the curriculum, you will have the skills to design, build, and deploy a real Python application.

---

## 📁 Module 1 — Python Basics

**Location:** `basic/`

The foundation of all Python programming. These scripts introduce core syntax and essential constructs.

| File | What It Covers |
|---|---|
| `main.py` | Entry point structure, script organisation |
| `operators.py` | Arithmetic, comparison, logical, assignment, bitwise, identity, membership operators |
| `conditionalStatements.py` | `if`, `elif`, `else` branching; nested conditions; real-world decision logic |
| `for-loop.py` | Iterating over sequences, `range()`, `enumerate()`, `break`, `continue` |
| `while-loop.py` | Condition-based loops, sentinel values, infinite loop prevention |
| `loops.py` | Loop combinations, nested loops, loop with `else` clause |
| `functions.py` | Defining functions, parameters, return values, default arguments, scope |
| `game-guess-random-number.py` | Mini project — number guessing game using `random` module and loops |

### Key Concepts

- **Operators:** Python supports `+`, `-`, `*`, `/`, `//`, `%`, `**` for arithmetic; `==`, `!=`, `<`, `>`, `<=`, `>=` for comparison; `and`, `or`, `not` for logic.
- **Control Flow:** `if/elif/else` enables branching. Python uses indentation (not braces) to define code blocks.
- **Loops:** `for` loops iterate over any iterable. `while` loops run until a condition becomes `False`. Both support `break` (exit) and `continue` (skip).
- **Functions:** Reusable blocks defined with `def`. Support positional args, keyword args, default values, and `*args`/`**kwargs`.

---

## 📁 Module 2 — Data Structures

**Location:** `data-structure/`

Python's built-in data structures are its most powerful feature. This module covers all four core types with dedicated scripts for methods, traversal, and practice problems.

### 📌 Lists

| File | Content |
|---|---|
| `list/list.py` | Creating lists, indexing, slicing, mutable operations |
| `list/list-methods.py` | `append`, `extend`, `insert`, `remove`, `pop`, `sort`, `reverse`, `copy`, `count`, `index`, `clear` |
| `list/list-pract-questions.py` | Solved practice problems — filtering, sorting, transformation |

**When to use:** Ordered, mutable collections. Use lists when you need to add, remove, or change items.

### 📌 Tuples

| File | Content |
|---|---|
| `tuple/tuple.py` | Immutable sequences, tuple packing/unpacking, single-element tuples |
| `tuple/tuple-methods.py` | `count`, `index`; converting to/from lists; named tuples concept |

**When to use:** Ordered, immutable data — coordinates, RGB values, database rows. Faster than lists.

### 📌 Sets

| File | Content |
|---|---|
| `set/set.py` | Unique element collections, set creation, membership testing |
| `set/set-methods.py` | `add`, `remove`, `discard`, `pop`, `clear`, `union`, `intersection`, `difference`, `symmetric_difference` |
| `set/combining-sets.py` | Set operations — union (`|`), intersection (`&`), difference (`-`) |

**When to use:** Unique values, fast membership testing (`in` is O(1)), deduplication.

### 📌 Dictionaries

| File | Content |
|---|---|
| `dictionary/dictionary.py` | Key-value pairs, creation, access, modification, nested dicts |
| `dictionary/dict-pract-questions.py` | Word frequency, merging dicts, inverting, filtering by value |
| `dictionary/traverse.py` | `.keys()`, `.values()`, `.items()`, iterating, `get()`, `setdefault()` |

**When to use:** Fast key-based lookup. The backbone of JSON data, config files, and caching.

---

## 📁 Module 3 — Comprehensions

**Location:** `comprehension/`

| File | Content |
|---|---|
| `comprehension.py` | List, dictionary, and set comprehensions; conditional comprehensions; nested comprehensions |

Comprehensions are a concise, Pythonic way to build collections in a single line.

```python
# List comprehension
squares = [x**2 for x in range(10) if x % 2 == 0]

# Dict comprehension
word_lengths = {word: len(word) for word in ["hello", "world"]}

# Set comprehension
unique_chars = {c.lower() for c in "Hello World"}
```

**Why it matters:** Comprehensions are significantly faster than equivalent `for` loops and are considered idiomatic Python.

---

## 📁 Module 4 — Exception Handling

**Location:** `exception-handling/`

| File | Content |
|---|---|
| `exception.py` | `try`, `except`, `else`, `finally`; catching specific exceptions; custom error messages |
| `syntax.py` | Common syntax errors, how to read Python tracebacks, debugging tips |

### Key Concepts

```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except (TypeError, ValueError):
    print("Type or value error")
else:
    print("No error occurred")
finally:
    print("Always runs — cleanup code goes here")
```

- **`try`** — code that might raise an exception
- **`except`** — handles the exception
- **`else`** — runs only when no exception occurs
- **`finally`** — always runs regardless of errors (used for cleanup: closing files, DB connections)

Built-in exceptions covered: `ValueError`, `TypeError`, `IndexError`, `KeyError`, `ZeroDivisionError`, `FileNotFoundError`, `NameError`.

---

## 📁 Module 5 — File Handling

**Location:** `file-handling/`

| File | Content |
|---|---|
| `basic.py` | Opening files (`r`, `w`, `a`, `r+`), reading (`read`, `readline`, `readlines`), writing, context managers |
| `project.py` | File handling mini-project — reading, processing, and writing data |
| `Test.txt` | Sample file for reading operations |
| `Test-Create.txt` | Created by write operations during exercises |

### Key Concepts

```python
# Always use context managers — file is auto-closed
with open("data.txt", "r", encoding="utf-8") as f:
    content = f.read()        # entire file as string
    lines = f.readlines()     # list of lines

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, File!")
```

File modes: `"r"` (read), `"w"` (write, overwrites), `"a"` (append), `"r+"` (read + write), `"b"` suffix for binary.

---

## 📁 Module 6 — Lambda Functions

**Location:** `lambda-functions/`

| File | Content |
|---|---|
| `lambda-function.py` | Anonymous functions with `lambda`, use with `map()`, `filter()`, `sorted()`, `reduce()` |

### Key Concepts

```python
# Lambda syntax
square = lambda x: x ** 2

# With map — apply function to every element
doubled = list(map(lambda x: x * 2, [1, 2, 3, 4]))

# With filter — keep elements matching condition
evens = list(filter(lambda x: x % 2 == 0, range(10)))

# With sorted — custom sort key
names = ["Alice", "Bob", "Charlie"]
sorted_by_length = sorted(names, key=lambda name: len(name))
```

**When to use:** Short, throwaway functions passed as arguments. Avoid for complex logic — use `def` instead.

---

## 📁 Module 7 — Modules & Packages

**Location:** `modules-packages/`

| File/Folder | Content |
|---|---|
| `modules.py` | Importing built-in modules, `import`, `from ... import`, aliases |
| `maths.py` | Custom module — reusable math utility functions |
| `models/` | Package structure with `__init__.py`, importing from packages |
| `models/model/` | Nested sub-package — multi-level imports |
| `models/main.py` | Consuming a package from another file |
| `models/packages.py` | Demonstrating package-level imports |

### Key Concepts

```python
# Importing modules
import math
from math import sqrt, pi
import math as m

# Custom module
import maths              # your own maths.py
from maths import add, multiply

# Package import
from models.maths import calculate
from models.model.subMaths import advanced_calc
```

A **module** is a single `.py` file. A **package** is a directory containing an `__init__.py` file. Packages can be nested to any depth.

---

## 📁 Module 8 — Object-Oriented Programming (OOP)

**Location:** `OOPS/`

The most comprehensive module. OOP is the foundation of professional Python development and is directly applied in the capstone project.

### Core OOP Files

| File | Concept |
|---|---|
| `basic.py` | What is OOP? Classes vs procedural code |
| `classes.py` | Defining classes, class body, docstrings |
| `objects.py` | Creating instances, accessing attributes and methods |
| `constructors.py` | `__init__` method, `self`, instance initialisation |
| `attr-methods.py` | Instance attributes, class attributes, instance methods, class methods, static methods |

### Inheritance

| File | Concept |
|---|---|
| `inheritance/single-inheritance.py` | One child class inherits from one parent — `class Dog(Animal)` |
| `inheritance/multiple-inheritance.py` | One class inherits from multiple parents — MRO (Method Resolution Order) |
| `inheritance/multilevel-inheritance.py` | Chain inheritance — `Grandchild → Child → Parent` |
| `inheritance/hierarchical-inheritance.py` | Multiple children from one parent |

### Advanced OOP

| File | Concept |
|---|---|
| `encapsulation/encapsulation.py` | Bundling data + behaviour; restricting direct access |
| `encapsulation/private-access.py` | `_protected`, `__private` naming; name mangling; getters/setters |
| `abstraction/abstraction.py` | Abstract base classes (`ABC`); `@abstractmethod`; hiding implementation |
| `polymorphism/polymorphism.py` | Same method name, different behaviour per class; method overriding |
| `polymorphism/duck-typing.py` | Python's dynamic typing — "if it walks like a duck…" |
| `decorators/decorator.py` | Function decorators, `@property`, `@classmethod`, `@staticmethod`, chaining decorators |
| `dunder-methods/dunder-methods.py` | Magic methods: `__str__`, `__repr__`, `__len__`, `__add__`, `__eq__`, `__lt__`, `__contains__` |
| `star-args/star-args.py` | `*args` (variable positional), `**kwargs` (variable keyword arguments) |
| `star-args/star-args-with-decorators.py` | Combining `*args`/`**kwargs` with decorators for flexible wrappers |
| `oops-project.py` | Mini OOP project applying all concepts together |

### OOP Pillars — Summary

| Pillar | Description | Python Implementation |
|---|---|---|
| **Encapsulation** | Wrap data and methods; control access | Private/protected attributes, getters/setters, `@property` |
| **Inheritance** | Child class reuses parent class behaviour | `class Child(Parent):`, `super()` |
| **Polymorphism** | Different classes, same interface | Method overriding, duck typing |
| **Abstraction** | Expose only what's necessary, hide complexity | `ABC`, `@abstractmethod` |

---

## 🏦 Capstone Project — Bank Management System

**Location:** `oops-bank-management-project.py/`

The capstone project applies **every concept from the curriculum** in a real-world banking application. It is available in two versions:

| File | Description |
|---|---|
| `bank-management-project.py` | Original CLI (command-line) version |
| `bank_app.py` | Full-featured Streamlit web application |
| `data.json` | JSON database — persists all account data |

---

### 🖥️ CLI Version — `bank-management-project.py`

The original console-based application demonstrates core OOP principles.

**Features:**
- Create a new bank account with name, age, email, and PIN
- Deposit money into an account
- Withdraw money from an account
- Display full account details
- Update account information
- Delete an account

**OOP Concepts Applied:**
- `class Bank` — encapsulates all banking logic
- Class-level vs instance-level attributes
- Private methods (`__update`, `__accountGenerate`) — encapsulation
- `@classmethod` — class-level operations not tied to an instance
- JSON file I/O — data persistence
- Exception handling — robust error management

---

### 🌐 Web Application — `bank_app.py` (Streamlit)

A production-grade web banking interface built with **Streamlit**, demonstrating how Python OOP code can power a full web application.

#### ✅ All Working Features

| Feature | Description |
|---|---|
| **Dashboard** | Live statistics — total accounts, total balance held, total transactions; quick-action cards |
| **Open Account** | Validated form; creates account; displays **Account Number + PIN** on success |
| **Deposit Funds** | Authenticate → deposit → instant balance update with result card |
| **Withdraw Funds** | Authenticate → withdraw → remaining balance displayed; insufficient balance guard |
| **Account Details** | Authenticate → visual bank card + profile table + full transaction history |
| **Update Profile** | 2-step flow: verify identity → edit name / email / PIN |
| **Close Account** | Confirmation checkbox required → permanent deletion with warning |

#### 🏗️ Technical Architecture

```
bank_app.py
│
├── class Bank                    ← Core banking engine (OOP)
│   ├── _load() / _save()         ← JSON persistence layer
│   ├── _find()                   ← Account lookup by account no + PIN
│   ├── create_account()          ← Validation + account creation
│   ├── deposit() / withdraw()    ← Balance management + transaction log
│   ├── get_account()             ← Authenticated account fetch
│   ├── update_account()          ← Profile update
│   ├── delete_account()          ← Permanent removal
│   └── stats()                   ← Aggregate dashboard metrics
│
├── UI Helpers                    ← Reusable HTML/CSS components
│   ├── sidebar_nav()             ← Navigation sidebar
│   ├── hero()                    ← Page banner
│   ├── bank_card_html()          ← Visual bank card
│   ├── txn_row()                 ← Transaction list item
│   └── bal_result()              ← Balance display card
│
└── Page Functions                ← One function per page
    ├── page_dashboard()
    ├── page_open_account()
    ├── page_deposit()
    ├── page_withdraw()
    ├── page_account_details()
    ├── page_update_profile()
    └── page_delete_account()
```

#### 🎨 Design & UX

- **Color Scheme:** Deep Navy `#0f2460` + Royal Blue `#1d4ed8` + Slate White `#f0f4f8`
- **Typography:** Inter (Google Fonts) — professional, high-legibility sans-serif
- **Responsive Layout:** Two-column layouts (form + info panel) with adaptive stacking
- **Forms styled as Cards:** White background, rounded corners, subtle shadow via CSS
- **Visual Bank Card:** Gradient card showing balance, account number, holder name
- **Transaction History:** Color-coded rows — green (credit ⬆️) / red (debit ⬇️)
- **Step Indicator:** Multi-step visual flow for Update Profile
- **Flash Messages:** Results shown at top of page after `st.rerun()` for clean UX

#### 🔒 Security & Data Integrity

- PIN stored as integer; 4-digit validation enforced (1000–9999)
- Account lookup requires both account number **and** PIN — dual authentication
- Duplicate email detection on account creation
- Balance precision using `round()` to prevent floating-point errors
- Delete account requires explicit checkbox confirmation
- All data written with `ensure_ascii=False` for international character support

#### 📦 Bugs Fixed from Original CLI Version

| Original Bug | Fix Applied |
|---|---|
| `if userData == False` — always evaluates to `False` | Corrected to `if not acct` after refactoring to return `None` |
| PIN validation crash — `int("")` on empty string | PIN is a validated number input; skip logic uses `None` guard |
| Account saved even when age < 18 | Early `return False` before any write operation |
| Data loaded once at class level (stale after restart) | `_load()` called fresh on every operation |
| Deposit capped at ₹10,000 with no explanation | Raised to ₹1,00,000 with clearly labeled limits |
| No email uniqueness check | Duplicate email detection added |
| No transaction history | Every deposit/withdraw logs timestamped transaction record |

#### ▶️ Running the Web App

**Install Streamlit (one time):**
```bash
pip install streamlit
```

**Launch the application:**
```bash
streamlit run "oops-bank-management-project.py/bank_app.py"
```

**Open in browser:**
```
http://localhost:8501
```

---

## 🛠️ Tech Stack

| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.8+ | Core language |
| **Streamlit** | 1.58+ | Web application framework |
| **JSON** | Built-in | Data persistence |
| `random` | Built-in | Account number generation |
| `string` | Built-in | Character sets for account numbers |
| `datetime` | Built-in | Transaction timestamps |
| `pathlib` | Built-in | Cross-platform file paths |
| **Inter (Google Fonts)** | — | UI typography |

---

## ⚙️ Prerequisites & Setup

### Requirements

- **Python 3.8** or newer
- **pip** (comes with Python)

### Step 1 — Clone the repository

```bash
git clone https://github.com/swapnil-menkar/python-beginners-to-advanced.git
cd python-beginners-to-advanced
```

### Step 2 — Create a virtual environment (recommended)

```bash
# Create environment
python -m venv .venv

# Activate — Windows PowerShell
.venv\Scripts\Activate.ps1

# Activate — Windows Command Prompt
.venv\Scripts\activate.bat

# Activate — macOS / Linux
source .venv/bin/activate
```

### Step 3 — Install dependencies (for the web app only)

```bash
pip install streamlit
```

The basic tutorial scripts have **no external dependencies** — just Python.

### Step 4 — Run any tutorial script

```bash
python basic/for-loop.py
python basic/functions.py
python OOPS/inheritance/multiple-inheritance.py
```

### Step 5 — Run the Bank Management Web App

```bash
streamlit run "oops-bank-management-project.py/bank_app.py"
```

---

## 📂 Project Structure

```
python-beginners-to-advanced/
│
├── basic/                              # Module 1 — Python Fundamentals
│   ├── main.py
│   ├── operators.py
│   ├── conditionalStatements.py
│   ├── for-loop.py
│   ├── while-loop.py
│   ├── loops.py
│   ├── functions.py
│   └── game-guess-random-number.py
│
├── data-structure/                     # Module 2 — Data Structures
│   ├── list/
│   │   ├── list.py
│   │   ├── list-methods.py
│   │   └── list-pract-questions.py
│   ├── tuple/
│   │   ├── tuple.py
│   │   └── tuple-methods.py
│   ├── set/
│   │   ├── set.py
│   │   ├── set-methods.py
│   │   └── combining-sets.py
│   └── dictionary/
│       ├── dictionary.py
│       ├── dict-pract-questions.py
│       └── traverse.py
│
├── comprehension/                      # Module 3 — Comprehensions
│   └── comprehension.py
│
├── exception-handling/                 # Module 4 — Exception Handling
│   ├── exception.py
│   └── syntax.py
│
├── file-handling/                      # Module 5 — File Handling
│   ├── basic.py
│   └── project.py
│
├── lambda-functions/                   # Module 6 — Lambda Functions
│   └── lambda-function.py
│
├── modules-packages/                   # Module 7 — Modules & Packages
│   ├── modules.py
│   ├── maths.py
│   └── models/
│       ├── main.py
│       ├── maths.py
│       ├── packages.py
│       └── model/
│           ├── subMain.py
│           └── subMaths.py
│
├── OOPS/                               # Module 8 — Object-Oriented Programming
│   ├── basic.py
│   ├── classes.py
│   ├── objects.py
│   ├── constructors.py
│   ├── attr-methods.py
│   ├── oops-project.py
│   ├── inheritance/
│   │   ├── single-inheritance.py
│   │   ├── multiple-inheritance.py
│   │   ├── multilevel-inheritance.py
│   │   └── hierarchical-inheritance.py
│   ├── encapsulation/
│   │   ├── encapsulation.py
│   │   └── private-access.py
│   ├── abstraction/
│   │   └── abstraction.py
│   ├── polymorphism/
│   │   ├── polymorphism.py
│   │   └── duck-typing.py
│   ├── decorators/
│   │   └── decorator.py
│   ├── dunder-methods/
│   │   └── dunder-methods.py
│   └── star-args/
│       ├── star-args.py
│       └── star-args-with-decorators.py
│
├── oops-bank-management-project.py/   # Capstone Project
│   ├── bank-management-project.py     ← Original CLI version
│   ├── bank_app.py                    ← Streamlit web application
│   └── data.json                      ← JSON data store (auto-generated)
│
└── README.md
```

---

## 🤝 Contributing

Contributions are welcome! If you find a bug, want to improve an example, or want to add a new topic:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-topic`)
3. Commit your changes with a clear message
4. Open a Pull Request

Please follow existing naming conventions and keep scripts focused on a single concept.

---

## 👤 Author

<table>
  <tr>
    <td><strong>Name</strong></td>
    <td>Swapnil Menkar</td>
  </tr>
  <tr>
    <td><strong>Mobile</strong></td>
    <td>+91 8149005578</td>
  </tr>
  <tr>
    <td><strong>LinkedIn</strong></td>
    <td><a href="https://www.linkedin.com/in/swapnil-menkar-7051852b/">linkedin.com/in/swapnil-menkar-7051852b</a></td>
  </tr>
</table>

---

<div align="center">

**Built with ❤️ to make Python learning structured, practical, and enjoyable.**

*From `print("Hello, World!")` to a full-stack banking application — one concept at a time.*

</div>
