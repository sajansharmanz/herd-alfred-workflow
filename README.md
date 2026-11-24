# herd

**Start a coding agent on a task from Alfred. It opens in its own Herdr tab, and can work on its own git worktree.**

Type `herd fix the flaky login test` in Alfred and press Enter. A new tab opens in [Herdr](https://herdr.dev), your coding agent starts, and the task is already typed in. You carry on with what you were doing, or jump straight to the new tab if you'd rather.

```
herd fix the flaky login test
herd /code-review 5281 +pr
herd tidy up the README #website +wt @codex
herd why is the queue backing up %here
```

## Why use it

Starting an agent on a side task usually means opening a terminal, finding the repo, maybe making a worktree, starting the agent, then pasting the task in. `herd` does all of that from one line in Alfred.

- **Use any agent.** Claude Code, Codex, opencode, Gemini CLI, pi, Amp, Cursor, Aider, Goose, or anything else that runs in a terminal. Type its command as your default, and switch for one task with `@codex`.
- **Use any repo.** Tell it where your repos live, then pick one with `#name`. Alfred completes the name as you type.
- **Run your skills.** Type `/` to list the skills and slash commands in the repo and in your global folders, with their descriptions. Each agent gets the request in the form it understands.
- **Keep work apart.** Give the task its own worktree and branch, or paste a pull request link to check it out for review.
- **No syntax to learn.** Set a hotkey that opens a form with every option, or type shortcuts like `@codex` once you know them.
- **Choose where it lands.** Tasks open in a Herdr Space named after the repo, or the one you pick with `%space`.
- **Keep track of them.** See which agents need you, message one without finding its tab, and clear away finished worktrees.

## What you need

- macOS with **Alfred 6 and the [Powerpack](https://www.alfredapp.com/powerpack/)**
- **[Herdr](https://herdr.dev)**: the desktop app, its background core, or the terminal UI
- **jq**: included in macOS 15 and later. On older versions, `brew install jq`.
- **git**
- **For `tidy` only:** the command-line tool for the site your repos are on, signed in. See [the `tidy` section](#tidy-clear-finished-worktrees).
- **At least one coding agent** that runs in a terminal

## Words used here

| Word | Meaning |
|---|---|
| **Agent** | A program that writes code for you in a terminal, such as Claude Code or Codex. |
| **Herdr** | An app that runs agents in tabs, so you can watch several at once. |
| **Space** | A group of tabs in Herdr, such as one per project. |
| **Repo** | A project folder kept in git. |
| **Worktree** | A second copy of a repo on its own branch. The agent works there, so its changes don't mix with yours. |
| **Pull request (PR)** | A proposed change, waiting for review on GitHub or a similar site. |
| **Skill** | Saved instructions an agent can follow, started with `/` and its name, such as `/code-review`. |

## Install

1. Download `herd.alfredworkflow` from the [latest release](https://github.com/sajansharmanz/herd-alfred-workflow/releases/latest) and double-click it. To update later, download the newest release and double-click it again. Alfred keeps your settings.
2. Fill in the form Alfred shows, then click **Import**.
3. Optional, and recommended: set a hotkey for the form. In Alfred Preferences → Workflows → herd, double-click the **Hotkey** box and press the keys you want, such as ⌃⌥H. Alfred doesn't import hotkeys, so every user sets their own.

| Field | What it's for |
|---|---|
| **Default agent** | The command that starts your agent, such as `claude`, `codex`, `opencode` or `pi`. Add flags if you like: `claude --model opus`. Leave it blank to use the first agent `herd` finds. |
| **Repo folders** | One per line: a folder that holds your repos, such as `~/repos`, or a single repo. `#name` picks a repo from these. |
| **Default repo** | The repo to use unless you type `#repo`. A name from your repo folders, or a full path. |
| **Herdr Space** | Where tabs open unless you type `%space`. `{repo}` uses the repo's name, `{here}` uses the Space on screen, or give a fixed name. |
| **Show new tabs** | Tick to bring Herdr forward on the new tab when a task starts. Leave it unticked to stay where you are. Type `+s` or `+ns` to change it for one task. |
| **Herdr** | Which Herdr to use. Leave it on Auto to use whichever is running. |

You can change these at any time in Alfred Preferences → Workflows → herd → **Configure Workflow**.

## Using it

Open Alfred and type `herd` followed by a space.

### A task

Type what you want done and press Enter:

```
herd add a loading state to the settings page
```

A notification confirms it started, or says why it couldn't.

### The form

Open it any of these ways:

- **Your hotkey.** Any text you have selected becomes the task, so you can select an error, a ticket or a paragraph of a spec, press the hotkey, and start.
- **⌥↩ in Alfred.** Type a task after `herd`, then press ⌥↩ instead of ↩. The form opens with your task filled in.
- **Universal Actions.** Select text or a link anywhere, open Alfred's Universal Actions, and pick **Start an agent task**.

| Field | What it does |
|---|---|
| **Task** | What the agent should do. It can run over several lines, so you can paste a log or a list of steps. To run a skill, make it the first word. |
| **Agent** | Which agent to use. Your default is first. |
| **Repo** | Which repo to work in. Your default repo is first, then every repo in your repo folders. |
| **Space** | Which Herdr Space the tab opens in. Pick **New Space…** to type a name for a new one. |
| **Tab name** | A name for the agent's tab, so you can message it later with `tell`. |
| **Worktree** | Tick to work on a new worktree and branch. |
| **Pull request** | A PR number or link to check out on its own worktree. With no task, the agent is handed the PR's link. |
| **Show** | Tick to bring Herdr forward on the new tab. It starts ticked or not to match your **Show new tabs** setting. |

Press **Start**. In the Task box, Return starts a new line. You don't need to remember any symbols. The form is built with Alfred 6's [Alfred UI](https://www.alfredapp.com/help/alfredui/).

A pull request link in the task is checked out automatically, with or without the form:

```
herd review https://github.com/acme/app/pull/1234
herd review https://gitlab.example.com/team/app/-/merge_requests/56
herd review https://codeberg.org/acme/app/pulls/78
```

| Site | Link | Checked out |
|---|---|---|
| GitHub | `…/pull/12` | Yes |
| GitLab, including self-hosted | `…/-/merge_requests/12` | Yes |
| Gitea and Forgejo, including Codeberg | `…/pulls/12` | Yes |
| Bitbucket | `…/pull-requests/12` | No. Bitbucket doesn't publish pull requests to git, so check out the PR's branch instead. |

The pull request is fetched from the repo's remote, `origin`. So a plain number such as `+pr 12` works on these sites too.

### A skill

Type `/` to see your skills and slash commands. It works anywhere in the line. Press Tab to pick one and add more words, or Enter to run it as it is:

```
herd /code-review 5281
herd /fix-issue https://github.com/acme/app/issues/12
```

### Shortcuts for the form

Once you know the form, you can skip it by typing its options into the line. Add any of these anywhere. Alfred completes `@`, `#` and `%` as you type.

| Option | Effect | Example |
|---|---|---|
| `@agent` | Use a different agent for this task. Only your agents count: `@code-reviewer` or any other name stays in the task, so Claude subagents still work. | `@codex` |
| `#repo` | Use a different repo. Only your repos count: `#12` stays in the task. | `#website`, `#~/code/app` |
| `%space` | Open in a different Herdr Space. Partial names work. `%here` is the Space on screen. A name that matches none makes a new Space; use `_` for a space, as in `%release_work`. | `%reviews` |
| `=name` | Name the tab, so you can find it and message it later with `tell name`. Letters, digits, dots, dashes and underscores. With `+wt`, the branch is named after it too. | `=login` |
| `+wt` | Work on a new worktree and branch | |
| `+pr` | Check out the pull request named in the task, on its own worktree. A PR link does this without `+pr`. | `+pr 5281` |
| `+s` | Bring Herdr forward on the new tab, for this task only | |
| `+ns` | Don't bring Herdr forward, for this task only | |
| `+clip` | Add what's on the clipboard to the task | `herd /fix-issue +clip` |
| `@@` `##` | Keep an `@` or `#` word in the task even when it matches an agent or repo | `ask @@codex what it thinks` |

### Commands

| Type | Effect |
|---|---|
| `herd default ` | Choose the default agent, if the form's Default agent is blank |
| `herd root add ~/repos` | Add a repo folder, if the form's Repo folders is blank |
| `herd root ` | List repo folders and remove one |
| `herd setup` | Pick up agents installed since you last ran it |

## Keeping track of your agents

Three more keywords come with the workflow.

### `agents`: what needs you

Lists every running agent, with the ones waiting on you first: **Needs you** (red), then **Finished** (green), **Idle** (grey) and **Working** (orange). Each agent shows with its logo and a dot in that colour. An agent without a logo shows the herd sheep instead. Type to filter by Space, tab or repo. Enter brings Herdr forward on that agent's tab. ⌥↩ writes it a message.

### `tell`: message an agent

Type `tell`, pick an agent and press Tab, then type your message. Agents are completed by their tab name, or by their terminal ID (such as `t32`) where two tabs share a name:

```
herd fix the login flow =login +wt
tell login also check the session timeout
```

The agent gets it as if you'd typed it in its tab.

For a longer message, press **⌥↩** on an agent, in `tell` or in `agents`. A form opens with:

- **Agent**: the running agents. Pick another one to switch.
- **Recent**: the last 50 lines on that agent's screen, so you can see what you're replying to. It opens at the newest line and updates every 2 seconds while the agent works. Scroll up to read back, and it stays where you put it.
- **Open in Herdr**: goes to the agent's tab, if you need more than 50 lines.
- **Message**: write several lines or paste a log, then press **Send**.

### `tidy`: clear finished worktrees

Lists the worktrees in `~/.herdr/worktrees` with the state of their pull request. To find that state, it uses the site's own command-line tool. Install the one for your site and sign in once:

| Site | Tool | Install | Sign in |
|---|---|---|---|
| GitHub, including GitHub Enterprise | [`gh`](https://cli.github.com) | `brew install gh` | `gh auth login` |
| GitLab, including self-hosted | [`glab`](https://gitlab.com/gitlab-org/cli) | `brew install glab` | `glab auth login` |
| Gitea, Forgejo and Codeberg | [`gt`](https://about.gitea.com/products/gitea-cli/) | `brew install gitea-cli` | `gt auth login --host <your site>` |
| Bitbucket | None | | |

Bitbucket has no tool that can check a pull request, so `tidy` keeps those worktrees. Remove one yourself with `git worktree remove <folder>`.

Enter on a worktree whose PR is merged or closed:

- closes any Herdr tabs open in it (desktop app and core only; in the Terminal UI, close them yourself),
- removes the worktree,
- deletes its branch, if the PR was **merged**. A closed PR's branch is kept, because it may hold commits that were never pushed.

A worktree with uncommitted changes is never removed. Worktrees with an open PR, or none, are shown but left alone.

## How it works

When you press Enter, `herd` works out the agent, repo, folder and prompt from what you typed and your settings. If you used the form, Start hands its choices to the same steps. Then it:

1. makes a worktree, if you asked for one, and copies `.env` into it,
2. opens a tab in the right Herdr Space and starts the agent there,
3. hands the task to the agent once it's ready for input.

Herdr does the hand-over, so `herd` doesn't need to know how each agent takes a prompt. That's why any interactive agent works.

It works with all three ways of running Herdr:

| Herdr | How the task is started |
|---|---|
| Desktop app | A named tab opens, and Herdr types the task in once the agent is ready. |
| Core only (window closed) | The agent starts in the background and shows as a tab when you open the window. `herd` sends the task when the agent is ready. |
| Terminal UI | A named tab opens. For agents the Terminal UI recognises, Herdr waits for the agent and sends the task. For others, `herd` types it in after a short pause. |

## Skills and agents

`herd` finds skills the way agents store them, so it works with any agent without a list of their folders:

- a skill is a folder with a `SKILL.md`, such as `.opencode/skills/code-review/SKILL.md`,
- a slash command is a Markdown file in a `commands` folder, such as `.claude/commands/deploy.md`.

It looks inside the repo's hidden folders (`.claude`, `.agents`, `.opencode` and any others), then your home's. The repo's skills come first. Your global skills are remembered for an hour, so the list stays quick; `herd setup` rescans them straight away.

Type `/` anywhere in the line to pick a skill. `herd what is the weather /grill-me` runs grill-me with the rest of the line. A `/` word that isn't one of your skills, like `/tmp/log`, stays in the task.

Agents ask for skills in different ways, so `herd` adjusts the request:

| Agent | `herd /code-review 5281` sends |
|---|---|
| Claude Code | `/code-review 5281` |
| Codex | `$code-review 5281` |
| pi | `/skill:code-review 5281` |
| Others | `Use the code-review skill. 5281` |

## More settings

The form covers the everyday settings. For more, edit `~/.config/herd/config.json`, which `herd` creates the first time you use it. In Finder, press ⇧⌘G and go to `~/.config/herd`. A filled-in form field always wins over the same setting in this file.

[`config.example.json`](config.example.json) shows every option. The two most useful are agent variants and shortcuts.

### Agent variants

Add the same agent with different flags, then pick it with `@`:

```json
"agents": {
  "claude-opus": { "cmd": ["claude", "--model", "opus"], "skill": "/{skill} {args}" }
}
```

```
herd plan the billing migration @claude-opus
```

### Shortcuts

A shortcut is a named task with its own prompt, worktree and Space. Any of its fields can differ by agent, so one shortcut can use a skill where an agent has it and plain words where it doesn't:

```json
"shortcuts": {
  "review": {
    "about": "Review a PR on its own worktree",
    "space": "Reviews",
    "worktree": "pr",
    "prompt": {
      "claude": "/code-review {prurl}",
      "default": "Review {prurl}. List bugs by severity with file:line."
    }
  }
}
```

```
herd review 5281
```

### All settings

| Setting | What it does | Default |
|---|---|---|
| `defaultAgent` | Agent used without `@agent` | First agent found |
| `repoRoots` | Folders that hold your repos | None |
| `defaultRepo` | Repo used without `#repo` | None (your home folder) |
| `space` | Space used without `%space` | `{repo}` |
| `show` | Bring Herdr forward on each new tab | `false` |
| `backend` | `auto`, `app`, `core` or `tui` | `auto` |
| `worktreeRoot` | Where worktrees go | `~/.herdr/worktrees` |
| `copyFiles` | Files copied into new worktrees | `[".env"]` |
| `skillDirs` | Extra folders to search for skills, for any kept outside a hidden folder | None |
| `tuiSession` | Herdr Terminal UI session to use | The default session |
| `tuiPromptDelay` | Seconds before typing into an agent the Terminal UI doesn't recognise | `5` |
| `agents` | Your agents, their commands and how they take skills | Agents found |
| `shortcuts` | Your shortcuts | None |

## Troubleshooting

| Problem | Fix |
|---|---|
| Nothing appears after `herd ` | In Alfred Preferences → Workflows → herd, turn on the debugger (the bug icon) and type `herd ` again. The error is usually that jq isn't installed. |
| "Herdr isn't running" | Open Herdr, or start its Terminal UI. |
| "can't find 'x'" | Your Default agent command isn't installed, or isn't on your login shell's PATH. Check the spelling in Configure Workflow, then type `herd setup`. |
| "no agent 'x'" | Install the agent, then type `herd setup`. Or check the `@x` you typed. |
| The hotkey opens the form without the text I selected | Alfred copies the selection with ⌘C, which some apps ignore. Copy it yourself and type it in, or use Universal Actions. |
| The tab opens, then closes | The agent couldn't start. Type `herd setup` so `herd` finds where it's installed. |
| The agent starts but never gets the task | Herdr couldn't tell when it was ready. In the settings file, add `"{prompt}"` to that agent's `cmd` to pass the task as an argument instead. |
| The form doesn't open, or it opens in an odd place | Open the workflow in Alfred Preferences and double-click the **Alfred UI** object. Check its file is `herd.alfredui`, and try the other launch setting: inside Alfred or as its own window. |
| The agent asks whether to trust the folder | Answer it once per folder. The task arrives after that. |
| A skill isn't in the `/` list | A new global skill shows within the hour, or straight away after `herd setup`. A skill outside a hidden folder needs its folder in `skillDirs` in the settings file. |
| A pull request won't check out | The task needs a PR number or link, and the PR must be in the repo's `origin`. Bitbucket pull requests can't be fetched this way. |
| `tidy` says to install a tool and sign in | Install the tool it names, then sign in. The table in the `tidy` section shows how. |
| `tidy` says "no PR" for a worktree that has one | Check you're signed in to the site's tool. For GitHub, run `gh auth status`. |
| A task opened with the window closed isn't in any Space | `herd` hadn't seen that Space yet. Open Herdr once, then run it again. |

`herd` only deletes worktrees when you ask it to with `tidy`, and only once their pull request is merged or closed.

## Working on herd

### What's in the repo

| File | What it does |
|---|---|
| `herd` | The zsh script that does the work |
| `info.plist` | The Alfred workflow: keywords, hotkey, form and settings |
| `herd.alfredui/ui.json` | The options form and the message form |
| `herd.alfredui/scripts/fill` | Fills the form's lists when it opens |
| `herd.alfredui/scripts/space` | Shows the New Space box when you pick **New Space…** |
| `herd.alfredui/scripts/history` | Refreshes the Recent box when you pick another agent |
| `herd.alfredui/scripts/pulse` | Runs every 2 seconds while the form is open, and refreshes Recent when the agent's screen changes |
| `icons/` | The status icons. `make-icons.py` draws them. |
| `build.sh` | Packs everything into `herd.alfredworkflow` |
| `scripts/next-version` | Works out the next version number from the commit messages |
| `.github/workflows/release.yml` | Builds and publishes a release on every push to `master` |

The form's Start button hands its choices back to `herd` as `herd_f_*` variables.

### Testing

`herd` refuses to run outside Alfred. To test it from a terminal, set `HERD_DEV=1`, and add `-n` to print the Herdr commands instead of running them:

```sh
HERD_DEV=1 ./herd -n fix the build +wt @codex
```

Run `./build.sh` to make `herd.alfredworkflow`, then double-click it to install your build. The built file isn't kept in git.

To redraw the status icons, run `uv run --with pillow python make-icons.py`. It needs `rsvg-convert` (`brew install librsvg`). To give another agent a logo, add it to the list at the top of `make-icons.py`.

### Releases

Every push to `master` makes a release on GitHub, with the built workflow attached and notes listing the changes. The version goes up based on the commit messages since the last release:

| Commit message starts with | Example | Version change |
|---|---|---|
| `feat:` | `feat: show agent logos` | 1.2.0 → 1.3.0 |
| `fix:`, or anything else | `fix: tell form scroll` | 1.2.0 → 1.2.1 |
| A `!` after the type, or `BREAKING CHANGE:` in the body | `feat!: drop the TUI backend` | 1.2.0 → 2.0.0 |

The first release uses the version in `info.plist`. After that, the tags (`v1.2.3`) hold the version, and the release job stamps it into the package. You don't need to edit `info.plist` to release.

## Licence

MIT. See [LICENSE](LICENSE).

The icon is <a href="https://www.vecteezy.com/free-vector/sheep-icon">Sheep Icon Vectors by Vecteezy</a>, used under the Vecteezy Free License. It isn't covered by the MIT licence.

The agent logos come from [LobeHub Icons](https://github.com/lobehub/lobe-icons), under the MIT licence. Each logo is a trademark of its owner.
