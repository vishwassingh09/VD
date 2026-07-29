from manim import *

class AnilineResonance(Scene):
    def construct(self):
        # PRO-TIP: Uncomment the line below to show a coordinate grid on your video.
        # This makes it infinitely easier to find the exact coordinates for your arrows!
        # self.add(NumberPlane())

        # ---------------------------------------------------------
        # 1. LOAD THE MOLECULES
        # ---------------------------------------------------------
        # Assuming you have exported your structures as SVGs in the same folder.
        # (If you don't have SVGs yet, you can replace SVGMobject with Text("Molecule 1") to test the setup)
        
        state1 = SVGMobject("aminobenzene.svg").scale(2).move_to(LEFT * 3)
        state2 = SVGMobject("aminobenzene2.svg").scale(2).move_to(RIGHT * 3)

        # ---------------------------------------------------------
        # 2. SCENE START
        # ---------------------------------------------------------
        # Fade in the title and the first resonance structure
        title = Text("Positive Resonance (+R) Effect", color=BLUE).to_edge(UP)
        self.play(Write(title))
        self.play(FadeIn(state1))
        self.wait(1)

        # ---------------------------------------------------------
        # 3. DRAW THE ELECTRON ARROWS
        # ---------------------------------------------------------
        # We use CurvedArrow to show electron movement. 
        # You will tweak the coordinates [x, y, z] to perfectly match your SVG's lone pairs and bonds.
        
        # Arrow 1: Nitrogen lone pair down to the C-N bond
        arrow1 = CurvedArrow(
            start_point=np.array([-3.0, 1.5, 0]), 
            end_point=np.array([-2.5, 0.8, 0]), 
            angle=-PI/2, 
            color=RED
        )
        
        # Arrow 2: Ring pi-bond breaking and moving to the Ortho carbon
        arrow2 = CurvedArrow(
            start_point=np.array([-3.5, 0.2, 0]), 
            end_point=np.array([-4.2, -0.5, 0]), 
            angle=PI/2, 
            color=RED
        )

        # Animate the arrows drawing themselves sequentially
        self.play(Create(arrow1), run_time=1)
        self.play(Create(arrow2), run_time=1)
        self.wait(1)

        # ---------------------------------------------------------
        # 4. MORPH TO THE NEXT STATE
        # ---------------------------------------------------------
        # Transform the first molecule into the second, while fading out the arrows
        
        self.play(
            ReplacementTransform(state1, state2),
            FadeOut(arrow1),
            FadeOut(arrow2),
            run_time=1.5
        )
        
        # Add a label to the new state
        label = Text("Ortho- Carbanion", font_size=24, color=YELLOW).next_to(state2, DOWN)
        self.play(Write(label))
        
        self.wait(2)