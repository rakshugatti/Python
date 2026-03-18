Here’s a **brief and clear explanation** of all concepts with examples 👇

---

# 🔹 **1. Greedy vs Lazy Matching**

### ✅ **Greedy Matching (Default)**

* Matches **maximum possible text**
* Uses: `*`, `+`, `{}`

👉 Example:

```python
re.findall(r"<div>.*</div>", "<div>A</div><div>B</div>")
```

**Output:**
`['<div>A</div><div>B</div>']`
✔ Captures everything (too much)

---

### ✅ **Lazy Matching (Non-Greedy)**

* Matches **minimum possible text**
* Add `?` → `*?`, `+?`

👉 Example:

```python
re.findall(r"<div>.*?</div>", "<div>A</div><div>B</div>")
```

**Output:**
`['<div>A</div>', '<div>B</div>']`
✔ Correct extraction

---

# 🔸 (a) **HTML Extraction (Greedy vs Lazy)**

| Type   | Pattern          | Result                   |
| ------ | ---------------- | ------------------------ |
| Greedy | `<div>.*</div>`  | One large match          |
| Lazy   | `<div>.*?</div>` | Multiple correct matches |

---

# 🔸 (b) **Min vs Max Repetition**

```python
text = "aaaa"
```

* **Greedy (`a+`)** → `['aaaa']` (maximum)
* **Lazy (`a+?`)** → `['a','a','a','a']` (minimum)

---

# 🔸 (c) **Difference Between `.*` and `.*?`**

```python
text = "Start A End B End"
```

* **`.*` (Greedy)**

  ```python
  re.search(r"Start.*End", text).group()
  ```

  👉 `Start A End B End`

* **`.*?` (Lazy)**

  ```python
  re.search(r"Start.*?End", text).group()
  ```

  👉 `Start A End`

---

# 🔹 **2. Lookahead `(?=...)`**

* Matches **only if followed by something**

```python
re.findall(r"\d+(?=USD)", "100USD 200INR 300USD")
```

👉 Output: `['100', '300']`
✔ Numbers followed by "USD"

---

# 🔹 **3. Lookbehind `(?<=...)`**

* Matches **only if preceded by something**

```python
re.findall(r"(?<=₹)\d+", "₹500 $300 ₹1000")
```

👉 Output: `['500', '1000']`
✔ Numbers after ₹

---

# ⭐ **Final Summary**

| Concept      | Meaning                   |
| ------------ | ------------------------- |
| Greedy (`*`) | Maximum match             |
| Lazy (`*?`)  | Minimum match             |
| `.*`         | Match everything          |
| `.*?`        | Match minimum             |
| `(?=...)`    | Lookahead (check after)   |
| `(?<=...)`   | Lookbehind (check before) |

---

# 🎯 **One-Line Answer (Viva)**

👉 “Greedy matching captures maximum text while lazy matching captures minimum; lookahead and lookbehind match patterns based on surrounding context without including them in the result.”
