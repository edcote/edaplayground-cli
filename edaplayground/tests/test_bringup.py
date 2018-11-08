import edaplayground

u = "foo@bar.com"
p = "password"

playground = edaplayground.CLI(u, p)
playground.connect()

design = """
module dff (
     input      clk
    ,input      d
    ,output reg q
);

always_ff @(posedge clk)
    q <= d;

endmodule
""".strip()

testbench = """
module tb_top;
    bit clk;
    bit d;
    bit q;
    
    dff dff_0 (clk, d, q);
    
    initial begin
        #10;
        $display("DONE!");
        $finish;
    end

endmodule
""".strip()

playground.run_simulation(design, testbench)

playground.disconnect()
