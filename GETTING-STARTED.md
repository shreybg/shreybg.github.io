# Getting started, from nothing

This assumes you have never used GitHub, a terminal, or Python. Work through
it in order. Steps 1–6 get the blog running on your own computer; steps 7–10
put it on the internet.

Budget about an hour the first time. After that, publishing a post takes two
commands.

---

## Some vocabulary, so the rest makes sense

- **Terminal** — a window where you type commands instead of clicking. On Mac
  it's called Terminal, on Windows it's PowerShell.
- **Pelican** — a program that reads your Markdown files and spits out a
  finished website (a folder of HTML). It runs on your computer, not on a
  server.
- **Git** — tracks changes to your files and copies them to GitHub.
- **GitHub** — a website that stores your files. It will also host your blog
  for free.
- **Repository (repo)** — one project's folder, stored on GitHub.
- **Markdown** — plain text with light formatting. `**bold**`, `# Heading`.
  It's what you write posts in.

You do **not** need to understand Git properly to follow this. Four commands
are enough, and they're all written out below.

---

## Step 1 — Make a GitHub account

1. Go to <https://github.com> and click **Sign up**.
2. Pick a username carefully. **Your blog's address will be
   `https://YOURUSERNAME.github.io`**, so choose something you'll be happy
   reading on a URL for years. Short and lowercase is best.
3. Verify your email address when GitHub asks. You must do this or the next
   steps fail.

From here on, wherever you see `YOURUSERNAME`, substitute what you chose.

---

## Step 2 — Install Python

Pelican is a Python program, so you need Python first.

**Windows**

1. Go to <https://www.python.org/downloads/> and click the yellow download
   button.
2. Run the installer. **On the first screen, tick the box that says "Add
   python.exe to PATH."** This is easy to miss and everything breaks without
   it.
3. Click Install Now.

**Mac**

1. Go to <https://www.python.org/downloads/> and download the macOS installer.
2. Run it and accept the defaults.

(macOS does ship with a Python, but it's an old one that's awkward to install
packages into. Use the one from python.org.)

**Linux**

Python is almost certainly already there. If `python3 --version` prints
something, you're fine.

**Check it worked.** Open your terminal:

- Windows: press the Start key, type `powershell`, press Enter.
- Mac: press Cmd+Space, type `terminal`, press Enter.

Type this and press Enter:

```
python3 --version
```

You should see something like `Python 3.12.4`. If Windows says the command
isn't recognised, try `python --version` instead; if that also fails, the
PATH box in the installer wasn't ticked — reinstall and tick it.

> **Windows note:** everywhere below I write `python3`. On Windows, use
> `python` instead. That's the only difference.

---

## Step 3 — Install Git

**Windows** — download from <https://git-scm.com/download/win> and run the
installer. Accept every default; there are a lot of screens and none of them
need changing.

**Mac** — in your terminal, type:

```
git --version
```

If it isn't installed, macOS will pop up a dialog offering to install the
developer tools. Click Install and wait.

**Linux** — `sudo apt install git` (or your distro's equivalent).

Then tell Git who you are. Run these two, with your own details:

```
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Use the same email you signed up to GitHub with.

---

## Step 4 — Put the blog files somewhere sensible

Download the `tao-pelican` folder from our conversation and unzip it if
needed. Move it somewhere you'll find again — your Documents folder is fine.
Rename it to `blog` if you like.

Now point your terminal at it. Type `cd ` (with a space after it), then drag
the folder from your file manager onto the terminal window and press Enter.
That fills in the path for you, which saves typing it out.

Check you're in the right place:

```
ls
```

(On Windows PowerShell, `ls` works too.) You should see `pelicanconf.py`,
`content`, `themes`, and a few other files. If you don't, you're in the wrong
folder.

---

## Step 5 — Install Pelican

A "virtual environment" is a private box of Python packages for this project,
so it can't collide with anything else on your machine. Create one:

```
python3 -m venv .venv
```

Then switch it on. **This command is different per platform:**

- Mac / Linux: `source .venv/bin/activate`
- Windows PowerShell: `.venv\Scripts\Activate.ps1`

Your prompt should now start with `(.venv)`. That's how you know it's active.

> If Windows refuses with a message about execution policies, run
> `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`, answer `Y`, then try
> activating again.

Now install everything:

```
pip install -r requirements.txt
```

It'll print a lot of lines. That's normal.

**You need to activate the virtual environment every time you open a new
terminal to work on the blog.** It doesn't persist. If a Pelican command ever
says "command not found," this is almost always why.

---

## Step 6 — See your blog

```
pelican --autoreload --listen
```

Open <http://localhost:8000> in your browser. There's your blog, with the
sample post.

Leave that command running while you write — it rebuilds automatically every
time you save a file. Press Ctrl+C in the terminal to stop it.

### Write your first real post

Create a new file in `content/posts/`. Name it something like
`my-first-post.md`. The top of the file needs these lines:

```markdown
Title: My first post
Date: 2026-08-12 10:00
Category: uncategorised
Tags: first
Author: Your Name
Slug: my-first-post

Then leave a blank line, and write here. Math works: $e^{i\pi} + 1 = 0$.
```

Save it, and it'll appear in your browser within a second or two.

`Slug` is the bit that becomes the web address, so keep it lowercase with
hyphens. Delete the sample post (`2026-08-12-a-first-post.md`) whenever you
like — but read it first, it demonstrates the theorem boxes.

### Personalise it

Open `pelicanconf.py` in any text editor and change `AUTHOR`, `SITENAME` and
`SITESUBTITLE` at the top. Replace `content/images/header.jpg` with your own
banner image (keep the same filename, or update `HEADER_IMAGE` to match).

---

## Step 7 — Create the repository on GitHub

1. Go to <https://github.com/new>.
2. Under **Repository name**, type exactly: `YOURUSERNAME.github.io` — your
   own username, then `.github.io`. This exact name is what makes GitHub
   serve it as a website at the root of your domain.
3. Leave it **Public**.
4. Do **not** tick "Add a README file" or add a .gitignore. You want it empty.
5. Click **Create repository**.

Leave that page open. You'll need the URL on it in a moment.

---

## Step 8 — Set your site's address

Open `publishconf.py` and change this line:

```python
SITEURL = "https://example.com"
```

to your real address:

```python
SITEURL = "https://YOURUSERNAME.github.io"
```

Save it. This matters — get it wrong and your stylesheet and links break once
the site is live.

---

## Step 9 — Send your files to GitHub

Back in the terminal, in your blog folder, run these one at a time:

```
git init -b main
git add .
git commit -m "First commit"
git remote add origin https://github.com/YOURUSERNAME/YOURUSERNAME.github.io.git
git push -u origin main
```

GitHub will ask you to sign in. A browser window should open — approve it
there.

> If it asks for a password in the terminal instead, note that your account
> password won't work; GitHub requires a "personal access token." The browser
> sign-in is easier, so try to get that one.

Refresh your GitHub page and you should see your files.

This step backs up your *source* files. It does not publish the site yet —
that's next.

---

## Step 10 — Publish

Two commands. Build the finished site, then push it:

```
pelican content -s publishconf.py
ghp-import -n -p -f output
```

The first turns your Markdown into a folder of HTML called `output`. The
second copies that folder to a branch called `gh-pages`, which is where
GitHub Pages looks.

Now switch it on:

1. On your GitHub repo page, click **Settings**.
2. In the left sidebar, click **Pages**.
3. Under **Source**, choose **Deploy from a branch**.
4. Set the branch to **gh-pages** and the folder to **/ (root)**.
5. Click **Save**.

Wait two or three minutes, then visit `https://YOURUSERNAME.github.io`.

First deploys are sometimes slow, and it's normal to get a 404 for a few
minutes. Give it ten before you start worrying.

---

## Your routine from now on

Every time you write a post:

```
source .venv/bin/activate        # Windows: .venv\Scripts\Activate.ps1
pelican --autoreload --listen    # write and preview, Ctrl+C when done
```

Every time you want the world to see it:

```
pelican content -s publishconf.py
ghp-import -n -p -f output
git add . && git commit -m "New post" && git push
```

That last line backs up the source. Strictly optional for the site to work,
but do it — it's your only backup.

---

## When something goes wrong

**"command not found: pelican"** — the virtual environment isn't active. Run
the activate command from step 5.

**Site is live but has no styling** — `SITEURL` in `publishconf.py` is wrong,
or you built with `pelicanconf.py` instead of `publishconf.py`. Fix and
republish.

**Changes don't show up on the live site** — you rebuilt but forgot
`ghp-import`, or your browser cached the old version. Try a hard refresh
(Ctrl+Shift+R, or Cmd+Shift+R on Mac).

**Math shows as raw `$...$`** — check you're using single dollars for inline
and double for displayed, and that the post has a blank line before a
displayed equation.

**404 after ten minutes** — check Settings → Pages actually says `gh-pages`,
and check the repo name is exactly `YOURUSERNAME.github.io`, including the
dot.
