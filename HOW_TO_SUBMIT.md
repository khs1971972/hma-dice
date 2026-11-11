# How to turn this folder into a real chip

This folder is a complete Tiny Tapeout project for the **HMA Dice**, made from the official template (`ttsky-verilog-template`, shuttle TTSKY26d). Everything is filled in and checked:

- `src/project.v` – the chip (passes Yosys's checks: 25 cells, 6 flip-flops; and 310 simulation checks)
- `info.yaml` – the chip's name, pins and settings
- `test/test.py` – the test GitHub runs on the chip (cocotb + Icarus Verilog)
- `docs/info.md` – the datasheet page Tiny Tapeout prints for your chip

The steps below need your own accounts, so only you can do them. Claude can do step 3 for you once you have steps 1–2.

## 1. Make a free GitHub account

Go to github.com and sign up. Your username matters in step 2.

## 2. Make an empty repository

On GitHub: **+** (top right) → **New repository**. Name it `hma-dice`, choose **Public**, and leave every "add a file" box unticked. Press **Create repository**.

Tiny Tapeout asks that the chip's name is unique on the whole shuttle, so it should include your GitHub username: `tt_um_<username>_dice`. Done: the chip is named `tt_um_khs1971972_dice`.

## 3. Upload this folder

Tell Claude the repository's address (like `https://github.com/<username>/hma-dice`). Claude will upload the folder with git; Windows will open a browser window once so you can sign in to GitHub and allow it.

## 4. Switch on the chip builder

On your repository page: **Settings** → **Pages** → under *Source*, choose **GitHub Actions**. Then open the **Actions** tab. If it asks, press the button to enable workflows.

GitHub then builds your chip automatically, typically in a few minutes for a design this small:

| Check | What it does |
|---|---|
| **gds** | turns your Verilog into the real chip layout (the file the factory needs) and runs the factory checks |
| **test** | runs `test/test.py` on your design |
| **docs** | checks your datasheet page |
| **gl_test** | runs the same test again on the finished gates |

When they're green, the gds check's summary links to a **3D view of your chip**.

## 5. Submit to Tiny Tapeout

Go to app.tinytapeout.com, sign in with GitHub, and create a project from your repository. Pick a shuttle (dates are on tinytapeout.com/chips), check the price in the calculator, and pay for your tile. You can keep updating the design until the shuttle closes.

## 6. Wait, then bring it up

Manufacturing takes about 6–9 months (up to a year in total). Your chip arrives on a demo board. Select the HMA Dice, flip switch 0 on and off, and watch your own silicon roll a dice.
