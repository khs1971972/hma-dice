<!---

This file is used to generate your project datasheet. Please fill in the information below and delete any unused
sections.

You can also include images in this folder and reference them in the markdown. Each image must be less than
512 kb in size, and the combined size of all images must be less than 1 MB.
-->

## How it works

A dice on the 7-segment display.

Inside, a small counter steps through 1, 2, 3, 4, 5, 6, 1, 2 … on every clock tick. While the roll input (`ui[0]`) is high, the displayed face follows the counter. When the roll input goes low, the face freezes.

The clock runs millions of times per second, so the counter goes round hundreds of thousands of times while the input is held. Nobody can time a release that precisely, so the face it stops on is effectively random.

The design uses 6 flip-flops (3 for the counter, 3 for the face) and a decoder that turns the face into the segment pattern.

## How to test

1. Select the project and reset it. The display shows **1**.
2. Set `ui[0]` high (switch 0 on, or hold a button wired to it). The dice is rolling.
3. Set `ui[0]` low. The display shows a face from 1 to 6.
4. Repeat. Every face from 1 to 6 should come up over a few rolls.

Any clock frequency works; 10 MHz is a good choice.

## External hardware

None. It uses the 7-segment display on the Tiny Tapeout demo board (`uo[0]`–`uo[6]` = segments a–g).
