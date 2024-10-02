from manim import *
class vaults(Scene):
    def construct(self):
        f1 = Text('ERC4626: VAULTS').scale(0.9)
        for i in f1:
              self.play(
            Write(i), run_time=0.1
        )
      
        self.play(
            f1.animate.shift(UP*3.5), run_time= 0.6
        )
        self.wait(1)
        f2 =Text('Deposits and Share Allocation:').scale(0.55).next_to(f1,DOWN *1.1).shift(LEFT*4.2)
        
        self.play(
                Write(f2), run_time=0.3
            )
        
        
        re1 = Rectangle(height=1.7, width=5.5).next_to(f2, DOWN).shift(RIGHT*3).set_color('#08BAF500')
        self.play(
            Create(re1), run_time=0.3
        )
        
        tx1 =Text('a  = Amount of deposit').move_to(re1).scale(0.4).shift(LEFT*1.2 + UP*0.5)
        tx2 = Text('B = Balance of vault before deposit').scale(0.4).next_to(tx1, DOWN *0.35).shift(RIGHT*0.69)
        tx3 = Text('s = Shares to mint').scale(0.4).next_to(tx2, DOWN *0.35).shift(LEFT*0.91)
        tx4 = Text('T = Total share after mint').scale(0.4).next_to(tx3, DOWN *0.55).shift(RIGHT*0.38)
        atx = VGroup(tx1,tx2,tx3,tx4)
    
        self.play(
                  Write(atx), run_time=0.3 
                )
        bt =Text('BEFORE').scale(0.5).next_to(re1,DOWN*2.3).shift(LEFT*0.2)
        bt2 =Text('DEPOSIT').scale(0.5).next_to(bt,DOWN).shift(RIGHT*0.05)
        vbt = VGroup(bt, bt2)
        self.play(
            FadeIn(vbt), run_time=0.3
        )
       
        c = VGroup(*[Circle(radius=2).scale(.3) for _ in range(2)]).arrange(RIGHT,buff=2.2).next_to(re1, DOWN*1.4).shift(LEFT*0.2).set_color('#08BAF500')
        self.play(
            FadeIn(c), run_time=0.3
        )
        
        ct= Text('B').scale(0.4).move_to(c[0])
        ct1 = Text('T').scale(0.4).move_to(c[1])
        vct = VGroup(ct, ct1).set_color('#08BAF500')
        for i in vct:
            for char in i:
                self.play(
                    Write(char), run_time=0.3
                )
        
        a = VGroup(*[Arrow(UP,DOWN, max_tip_length_to_length_ratio=0.1, stroke_width=1.5).scale(.5) for _ in range(2)]).arrange(RIGHT,buff=3.4).next_to(c, DOWN).shift(LEFT*0.02)
        self.play(
            Create(a), run_time=0.3
        )
        
        abt =Text('AFTER').scale(0.5).next_to(vbt,DOWN*7.3).shift(LEFT*0.2)
        abt2 =Text('DEPOSIT').scale(0.5).next_to(abt,DOWN).shift(RIGHT*0.2)
        avbt = VGroup(abt, abt2)
        self.play(
            FadeIn(avbt), run_time=0.3
        )
        
        c1= VGroup(*[Circle(radius=2).scale(.3) for _ in range(2)]).arrange(RIGHT,buff=2.3).next_to(a, DOWN)
      
        l1 = Line(buff=0.3).scale(0.4).move_to(c1[0]).rotate(75*DEGREES).shift(UP*0.3+LEFT*0.15).shift(RIGHT*0.15)
       
        l2 = Line(buff=0.3).scale(0.44).move_to(c1[0]).rotate(3*DEGREES).shift(RIGHT*0.26).shift(UP*0.05)
      
        l3 = Line(buff=0.3).scale(0.4).move_to(c1[1]).rotate(75*DEGREES).shift(UP*0.3+LEFT*0.15).shift(RIGHT*0.15)
       
        l4 = Line(buff=0.3).scale(0.44).move_to(c1[1]).rotate(3*DEGREES).shift(RIGHT*0.26).shift(UP*0.05)
        
        acl = VGroup(c1,l1,l2,l3,l4).set_color('#08BAF500')
        
        self.play(
            FadeIn(acl), run_time=0.3
        )
        
        cd= Text('B').scale(0.4).move_to(c1[0]).shift(DOWN*0.28)
        cd1 = Text('a').scale(0.5).move_to(c1[0]).shift(UP*0.3).shift(RIGHT*0.25).rotate(45*DEGREES)
        cd2= Text('T').scale(0.4).move_to(c1[1]).shift(DOWN*0.28)
        cd3 = Text('s').scale(0.5).move_to(c1[1]).shift(UP*0.3).shift(RIGHT*0.25).rotate(45*DEGREES)
        vcd = VGroup(cd,cd1,cd2,cd3).set_color('#08BAF500')
        
        for e in vcd:
            for d in e:
                self.play(
                    Write(d), run_time=0.3
                )
                
        self.wait(1.2)
        
        evyi = VGroup(f2, re1, atx, vbt, c ,vct, a, avbt, acl, vcd)
        self.play(
            FadeOut(evyi)
        )
        
        w =Text('Withdrawing Funds:').scale(0.55).next_to(f1,DOWN *1.1).shift(LEFT*5.2)
       
        self.play(
                Write(w), run_time=0.3
            )
        
        rc1 = Rectangle(height=2.2, width=4.7).next_to(w, DOWN).shift(RIGHT*3).set_color('#08BAF500')
        self.play(
            Create(rc1), run_time=0.3
        )
        rxx =Text('Total deposit = ').move_to(rc1).scale(0.5).shift(LEFT*0.9).shift(UP*0.4)
        rxx1 = MathTex(r'\frac{a + B}{B}').scale(0.55).next_to(rxx).shift(RIGHT*0.05)
        rxx1[0][0].scale(1.2)
        
        
        
        rx1 =Text('Total shares = ').next_to(rxx, DOWN*1.7).scale(0.5)
        rx2 = MathTex(r'\frac{s + T}{T}').scale(0.55).next_to(rx1)
        rx2[0][0].scale(1.2)
        
        
        grx = VGroup(rxx, rxx1, rx1, rx2)
        
        self.play(
                    Write(grx), run_time=0.3
                )
                
        pt = Text('According to our statement, share to mint is').next_to(rc1).shift(LEFT*3.5).shift(UP*0.3)
        pt1 = Text(' proportional to increase in balance of vault ').next_to(pt, DOWN)
        
        vpt = VGroup(pt,pt1).scale(0.4).set_color('#0CFF2400')
        self.play(
            Write(vpt), run_time=0.3
        )
        
        pt2 = Text('Therfore, we can say that;').next_to(rc1, DOWN*0.4).scale(0.4).shift(LEFT*3.2)
        self.play(
            Write(pt2), run_time=0.3
        )
        
        px1 = MathTex(r'\frac{a + B}{B} =  \frac{s + T}{T}').scale(0.6).next_to(rc1, DOWN*2.8)
        self.play(
            Write(px1), run_time= 0.3
        )
        px1copy = px1.copy()
        px2 = MathTex(r'T(a + B) = B(s + T)').scale(0.6).next_to(px1, DOWN*0.65)
        self.play(
            ReplacementTransform(px1copy, px2)
        )
        px2copy = px2.copy()
        
        px3 = MathTex(r'Ta + TB = Bs + TB').scale(0.6).next_to(px2, DOWN*0.65)
        lp = Line(buff=0.1).scale(0.28).rotate(35 * DEGREES).move_to(px3).shift(LEFT*0.4).set_color(RED)
        lp1 = Line(buff=0.1).scale(0.28).rotate(35 * DEGREES).move_to(px3).shift(RIGHT*1.05).set_color(RED)
        vlp = VGroup(px3, lp, lp1)
        self.play(
            ReplacementTransform(px2copy, vlp)
        )
        vlpcopy = vlp.copy()
        px4 = MathTex(r'Ta = Bs ').scale(0.6).next_to(vlp, DOWN*0.65)
        self.play(
            ReplacementTransform(vlpcopy, px4)
        )
        px4copy = px4.copy()
        px5 = MathTex(r's = \frac{aT}{B}').scale(0.6).next_to(px4, DOWN*0.65)
        self.play(
            ReplacementTransform(px4copy, px5)
        )
        self.play(Circumscribe(px5, color='#08BAF500'))
        self.play(Circumscribe(px5, color='#08BAF500'))
        self.play(Circumscribe(px5, color='#08BAF500'))
        
        ft = Text('s = Amount to shares to mint').scale(0.4).next_to(px5, DOWN).set_color('#08BAF500')     
        self.play(
            Write(ft), run_time= 0.3
        ) 
      
      
        
        
        
    
    
     
     
     
     
     
        
        self.wait(2)
        
        