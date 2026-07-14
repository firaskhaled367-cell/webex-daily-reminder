# Webex Daily Islamic Reminder Bot

Posts a short ayah, dhikr, or dua (4-6 lines) to a Webex space every day.

## Files

- `content.json` — the rotating list of reminders. Edit/add to this freely.
- `daily_message.py` — picks today's reminder and posts it to Webex.
- `get_room_id.py` — one-time helper to find your space's `roomId`.
- `.github/workflows/daily.yml` — GitHub Actions schedule that runs the script daily.

## Setup

### 1. Get your bot token
From [My Webex Apps](https://developer.webex.com/my-apps), open your bot and copy its
access token (shown only once — regenerate it there if you lost it).

### 2. Find your room ID
You've already added the bot to the target space. Now run locally:

```bash
pip install -r requirements.txt
export WEBEX_BOT_TOKEN="paste-your-token-here"
python get_room_id.py
```

This prints every space the bot can see along with its `roomId`. Copy the one for
your target space.

### 3. Test sending a message manually

```bash
export WEBEX_ROOM_ID="paste-the-room-id-here"
python daily_message.py
```

Check the Webex space — you should see today's reminder posted by the bot.

### 4. Put this project on GitHub (for the free daily scheduler)

```bash
git init
git add .
git commit -m "Daily Webex reminder bot"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/webex-daily-reminder.git
git push -u origin main
```

### 5. Add your secrets to GitHub
In your GitHub repo: **Settings → Secrets and variables → Actions → New repository secret**

Add two secrets:
- `WEBEX_BOT_TOKEN`
- `WEBEX_ROOM_ID`

### 6. Adjust the schedule
Open `.github/workflows/daily.yml` and edit the `cron` line to your preferred time.
Cron times are in UTC. For example, for 7:00 AM in Amman (UTC+3):

```yaml
- cron: '0 4 * * *'   # 04:00 UTC = 07:00 Amman time
```

Note: Jordan does not currently observe daylight saving, so UTC+3 stays fixed
year-round — double check if that ever changes.

### 7. Done
GitHub Actions will now run the script automatically every day at that time.
You can also trigger it manually anytime from the repo's **Actions** tab using
"Run workflow" (this is enabled by the `workflow_dispatch` line).

## Content

`content.json` now has **508 entries, entirely in Arabic**, built from real
open-source Islamic datasets rather than generated from memory (important for
Quran/hadith accuracy):

- **64 complete short-to-medium surahs** — full Arabic text (Uthmani script),
  sourced from the [amrayn/quran-text](https://github.com/amrayn/quran-text)
  dataset. Only complete surahs are included, never partial verses out of
  context.
- **345 athkar and duas** from the classical collection *Hisn al-Muslim*
  (حصن المسلم), sourced from
  [osamayy/azkar-db](https://github.com/osamayy/azkar-db) — morning/evening
  athkar, prayer, sleep, travel, and daily-situation duas, each with its
  original reference.
- **99 Names of Allah (Asma-ul-Husna)**, sourced from
  [KabDeveloper/99-Names-Of-Allah](https://github.com/KabDeveloper/99-Names-Of-Allah),
  each with the Quranic verse(s) where it appears.

Note: entry length varies — most are short (a few lines), but full surahs run
longer since they're shown complete rather than cut off mid-verse (an earlier
draft tried picking random single verses for brevity, but isolated verses
often read as confusing fragments out of context, so that approach was
dropped in favor of always showing complete, authentic text).

## Customizing the content

Open `content.json` and add, remove, or edit entries — each entry is one
message string. The script picks one deterministically based on the date,
cycling through the whole list before repeating (at 508 entries, that's a
full 500+ days before anything repeats).

## Alternative: running without GitHub

If you'd rather run this on your own PC or server instead of GitHub Actions,
just set the two environment variables and add this to your crontab
(`crontab -e`):

```
0 7 * * * cd /path/to/webex-daily-reminder && /usr/bin/python3 daily_message.py
```
"# webex-daily-reminder" 
"# webex-daily-reminder" 
