/*
 * Copyright (c) 2026 HMA
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

// HMA Dice: hold the roll input and the dice rolls; let go and it shows a face from 1 to 6.
// Inputs:  ui_in[0] = roll (hold to roll)
// Outputs: uo_out[6:0] = 7-segment display (segments g f e d c b a), uo_out[7] = dot (off)
module tt_um_khs1971972_dice (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when the design is powered, so you can ignore it
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

  reg [2:0] spin;   // counts 1..6 on every clock tick
  reg [2:0] face;   // the value on the display

  always @(posedge clk) begin
    if (!rst_n) begin
      spin <= 3'd1;
      face <= 3'd1;
    end else begin
      spin <= (spin == 3'd6) ? 3'd1 : spin + 3'd1;
      if (ui_in[0]) face <= spin;   // rolling while held
    end
  end

  reg [6:0] seg;   // segments g f e d c b a
  always @(*) begin
    case (face)
      3'd1: seg = 7'b0000110;
      3'd2: seg = 7'b1011011;
      3'd3: seg = 7'b1001111;
      3'd4: seg = 7'b1100110;
      3'd5: seg = 7'b1101101;
      default: seg = 7'b1111101;   // 6
    endcase
  end

  // All output pins must be assigned. If not used, assign to 0.
  assign uo_out  = {1'b0, seg};
  assign uio_out = 8'b0;
  assign uio_oe  = 8'b0;

  // List all unused inputs to prevent warnings
  wire _unused = &{ena, uio_in, ui_in[7:1], 1'b0};

endmodule
