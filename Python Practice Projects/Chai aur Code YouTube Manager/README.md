# 🎥 YouTube Video Manager (with SQLite3)

Hi there! 👋 This is my **first Python project** that uses a real database — a small SQLite3-powered YouTube Video Manager.

This was a small learning project, but I ran into **4 bugs** along the way that taught me more than pure theory ever could. Honestly, before starting this, I was in a dilemma — I thought SQLite3 would be hard to wrap my head around. Turns out, it proved me completely wrong. 😄

## 🛠️ What the project does

- **`main()`** — the body of the whole program, ties everything together in a loop
- **`list_videos()`** — lists all videos using `fetchall()` along with a `for` loop to go through each row
- **`add_video()`** — lets you add a new video, which gets stored in the SQLite database
- **`update_video()`** — lets you update an existing video's details
- **`delete_video()`** — deletes a video by its ID (note: once deleted, that ID is never reused)
- **Exit** — closes the app

## 🐞 Bugs I ran into (and what they taught me)

**1. String vs Integer mismatch**
I was taking user input as a string, but matching it against integers:
```python
case 1:   # ❌ wrong
case '1': # ✅ right
```
Since `input()` always returns a string, my `match/case` needed to compare against strings/characters too — not integers.

**2. Missing comma in SQL syntax**
I forgot a comma between `name` and `time` in my `UPDATE` query. This gave me a confusing 2-line error, which I only understood properly after getting help from Claude to break it down.

**3. `break` inside every case, stuck in `while True`**
I had a `break` in every `match/case` branch, so even though my loop was `while True:`, it kept exiting after just one action instead of looping back for more input. Removing the unnecessary `break` statements fixed it.

**4. SQLite function syntax error**
Ran into a syntax issue with one of my SQLite functions — fixed it after re-watching the relevant part of a Chai aur Code video.

## 💡 Takeaway
Every bug here came from a small, specific misunderstanding — not knowing more theory would've fixed any of these. Only writing the code, breaking it, and fixing it actually did. 🚀