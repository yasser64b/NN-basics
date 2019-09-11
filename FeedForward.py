from manimlib.imports import *

class FeedForward(Scene):
    CONFIG = {"include_sound": True}
    def construct(self):
        self.add_sound("Quaternions.mp3",time_offset=0, gain=None) 
        # Creat the logo:
        #pg1
        Tcircle= Circle(fill_opacity=5).scale(2)
        Tcircle.set_fill()
        Tcircle.set_color(BLUE)
        pg1=TextMobject('Py', 'B','-TV')
        pg1[0].set_color(YELLOW)
        pg1.next_to(Tcircle,0,buff=0).scale(2)

        self.play(DrawBorderThenFill(Tcircle, run_time=6), Write(pg1, run_time=6))
        self.wait()

        pg1.scale(0.2)
        # pg1.to_corner(DOWN+RIGHT)
        Tcircle2=Tcircle.scale(0.2)
        Tcircle2.to_corner(DOWN+RIGHT)
        pg2=pg1.next_to(Tcircle,0,buff=0)

        self.play(Write(Tcircle2),Write(pg2))
        self.wait()

        # self.play(Transform(Tcircle, Tcircle2),Transform(pg1, pg2))
      

        #Title
        title=TextMobject('FeedForward: ','Single Neuron')
        title[1].set_color(YELLOW)
        title.to_edge(UP+LEFT)



        # Drow nodes
        circle1= Circle().scale(0.4)
        circle2= Circle().scale(0.4)
        circle3= Circle().scale(0.4)
        circle1.shift(5*LEFT)
        # circle2.shift()
        circle3.shift(5*RIGHT)

        # Draw arrows
        arrow1 = Arrow(circle1.get_right(),circle2.get_left(),buff=0.1)
        arrow2 = Arrow(circle2.get_right(),circle3.get_left(),buff=0.1)
        # arrow1.set_color(WHITE)

        # Weights and Biases
        w2=TextMobject("\\small $w_{11}^2$") 
        w2.next_to(arrow1,0.1*UP,buff=0.5)
         
        w3=TextMobject("\\small $w_{11}^3$")
        w3.next_to(arrow2,0.1*UP,buff=0.5)

        b2=TextMobject("\\small $b_{1}^2$") 
        b2.next_to(circle2,0.2*UP,buff=0.5)

        b3=TextMobject("\\small $b_{2}^3$") 
        b3.next_to(circle3,UP*0.2,buff = .5)

        # Inputs and out puts 
        x1=TextMobject("\\small $x_1$")
        x1.next_to(circle1,0,buff =0)
        x1.set_color(RED)

        a1=TextMobject("\\small $a_{1}^2$")
        a1.next_to(circle2,0,buff =0)
        a1.set_color(RED)



        o1=TextMobject("\\small $a_{1}^3$")
        o1.next_to(circle3,0,buff =0)
        o1.set_color(RED)

        z=TexMobject("\\small z_{1}^2 =","w_{11}^2", "x_1", "+ b_{1}^2")
        z.next_to(arrow1, DOWN, buff=0.2)
        z[2].set_color(RED)
               

        z2=TexMobject("\\small z_{1}^3 =", "w_{11}^3","a_{1}^2", "+ b_{2}^3 ")
        z2.next_to(arrow2, DOWN, buff=0.2)
        z2[2].set_color(RED)

        a=TexMobject("\\small a_{1}^2","=", "\\sigma","\\left ( w_{11}^2 x_1 + b_{1}^2 \\right )")
        a.next_to(z, 2*DOWN, buff=0.2)
        a[0].set_color(RED)
        a[2].set_color(YELLOW)
        # a[3].set_color(RED)
        
        #Texts
        text1=TextMobject('$\\sigma$', ' = activation function', ' (Sigmoid)')
        text1[0].set_color(YELLOW)
        text1[2].set_color(BLUE)
        text1.next_to(a, DOWN).scale(0.75)

        a2=TexMobject("a_{1}^3","=","\\sigma", "\\left ( w_{11}^3 a_{1}^2 + b_{2}^3 \\right ) ")
        a2.next_to(z2, 2*DOWN, buff=0.2)
        # a2.set_color(BLUE)
        a2[0].set_color(RED)
        a2[2].set_color(YELLOW)
        # furmola[:2].set_color(WHITE)



        #Play
        
        self.play(Write(title))

        self.play(Write(circle1))
        self.play(Write(x1))
        self.play(ShowCreation(arrow1))
        self.play(Write(circle2))
        
        self.play(Write(w2))
        self.play(Write(b2))
        self.wait(6)
        self.play(Write(z))
        self.wait(4)

        self.play(Write(a))
        self.play(Write(a1))
        self.wait(4)
        self.play(Write(text1))
        self.wait(4)

        self.play(ShowCreation(arrow2))
        self.play(Write(circle3))
        self.play(Write(w3))
        self.play(Write(b3))
        self.wait(6)
        self.play(Write(z2))
        self.wait(2)
        self.play(Write(a2))
        self.wait(4)
        self.play(Write(o1))

        self.wait()

        self.play(FadeOut (title),FadeOut (circle1), FadeOut(x1), FadeOut(arrow1), FadeOut(circle2), FadeOut(w2),FadeOut(b2),FadeOut(z),FadeOut(a),
        FadeOut(a1),FadeOut(text1),FadeOut(arrow2),FadeOut(circle3),FadeOut(w3), FadeOut(b3),FadeOut(z2),FadeOut(a2), FadeOut(o1))

        self.wait(1)

       
        #Title
        title=TextMobject('FeedForward: ','Multiple input nodes')
        title[1].set_color(YELLOW)
        title.to_edge(UP+LEFT)
        self.play(Write(title))
        self.wait()
         # Drow nodes
        circle1= Circle().scale(0.25)
        circle2= Circle().scale(0.25)
        circle3= Circle().scale(0.25)
        # circle2.shift()
        circle2.shift(2*LEFT)
        circle3.shift(2*LEFT+2*DOWN)
        l=1
        x=[]
        w=[]
        for i in range (-4,5):
            circle1= Circle().scale(0.25)
            circle1.to_edge(LEFT)
            circle1.shift(0.7*i*DOWN)
        # Draw arrows
            arrow1 =Line(circle1.get_right(),circle2.get_left(),buff=0.1, width=0.2)
        # Inputs and out puts 
            x.append('x'+'_'+str(l))
            w.append('w_{1'+str(l)+'}^2')

            x1=TexMobject('x'+'_'+str(l)).scale(0.7)
            x1.next_to(circle1,0,buff =0)
            x1.set_color(RED)
            w2=TexMobject('w_{1'+str(l)+'}^2').scale(0.6)
            w2.next_to(arrow1,0,buff=0)
            w2.shift(0.1*LEFT)
            w2.set_color(YELLOW)
            l=l+1
            self.play(Write(circle1),Write(arrow1),Write(x1), Write(w2))

        self.play(Write(circle2))
        #b2
        b2=TextMobject("\\small $b_{1}^2$") 
        b2.next_to(circle2,0.2*UP,buff=0.5)
        self.play(Write(b2))
        self.wait(5)

        f=''
        for i in range(len(w)):
            f=f+ w[i]+x[i] +'+ '
        z=TexMobject('z_{1}^2 =', f[:-2],'+','b_{1}^2').scale(0.6)
        z[0].set_color(YELLOW)
        z[3].set_color(RED)
        z.to_edge(UP+RIGHT)
        self.play(FadeOut(title))
        self.play(Write(z))
        self.wait(5)
        #Barce
        brace_bottom = Brace(z[1], DOWN, buff = SMALL_BUFF)
        brace_bottom.set_color(BLUE)
        self.play(GrowFromCenter(brace_bottom))

        sum1=TexMobject('\\sum_{i}^{}', 'w_i x_i', '+', 'b_{1}^2')
        sum1[:-1].set_color(BLUE)
        sum1[3].set_color(RED)
        sum1.next_to(brace_bottom,0.1*DOWN, buff=0.5)
        self.play(Write(sum1))
        self.wait(4)


        #matrix
        matW=TexMobject('=\\begin{bmatrix} w_{11}^2\\ w_{12}^2 \\ w_{13}^2 \\ w_{14}^2 \\ w_{15}^2 \\ w_{16}^2 \\ w_{17}^2 \\ w_{18}^2 \\ w_{19}^2 \\end{bmatrix}').scale(0.5)
        matx=TexMobject('''\\begin{bmatrix} x_1
                        \\\\x_2
                        \\\\x_3 
                        \\\\x_4
                        \\\\x_5 
                        \\\\x_6 
                        \\\\x_7 
                        \\\\x_8 
                        \\\\x_9 
                        \\end{bmatrix}''').scale(0.5)

        self.play(FadeOut(brace_bottom))
        sum1.scale(0.5)
        self.play(                
                sum1.shift, 2*DOWN+LEFT,
                run_time=2,
                path_arc=0 #Change 0 by -np.pi
                )

        matW.next_to(sum1,0.1*RIGHT, buff=1)
        # matW.set_color(YELLOW)
        # matx.set_color(RED)
        matx.next_to(matW,0.3*RIGHT, buff=0.1)
        p=TexMobject('+').scale(0.5)
        p.next_to(matx,0.1*RIGHT,buff=0.5)
        b2.next_to(p,0.1*RIGHT,buff=0.5)
        b2.scale(0.5)
        b2.set_color(RED)

        self.play(Write(matW), Write(matx),Write(p), Write(b2))
        self.wait(4)

        brace_bottom2 = Brace(matW, DOWN, buff = SMALL_BUFF)
        brace_bottom3 = Brace(matx, DOWN, buff = SMALL_BUFF)
        brace_bottom2.set_color(BLUE)
        brace_bottom3.set_color(BLUE)
        self.play(GrowFromCenter(brace_bottom2),GrowFromCenter(brace_bottom3))
        wmat=TexMobject('w')
        wmat.next_to(brace_bottom2,0.1*DOWN, buff=0.5)
        xmat=TexMobject('x')
        xmat.next_to(brace_bottom3,0.1*DOWN, buff=0.5)
        self.play(Write(wmat), Write(xmat))
        self.wait(3)

        self.play(FadeOut(sum1),FadeOut(matW),FadeOut(matx),FadeOut(brace_bottom2),FadeOut(brace_bottom3),FadeOut(xmat),FadeOut(wmat),FadeOut(p),FadeOut(b2))
        wx=TexMobject('=','w.x', '+', 'b_{1}^2')
        wx[-1].set_color(RED)
        sum1.scale(2)
        sum1.shift(2*UP)
        wx.next_to(sum1,RIGHT, buff=0.5)
        wx.shift(2*UP)
        # self.play(Write(sum1),Write(wx))
        # self.wait(3)

        wx1=TexMobject('\\sum_{i}^{}', 'w_i x_i', '+', 'b_{1}^2','=','w.x', '+', 'b_{1}^2')
        wx1.shift(2*UP)
        wx1[:1].set_color(BLUE)
        wx1[3].set_color(RED)
        wx1[-1].set_color(RED)
        self.play(Write(wx1))
        self.wait(4)

        # Apply sigma function 


        a=TexMobject("\\small a_{1}^2","=", "\\sigma","\\left ( w.x + b_{1}^2 \\right )")
        a.next_to(circle2, 1*RIGHT, buff=0.2)
        a[0].set_color(RED)
        a[2].set_color(YELLOW)
        self.play(Write(a))
        self.wait(1)

        a1=TextMobject("\\small $a_{1}^2$").scale(0.7)
        a1.next_to(circle2,0,buff =0)
        a1.set_color(RED)
        self.play(Write(a1))
        self.wait(4)

        self.play(FadeOut(wx1))
        self.wait(2)


        # second node of the hidden layyer
        b22=TextMobject("\\small $b_{2}^2$") 
        b22.next_to(circle3,UP*0.2,buff = .5)
        self.play(Write(circle3), Write(b22))
        l=1
        for i in range (-4,5):
            circle4= Circle().scale(0.25)
            circle4.to_edge(LEFT)
            circle4.shift(0.7*i*DOWN)
            line1=Line( circle4.get_right(),circle3.get_left(), buff=0.1, width=0.1, color=GREEN)
            # line1.set_angle(190*DEGREES)
            w21=TexMobject('w_{2'+str(l)+'}^2').scale(0.6)
            w21.next_to(circle4,0.2*RIGHT,buff=0.5)
            w21.set_color(BLUE)
            l=l+1
            self.play(Write(line1),Write(w21))
        self.wait (4)
        self.play(FadeOut(a))

        # define z22 
        z22=TexMobject('z_{2}^2 ','=','w_{21}^2 x_1','+','w_{22}^2 x_2','+','w_{23}^2 x_3','+','w_{24}^2 x_4','+',
        'w_{25}^2 x_5','+','w_{26}^2 x_6','+','w_{27}^2 x_7','+','w_{28}^2 x_9','+','w_{29}^2 x_9','+', 'b_{2}^2')
        z22.set_color_by_tex('z_{2}^2', YELLOW)
        z22.set_color_by_tex('b_{2}^2', RED)
        z22.scale(0.6)
        z22.next_to(z, DOWN)

        self.play(Write(z22))
        self.wait(4)
        # self.play(FadeOut(a))

        # Define the matrix for both nodes:
        #Barce
        brace_bottom = Brace(z22[2:-2], DOWN, buff = SMALL_BUFF)
        brace_bottom.set_color(BLUE)
        self.play(GrowFromCenter(brace_bottom))

        sum2=TexMobject('\\sum_{i}^{}', 'w.x', '+', 'b^2')
        sum2[:-1].set_color(BLUE)
        sum2[3].set_color(RED)
        sum2.next_to(brace_bottom,0.1*DOWN, buff=0.5)
        self.play(Write(sum2))
        self.wait(4)


        #matrix
        matW2=TexMobject('''=\\begin{bmatrix} w_{11}^2\\ w_{12}^2 \\ w_{13}^2 \\ w_{14}^2 \\ w_{15}^2 \\ w_{16}^2 \\ w_{17}^2 \\ w_{18}^2 \\ w_{19}^2 \\\\
        w_{21}^2\\ w_{22}^2 \\ w_{23}^2 \\ w_{24}^2 \\ w_{25}^2 \\ w_{26}^2 \\ w_{27}^2 \\ w_{28}^2 \\ w_{29}^2 \\end{bmatrix}''').scale(0.5)
        matx2=TexMobject('''\\begin{bmatrix} x_1
                        \\\\x_2 
                        \\\\x_3 
                        \\\\x_4
                        \\\\x_5 
                        \\\\x_6 
                        \\\\x_7 
                        \\\\x_8 
                        \\\\x_9 
                        \\end{bmatrix}''').scale(0.5)
        matb=TexMobject('''\\begin{bmatrix} b_{1}^2 
                    \\\\ b_{2}^2
                    \\end{bmatrix}''').scale(0.7)


        self.play(FadeOut(brace_bottom))
        sum2.scale(0.7)
        self.play(                
                sum2.shift, 2*DOWN+LEFT,
                run_time=2,
                path_arc=0 #Change 0 by -np.pi
                )

        matW2.next_to(sum2,0.1*RIGHT, buff=1)
        matW2.shift(0.1*UP)
        # matW2.set_color(YELLOW)
        # matx2.set_color(RED)
        matx2.next_to(matW2,0.3*RIGHT, buff=0.1)
        p=TexMobject('+').scale(0.5)
        p.next_to(matx2,0.1*RIGHT,buff=0.5)
        matb.next_to(p,0.1*RIGHT,buff=0.5)
        matb.scale(0.5)
        matb.set_color(RED)

        self.play(Write(matW2), Write(matx2),Write(p), Write(matb))
        self.wait(4)

        #braces3 
        brace_bottom = Brace(matW2, DOWN, buff = SMALL_BUFF)
        brace_bottom.set_color(BLUE)
        wmat.next_to(brace_bottom,0.1*DOWN, buff=0.5)
        self.play(GrowFromCenter(brace_bottom), Write(wmat))
        self.wait(4)

        brace_bottom2 = Brace(matx2, DOWN, buff = SMALL_BUFF)
        brace_bottom.set_color(BLUE)
        xmat.next_to(brace_bottom2,0.1*DOWN, buff=0.5)
        self.play(GrowFromCenter(brace_bottom2), Write(xmat))
        self.wait(4)

        brace_bottom3 = Brace(matb, DOWN, buff = SMALL_BUFF)
        brace_bottom3.set_color(BLUE)
        bmat=TexMobject('b^2').scale(0.5)
        bmat.set_color(RED)
        bmat.next_to(brace_bottom3,0.1*DOWN, buff=0.5)
        self.play(GrowFromCenter(brace_bottom3), Write(bmat))
        self.wait(4)


        #Z matrix

        matz2=TexMobject('''\\begin{bmatrix} z_{1}^2 \\\\
        z_{2}^2 \\end{bmatrix} = ''').scale(0.5)
        matz2.set_color(YELLOW)
        matz2.next_to(sum2, LEFT, buff=0)
        matz2.shift(0.1*UP)
        self.play(Write(matz2))
        self.wait(5)


        #fade out matx and braces 
        self.play(FadeOut(matW2),FadeOut(matx2),FadeOut(brace_bottom),FadeOut(brace_bottom2),FadeOut(brace_bottom3),FadeOut(xmat),FadeOut(wmat),FadeOut(p),FadeOut(bmat),FadeOut(matb))

        self.play(                
        matz2.shift, 1.9*UP,
        run_time=2,
        path_arc=0 #Change 0 by -np.pi
        )
        self.play(                
        sum2.shift, 1.9*UP,
        run_time=2,
        path_arc=0 #Change 0 by -np.pi
        )
        self.wait(5)



        # Apply sigma function 2 


        mata=TexMobject("a^2","=", '\\begin{bmatrix} a_{1}^2 \\\\ a_{2}^2 \\end{bmatrix}', '=',"\\sigma","\\left ( w.x + b^2 \\right )")
        mata.next_to(circle2, 1*RIGHT+DOWN, buff=0.2)
        mata[:3].set_color(RED)
        mata[4].set_color(YELLOW)
        self.play(Write(mata))
        self.wait(5)

        a1=TextMobject("\\small $a_{1}^2$").scale(0.7)
        a1.next_to(circle2,0,buff =0)
        a1.set_color(RED)

        a2=TexMobject("a_{2}^2").scale(0.7)
        a2.next_to(circle3,0,buff =0)
        a2.set_color(RED)
        self.play(Write(a1),Write(a2))
        self.wait(4)

        self.play(FadeOut(sum2), FadeOut(z), FadeOut(z22), FadeOut(matz2), FadeOut(b22), FadeOut(mata))
        self.wait(1)

        # mata.scale(0.5)
        # self.play(                
        #     mata.shift,4*UP+4*LEFT,
        #     run_time=2,
        #     path_arc=0 #Change 0 by -np.pi
        #     )

        # self.wait(1)

        #Output layer
        circle5= Circle().scale(0.25)
        circle5.shift(2*RIGHT+0.5*DOWN)
        circle5.set_color(RED)


        arrow2 = Line(circle2.get_right(),circle5.get_left(),buff=0.1, color=BLUE)
        arrow3 = Line(circle3.get_right(),circle5.get_left(),buff=0.1, color=BLUE)

        w311=TextMobject("\\small $w_{11}^3$").scale(0.7)
        w312=TextMobject("\\small $w_{12}^3$").scale(0.7)
        w311.set_color(YELLOW)
        w312.set_color(YELLOW)
        w311.next_to(arrow2,0,buff=0)
        w312.next_to(arrow3,0,buff=0)

        b3=TextMobject("\\small $b_{1}^3$")
        b3.next_to(circle5,UP*0.2,buff = .5)

        self.play(Write(circle5),Write(arrow2), Write(arrow3), Write(w311), Write(w312), Write(b3))
        self.wait(5)


        # Define Z3
        z3=TexMobject("\\small z_{1}^3 =","w_{11}^3", "a_{1}^2", "+","w_{12}^3", "a_{2}^2", '+', 'b_{1}^3' ).scale(0.7)
        z3[0].set_color(YELLOW)
        z3[2].set_color(RED)
        z3[5].set_color(RED)
        z3.shift(3*UP)
        z3[-1].set_color(RED)
        self.play(Write(z3))
        self.wait(5)


        # matw3= TexMobject('\\begin{bmatrix} w_{11}^2 \\ w_{12}^3 \\end{bmatrix}')
        # mata3= TexMobject('\\begin{bmatrix} a_{1}^2 \\\\ a_{2}^2 \\end{bmatrix}')

        mata3=TexMobject("a_{1}^3","=", '\\begin{bmatrix} w_{11}^2 \\ w_{12}^3 \\end{bmatrix}',
        '\\begin{bmatrix} a_{1}^2 \\\\ a_{2}^2 \\end{bmatrix}', '+ b_{1}^3', '=',"\\sigma","\\left ( w.a^2 + b^3 \\right )").scale(0.7)
        mata3.next_to(z3, DOWN, buff=0.2)
        mata3[3].set_color(RED)
        mata3[6].set_color(YELLOW)
        self.play(Write(mata3))
        self.wait(5)


        a13=TexMobject("a_{1}^3").scale(0.5)
        a13.set_color(RED)
        a13.next_to(circle5,0, buff=0)
        self.play(Write(a13)) 
        self.wait(4)

        self.play(FadeOut(z3), FadeOut(b3), FadeOut(mata3))


        mata.scale(0.7)
        mata.next_to(circle2, 0.5*UP+0.2*RIGHT, buff=0.5)
        mata4=TexMobject("a^3","=", '[a_{1}^3]','=',"\\sigma","\\left ( w.a^2 + b^3 \\right )").scale(0.7)
        mata4[:3].set_color(RED)
        mata4[4].set_color(YELLOW)
        mata4.next_to(circle5, 0.2*UP+0.2*RIGHT, buff=0.5)

        self.play(Write(mata))    
        self.play(Write(mata4)) 
        self.wait(10)              
        # self.play(FadeOut(circle1),FadeOut(circle2),FadeOut(circle3),FadeOut(circle4),FadeOut(circle5),FadeOut(arrow1),FadeOut(arrow2),
        #     FadeOut(arrow3),FadeOut(Arrow), FadeOut(mata), FadeOut(mata4), FadeOut(a1), FadeOut(a),FadeOut(a2), FadeOut(a13),FadeOut(x1), 
        #     FadeOut(w312),FadeOut(w311), FadeOut(w),FadeOut(w2), FadeOut(w21), FadeOut(w3))


        clean= Circle(fill_opacity=5).scale(10)
        clean.set_fill(BLACK)
        # Tcircle.set_color(BLACK)
        self.play(GrowFromCenter(clean, run_time=3))
        self.wait()
    



        Tcircle3= Circle(fill_opacity=5).scale(2)
        Tcircle3.set_fill()
        Tcircle3.set_color(BLUE)
        pg3=TextMobject('Py', 'B','-TV')
        pg3[0].set_color(YELLOW)
        pg3.next_to(Tcircle3,0,buff=0).scale(2)


        self.play(DrawBorderThenFill(Tcircle3, run_time=6), Write(pg3, run_time=6))
        self.wait(5)
