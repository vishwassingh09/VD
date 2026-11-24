from manim import *
import numpy as np

class AnilineMechanism(Scene):
    def construct(self):
        # ---------------------------------------------------------
        # 1. BUILD THE MOLECULE NATIVELY
        # ---------------------------------------------------------
        # Create the benzene ring (a hexagon, rotated so a point is at the top)
        ring = RegularPolygon(n=6, radius=1.5, color=WHITE).rotate(PI/2)
        verts = ring.get_vertices() 
        # Vertices index mapping after rotation:
        # 0: Top, 1: Top-Left, 2: Bottom-Left, 3: Bottom, 4: Bottom-Right, 5: Top-Right

        # Helper function to easily draw inner pi bonds
        def get_pi_bond(v1, v2):
            bond = Line(v1, v2, color=WHITE).scale(0.8)
            # Shift the bond slightly towards the center of the ring
            direction = -bond.get_center() / np.linalg.norm(bond.get_center())
            bond.shift(direction * 0.25)
            return bond

        # Draw the 3 alternating pi bonds
        pi1 = get_pi_bond(verts[1], verts[2])
        pi2 = get_pi_bond(verts[3], verts[4])
        pi3 = get_pi_bond(verts[5], verts[0])

        # Create the Substituent Group (NH2) and the lone pair
        nh2 = MarkupText("NH<sub>2</sub>").next_to(verts[0], UP, buff=0.3)
        lone_pair = Circle(radius=0.05, color=YELLOW, fill_opacity=1).next_to(nh2, UP, buff=0.1)
        lone_pair_2 = Circle(radius=0.05, color=YELLOW, fill_opacity=1).next_to(lone_pair, LEFT, buff=0.05)
        lone_pairs = VGroup(lone_pair, lone_pair_2)
        
        # Connect NH2 to the ring
        c_n_bond = Line(verts[0], nh2.get_bottom(), color=WHITE)

        # Group everything together into one molecule
        aniline = VGroup(ring, pi1, pi2, pi3, c_n_bond, nh2, lone_pairs)
        aniline.move_to(LEFT * 3)

        # ---------------------------------------------------------
        # 2. ANIMATE THE DRAWING
        # ---------------------------------------------------------
        title = Text("Positive Resonance (+R) Effect", color=BLUE).to_edge(UP)
        self.play(Write(title))
        
        # Draw the molecule beautifully on screen
        self.play(Create(aniline), run_time=1.5)
        self.wait(0.5)

        # ---------------------------------------------------------
        # 3. DRAW THE MECHANISM ARROWS
        # ---------------------------------------------------------
        # Arrow 1: From the lone pair to the C-N bond
        # We can perfectly snap the arrow to the objects without guessing coordinates!
        arrow1 = CurvedArrow(
            start_point=lone_pairs.get_left() + LEFT*0.1, 
            end_point=c_n_bond.get_center() + LEFT*0.1, 
            angle=-PI/1.5, 
            color=RED
        )

        # Arrow 2: From the Pi bond to the Ortho Carbon (Vertex 1)
        arrow2 = CurvedArrow(
            start_point=pi1.get_center(), 
            end_point=verts[1] + LEFT*0.3, 
            angle=PI/1.5, 
            color=RED
        )

        # Animate electron flow
        self.play(Create(arrow1), run_time=1)
        self.play(Create(arrow2), run_time=1)
        self.wait(1)

        # ---------------------------------------------------------
        # 4. TRANSITION TO NEXT STATE (Intermediate)
        # ---------------------------------------------------------
        # We can dynamically change parts of the molecule to show the new state
        
        # New Double Bond for C=N
        new_pi_bond = Line(verts[0], nh2.get_bottom(), color=WHITE).shift(RIGHT*0.1)
        
        # Positive charge on N
        plus_charge = Text("+", color=RED, font_size=36).next_to(nh2, RIGHT, buff=0.1)
        
        # Negative charge/lone pair on the Ortho Carbon
        ortho_lone_pair = Text(":", color=YELLOW, font_size=36).next_to(verts[1], LEFT, buff=0.1)
        minus_charge = Text("-", color=RED, font_size=36).next_to(ortho_lone_pair, DOWN, buff=0.05)

        # Animate the transition!
        self.play(
            FadeOut(arrow1), FadeOut(arrow2), FadeOut(lone_pairs), FadeOut(pi1), # Remove old features
            Create(new_pi_bond), Write(plus_charge), Write(ortho_lone_pair), Write(minus_charge), # Add new features
            run_time=1.5
        )

        label = Text("Ortho- Carbanion", font_size=24, color=YELLOW).next_to(aniline, DOWN, buff=0.5)
        self.play(Write(label))
        self.wait(2)